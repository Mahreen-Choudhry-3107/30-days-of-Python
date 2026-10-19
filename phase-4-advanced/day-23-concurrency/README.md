# Day 23: Concurrency (Threading, Multiprocessing, Asyncio)

> **Phase 4 – Advanced & Professional** | Estimated time: 3.5 hours

## 🎯 Learning objectives

- Distinguish concurrency from parallelism and I/O-bound from CPU-bound work.
- Use threads, processes, and `concurrent.futures`.
- Write basic `async` / `await` programs.

## 📖 Concepts

### Key ideas

- **Concurrency:** managing multiple tasks making progress in overlapping time.
- **Parallelism:** tasks literally running at the same moment on multiple cores.
- **I/O-bound:** waiting on network, disk, or database.
- **CPU-bound:** heavy computation.

### The GIL

In standard CPython, the **Global Interpreter Lock** lets only one thread execute Python bytecode at a time. Consequences:

| Workload | Best tool |
|----------|-----------|
| I/O-bound | threads or asyncio |
| CPU-bound | multiprocessing (or native extensions like NumPy) |

(Recent Python versions include experimental free-threaded builds, but standard builds still use the GIL.)

### Threading

```python
import threading, time

def worker(name, seconds):
    print(f"{name} started")
    time.sleep(seconds)
    print(f"{name} finished")

threads = [threading.Thread(target=worker, args=(f"T{i}", 1)) for i in range(3)]
for t in threads: t.start()
for t in threads: t.join()          # wait for all
```

### Race conditions and locks

```python
counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100_000):
        with lock:                    # without this, updates can be lost
            counter += 1
```

Other tools: `queue.Queue` (thread-safe), `Event`, `Semaphore`.

### `concurrent.futures`

The simplest high-level API.

```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed

def fetch(url):
    ...    # e.g. requests.get

urls = ["https://a.com", "https://b.com"]
with ThreadPoolExecutor(max_workers=8) as pool:
    results = list(pool.map(fetch, urls))

with ThreadPoolExecutor() as pool:
    futures = {pool.submit(fetch, u): u for u in urls}
    for fut in as_completed(futures):
        print(futures[fut], fut.result())
```

### Multiprocessing

```python
def heavy(n):
    return sum(i * i for i in range(n))

if __name__ == "__main__":          # required on Windows/macOS
    with ProcessPoolExecutor() as pool:
        print(list(pool.map(heavy, [10**6] * 4)))
```

Processes have separate memory; data passed between them is pickled, so there is overhead.

### Asyncio

Single thread, cooperative multitasking using an event loop. Excellent for thousands of concurrent network connections.

```python
import asyncio

async def fetch(name, delay):
    print(f"{name} start")
    await asyncio.sleep(delay)      # non-blocking wait
    print(f"{name} done")
    return name

async def main():
    results = await asyncio.gather(
        fetch("A", 2), fetch("B", 1), fetch("C", 3)
    )
    print(results)

asyncio.run(main())                 # total ~3s, not 6s
```

Rules of thumb:

- `async def` defines a coroutine; `await` pauses it until the awaited thing completes.
- Never call blocking code (`time.sleep`, `requests.get`) inside a coroutine. Use async libraries (`aiohttp`, `httpx.AsyncClient`) or `asyncio.to_thread`.
- Use `asyncio.Semaphore` to limit concurrency, `asyncio.wait_for` for timeouts, and `asyncio.TaskGroup` (3.11+) for structured concurrency.

```python
async def limited(sem, i):
    async with sem:
        await asyncio.sleep(1)

async def main():
    sem = asyncio.Semaphore(5)
    await asyncio.gather(*(limited(sem, i) for i in range(20)))
```

### Which should I use?

| Situation | Choice |
|-----------|--------|
| Many network calls, simple code | `ThreadPoolExecutor` |
| Thousands of connections, async libraries available | `asyncio` |
| Heavy computation | `ProcessPoolExecutor` |
| Simple script, small data | no concurrency at all |

Measure first; concurrency adds complexity.

## ⚠️ Common mistakes

- Using threads to speed up CPU-bound work.
- Shared mutable state without locks.
- Blocking calls inside `async` code.
- Forgetting `if __name__ == "__main__":` with multiprocessing.
- Creating unbounded numbers of threads or tasks.

## 🏋️ Exercises

1. Time 5 sequential `time.sleep(1)` calls vs a thread pool.
2. Compute prime counts for 4 large ranges sequentially and with `ProcessPoolExecutor`; compare timings.
3. Demonstrate a race condition and fix it with a `Lock`.
4. Rewrite a sequential downloader using `asyncio.gather` and a semaphore.
5. Build a producer–consumer pipeline using `queue.Queue` and two threads.

## 🛠 Mini project: Concurrent URL health checker

Given a file of URLs, check each concurrently (thread pool or async), record status code and latency, handle timeouts, and print a sorted report.

## 📝 Summary

- Threads/async help I/O-bound work; processes help CPU-bound work.
- The GIL limits thread parallelism for Python code.
- Protect shared state; avoid blocking the event loop.

⬅️ [Day 22](../day-22-testing-debugging-logging/README.md) | ➡️ [Day 24 – Databases with SQLite](../day-24-databases-with-sqlite/README.md)
