# Day 26: Building a REST API with FastAPI

> **Phase 4 – Advanced & Professional** | Estimated time: 3.5 hours

## 🎯 Learning objectives

- Build a REST API with FastAPI and Pydantic.
- Use path/query parameters, request bodies, status codes, and dependencies.
- Handle errors and test the API.

> 📚 Pair this day with the backend concepts: REST, HTTP methods and status codes, authentication vs authorization, rate limiting, and SQL injection prevention.

## 📖 Concepts

### Setup

```bash
pip install fastapi uvicorn httpx
```

### Hello API

`main.py`:

```python
from fastapi import FastAPI

app = FastAPI(title="Demo API")

@app.get("/")
def root():
    return {"message": "Hello, API"}
```

Run:

```bash
uvicorn main:app --reload
```

Open `http://127.0.0.1:8000/docs` for automatic interactive documentation (Swagger UI).

### Path and query parameters

```python
@app.get("/items/{item_id}")
def get_item(item_id: int, verbose: bool = False):
    return {"id": item_id, "verbose": verbose}

@app.get("/search")
def search(q: str, limit: int = 10, skip: int = 0):
    return {"q": q, "limit": limit, "skip": skip}
```

FastAPI validates types automatically and returns `422` for invalid values.

### Request bodies with Pydantic

```python
from pydantic import BaseModel, Field, EmailStr   # EmailStr needs email-validator

class ItemCreate(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    price: float = Field(gt=0)
    in_stock: bool = True

class Item(ItemCreate):
    id: int

@app.post("/items", response_model=Item, status_code=201)
def create_item(payload: ItemCreate):
    ...
```

Separate **input models** from **output models** so you never leak internal fields (like password hashes).

### A complete in-memory CRUD

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()
items: dict[int, Item] = {}
next_id = 1

@app.post("/items", response_model=Item, status_code=201)
def create_item(payload: ItemCreate):
    global next_id
    item = Item(id=next_id, **payload.model_dump())
    items[next_id] = item
    next_id += 1
    return item

@app.get("/items", response_model=list[Item])
def list_items(skip: int = 0, limit: int = 10):
    return list(items.values())[skip: skip + limit]

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

@app.patch("/items/{item_id}", response_model=Item)
def update_item(item_id: int, changes: dict):
    ...

@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if items.pop(item_id, None) is None:
        raise HTTPException(status_code=404, detail="Item not found")
```

### Dependency injection

```python
from fastapi import Depends

def get_db():
    conn = sqlite3.connect("app.db")
    try:
        yield conn
    finally:
        conn.close()

@app.get("/users/{user_id}")
def get_user(user_id: int, db = Depends(get_db)):
    row = db.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
    ...
```

Dependencies are also used for authentication, pagination parameters, and permission checks.

### Authentication sketch

```python
from fastapi import Header, HTTPException

def require_api_key(x_api_key: str = Header(...)):
    if x_api_key != os.environ["API_KEY"]:
        raise HTTPException(status_code=401, detail="Invalid API key")

@app.delete("/items/{item_id}", dependencies=[Depends(require_api_key)])
def protected_delete(item_id: int): ...
```

For real apps use OAuth2 / JWT (`fastapi.security`) with hashed passwords (`bcrypt` or `argon2`), HTTPS, and short-lived tokens.

### `async def` vs `def`

Use `async def` only if you await async I/O inside. Plain `def` endpoints run in a thread pool, so blocking code is fine there.

### Testing the API

```python
from fastapi.testclient import TestClient

client = TestClient(app)

def test_create_and_read():
    r = client.post("/items", json={"name": "Pen", "price": 1.5})
    assert r.status_code == 201
    item_id = r.json()["id"]
    assert client.get(f"/items/{item_id}").json()["name"] == "Pen"

def test_not_found():
    assert client.get("/items/9999").status_code == 404
```

### Project structure for larger apps

```
app/
├── main.py          # create app, include routers
├── routers/
├── models.py        # database models
├── schemas.py       # Pydantic models
├── crud.py          # database operations
├── dependencies.py
└── config.py        # settings from environment variables
tests/
```

### Production notes

- Run with `uvicorn`/`gunicorn` behind a reverse proxy; terminate TLS at the proxy.
- Configure CORS only for trusted origins.
- Add rate limiting, structured logging, and health-check endpoints (`/health`).
- Version your API (`/api/v1/...`).

## ⚠️ Common mistakes

- Returning database models directly (leaking fields).
- Blocking calls inside `async def` endpoints.
- Storing global mutable state in multi-worker deployments (in-memory data is per process).
- Forgetting proper status codes (`201`, `204`, `404`, `409`).

## 🏋️ Exercises

1. Build a "books" CRUD API with validation.
2. Add pagination and a search query parameter.
3. Add API-key protection to the write endpoints.
4. Return `409 Conflict` when creating a duplicate resource.
5. Write tests for every endpoint using `TestClient`.

## 🛠 Mini project: Notes API with SQLite

Endpoints to create, list, update, and delete notes stored in SQLite, with pagination, validation, and tests.

## 📝 Summary

- FastAPI + Pydantic gives validation, docs, and speed with little code.
- Use proper status codes, response models, and dependencies.
- Test with `TestClient`.

⬅️ [Day 25](../day-25-http-apis-and-web-scraping/README.md) | ➡️ [Day 27 – Data Analysis](../day-27-data-analysis/README.md)
