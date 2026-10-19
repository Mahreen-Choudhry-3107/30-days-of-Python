# Project 04: Log Analyzer CLI

**Day 28 project** | Difficulty: ⭐⭐⭐

Parses access logs (Common Log Format) and reports totals, status codes, top IPs, and top paths.

## Usage

```bash
python loganalyzer.py sample.log
python loganalyzer.py sample.log --top 3
python loganalyzer.py sample.log --status 4          # only 4xx responses
python loganalyzer.py sample.log --format json
python loganalyzer.py --help
```

## Concepts used

`argparse`, regex with named groups, generators (constant memory for huge logs), `Counter`, JSON output, exit codes, stderr.

## Extension ideas

- Filter by date range using `datetime`.
- Detect suspicious IPs (many 401/404 responses).
- Add `--watch` mode that follows a growing file.
- Package it with `pyproject.toml` and a console script (Day 29).
