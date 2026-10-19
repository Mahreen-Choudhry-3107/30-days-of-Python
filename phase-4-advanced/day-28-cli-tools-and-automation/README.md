# Day 28: CLI Tools & Automation

> **Phase 4 – Advanced & Professional** | Estimated time: 3 hours

## 🎯 Learning objectives

- Build command-line tools with `argparse`.
- Automate files, processes, and scheduled tasks.
- Use `subprocess` and `shutil` safely.

## 📖 Concepts

### `sys.argv` (the basics)

```python
import sys
print(sys.argv)       # ['script.py', 'arg1', 'arg2']
```

### `argparse`

```python
import argparse

parser = argparse.ArgumentParser(description="Count words in files")
parser.add_argument("files", nargs="+", help="one or more files")
parser.add_argument("-n", "--top", type=int, default=5, help="show top N words")
parser.add_argument("--ignore-case", action="store_true")
parser.add_argument("--format", choices=["text", "json"], default="text")
args = parser.parse_args()

print(args.files, args.top, args.ignore_case)
```

Usage:

```bash
python wc.py a.txt b.txt -n 10 --ignore-case
python wc.py --help           # auto-generated help
```

### Subcommands

```python
parser = argparse.ArgumentParser(prog="todo")
sub = parser.add_subparsers(dest="command", required=True)

add = sub.add_parser("add", help="add a task")
add.add_argument("title")

done = sub.add_parser("done", help="complete a task")
done.add_argument("task_id", type=int)

sub.add_parser("list", help="list tasks")

args = parser.parse_args()
if args.command == "add":
    ...
```

Alternatives: `click` and `typer` provide a more concise API.

### Exit codes and stderr

```python
import sys

def main() -> int:
    try:
        ...
        return 0
    except FileNotFoundError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
```

Convention: `0` = success, non-zero = failure. Write errors to **stderr**, results to **stdout** so tools can be piped.

### Reading from stdin

```python
import sys
for line in sys.stdin:
    print(line.upper(), end="")
```

```bash
cat file.txt | python upper.py
```

### File automation with `pathlib` and `shutil`

```python
from pathlib import Path
import shutil

downloads = Path.home() / "Downloads"
for file in downloads.iterdir():
    if file.is_file():
        target = downloads / (file.suffix.lstrip(".") or "no_extension")
        target.mkdir(exist_ok=True)
        shutil.move(str(file), target / file.name)
```

Other tools: `shutil.copy2`, `shutil.rmtree`, `shutil.make_archive`, `glob`, `fnmatch`, `zipfile`, `tempfile`.

**Tip:** add a `--dry-run` option to any script that deletes or moves files.

### Running other programs with `subprocess`

```python
import subprocess

result = subprocess.run(
    ["git", "status", "--short"],
    capture_output=True, text=True, check=True, timeout=30,
)
print(result.stdout)
```

Security: pass arguments as a **list**; avoid `shell=True` with untrusted input (command injection).

### Scheduling

- Cron (Linux/macOS) / Task Scheduler (Windows) to run scripts periodically.
- In-process scheduling: the `schedule` library or APScheduler.
- Always log output and handle failures, since scheduled jobs run unattended.

### Sending email (concept)

Use `smtplib` with `email.message.EmailMessage`; load credentials from environment variables and use an app password, never your real password.

### Environment variables and config

```python
import os
from pathlib import Path

DEBUG = os.environ.get("DEBUG", "0") == "1"
```

Use a `.env` file with `python-dotenv` for local development and never commit it.

### Rich terminal output (optional)

`rich` and `tqdm` give colored tables and progress bars:

```python
from tqdm import tqdm
for item in tqdm(items):
    process(item)
```

### Packaging a script as a command

In `pyproject.toml`:

```toml
[project.scripts]
loganalyzer = "loganalyzer.cli:main"
```

After `pip install -e .`, `loganalyzer --help` works anywhere.

## ⚠️ Common mistakes

- Printing errors to stdout instead of stderr.
- Using `shell=True` with user input.
- Scripts that delete files without a dry-run or confirmation.
- Hard-coded paths and credentials.

## 🏋️ Exercises

1. Create a CLI that converts temperatures: `convert 100 --from c --to f`.
2. Write a file organizer that sorts a folder by extension with `--dry-run`.
3. Write a `todo` CLI with `add`, `list`, `done`, and JSON storage.
4. Write a script that backs up a folder into a timestamped zip file.
5. Use `subprocess` to run `git log --oneline -5` and format the output.

## 🛠 Mini project: Log analyzer CLI

Parse web-server logs with regex, count status codes, top IPs and paths, and output a text or JSON report with filters via command-line flags.

📁 Complete code: [`projects/project-04-log-analyzer-cli`](../../projects/project-04-log-analyzer-cli/README.md)

## 📝 Summary

- `argparse` turns scripts into proper tools with help and validation.
- Respect stdout/stderr and exit codes.
- Automate carefully: dry runs, logging, and safe subprocess usage.

⬅️ [Day 27](../day-27-data-analysis/README.md) | ➡️ [Day 29 – Best Practices & Packaging](../day-29-best-practices-and-packaging/README.md)
