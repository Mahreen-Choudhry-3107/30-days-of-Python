# Day 24: Databases with SQLite

> **Phase 4 – Advanced & Professional** | Estimated time: 3 hours

## 🎯 Learning objectives

- Use SQL from Python with the built-in `sqlite3` module.
- Perform CRUD safely with parameterized queries.
- Understand transactions, indexes, and joins.
- Get an introduction to ORMs.

## 📖 Concepts

### Why SQLite?

A serverless, file-based relational database bundled with Python. Perfect for learning, scripts, prototypes, and small applications.

### Connecting and creating a table

```python
import sqlite3

conn = sqlite3.connect("app.db")          # use ":memory:" for a temporary DB
conn.row_factory = sqlite3.Row            # access columns by name
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    name    TEXT NOT NULL,
    email   TEXT NOT NULL UNIQUE,
    age     INTEGER CHECK (age >= 0)
)
""")
conn.commit()
```

### CRUD

```python
# Create
cur.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
            ("Ali", "ali@example.com", 22))
conn.commit()
new_id = cur.lastrowid

# Read
cur.execute("SELECT * FROM users WHERE age > ?", (18,))
for row in cur.fetchall():
    print(row["id"], row["name"])
one = cur.execute("SELECT * FROM users WHERE id = ?", (1,)).fetchone()

# Update
cur.execute("UPDATE users SET age = ? WHERE id = ?", (23, 1))

# Delete
cur.execute("DELETE FROM users WHERE id = ?", (1,))
conn.commit()
```

### 🔒 Parameterized queries (SQL injection)

**Never** build SQL with string formatting:

```python
# DANGEROUS
cur.execute(f"SELECT * FROM users WHERE name = '{name}'")

# SAFE
cur.execute("SELECT * FROM users WHERE name = ?", (name,))
```

Placeholders apply to **values** only, not table or column names. Validate identifiers against an allow-list.

### Bulk inserts

```python
rows = [("A", "a@x.com", 20), ("B", "b@x.com", 30)]
cur.executemany("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", rows)
conn.commit()
```

### Transactions and context managers

```python
try:
    with conn:                      # commits on success, rolls back on error
        conn.execute("UPDATE accounts SET balance = balance - ? WHERE id = ?", (100, 1))
        conn.execute("UPDATE accounts SET balance = balance + ? WHERE id = ?", (100, 2))
except sqlite3.Error as e:
    print("Transfer failed:", e)
```

Note: `with conn` does **not** close the connection. Close it explicitly or use `contextlib.closing`.

### Relationships and joins

```python
conn.executescript("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id),
    total REAL NOT NULL
);
""")
conn.execute("PRAGMA foreign_keys = ON")      # needed per connection

cur.execute("""
SELECT u.name, SUM(o.total) AS spent
FROM users u
JOIN orders o ON o.user_id = u.id
GROUP BY u.id
HAVING spent > 100
ORDER BY spent DESC
""")
```

### Indexes

```python
cur.execute("CREATE INDEX IF NOT EXISTS idx_users_email ON users(email)")
cur.execute("EXPLAIN QUERY PLAN SELECT * FROM users WHERE email = ?", ("a@x.com",)).fetchall()
```

### Repository pattern (clean structure)

```python
class UserRepository:
    def __init__(self, conn):
        self.conn = conn

    def add(self, name, email):
        with self.conn:
            cur = self.conn.execute(
                "INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        return cur.lastrowid

    def get(self, user_id):
        return self.conn.execute(
            "SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
```

### ORMs (introduction)

An ORM maps tables to Python classes. The most popular is **SQLAlchemy**:

```python
from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

class Base(DeclarativeBase): pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))

engine = create_engine("sqlite:///app.db")
Base.metadata.create_all(engine)

with Session(engine) as session:
    session.add(User(name="Ali"))
    session.commit()
```

Revisit the N+1 query problem and indexing notes from the backend handbook when you use an ORM.

### Other databases

PostgreSQL (`psycopg`), MySQL (`mysql-connector`), and MongoDB (`pymongo`) work similarly: connect, execute, fetch, commit.

## ⚠️ Common mistakes

- String-formatting values into SQL (injection risk).
- Forgetting `commit()`; changes are lost.
- Not enabling `PRAGMA foreign_keys = ON`.
- Sharing one SQLite connection across threads without care.
- Opening a new connection for every tiny query in a web app (use pooling or a per-request connection).

## 🏋️ Exercises

1. Create a `students` table and insert 5 rows; query those with marks > 70.
2. Implement update and delete by ID with confirmation of affected rows (`cur.rowcount`).
3. Create `authors` and `books` tables and write a JOIN query listing each book with its author.
4. Demonstrate a transaction rollback when a transfer fails halfway.
5. Add an index and compare `EXPLAIN QUERY PLAN` output before and after.

## 🛠 Mini project: Contact book with SQLite

CLI app with add, search (partial name), update, delete, and export-to-CSV features using a repository class and parameterized queries.

## 📝 Summary

- `sqlite3` gives you a full SQL database with zero setup.
- Always use parameterized queries and transactions.
- Understand joins and indexes; ORMs build on the same ideas.

⬅️ [Day 23](../day-23-concurrency/README.md) | ➡️ [Day 25 – HTTP APIs & Web Scraping](../day-25-http-apis-and-web-scraping/README.md)
