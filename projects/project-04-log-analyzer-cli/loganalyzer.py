"""Log Analyzer CLI - Day 28 project.

Parses web-server access logs (Common Log Format) and prints a report.

Concepts used: argparse, regex, collections.Counter, generators,
json output, stderr/exit codes, and type hints.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from collections.abc import Iterator
from pathlib import Path

LOG_PATTERN = re.compile(
    r'(?P<ip>\S+) \S+ \S+ \[(?P<time>[^\]]+)\] '
    r'"(?P<method>[A-Z]+) (?P<path>\S+)[^"]*" (?P<status>\d{3}) (?P<size>\d+|-)'
)


def parse_lines(lines: Iterator[str]) -> Iterator[dict]:
    """Yield a dict for each valid log line; skip malformed lines."""
    for line in lines:
        match = LOG_PATTERN.match(line)
        if match:
            yield match.groupdict()


def read_log(path: Path) -> Iterator[dict]:
    with path.open(encoding="utf-8") as f:
        yield from parse_lines(f)


def analyze(entries: Iterator[dict], status: str | None = None,
            top: int = 5) -> dict:
    ips, paths, statuses = Counter(), Counter(), Counter()
    total = errors = bytes_sent = 0

    for e in entries:
        statuses[e["status"]] += 1
        if status and not e["status"].startswith(status):
            continue
        total += 1
        ips[e["ip"]] += 1
        paths[e["path"]] += 1
        if e["status"].startswith(("4", "5")):
            errors += 1
        if e["size"] != "-":
            bytes_sent += int(e["size"])

    return {
        "total_requests": total,
        "error_requests": errors,
        "bytes_sent": bytes_sent,
        "status_counts": dict(sorted(statuses.items())),
        "top_ips": ips.most_common(top),
        "top_paths": paths.most_common(top),
    }


def format_text(report: dict) -> str:
    lines = [
        "=== Log Report ===",
        f"Total requests : {report['total_requests']}",
        f"Error requests : {report['error_requests']}",
        f"Bytes sent     : {report['bytes_sent']:,}",
        "",
        "Status codes:",
    ]
    lines += [f"  {code}: {count}" for code, count in report["status_counts"].items()]
    lines += ["", "Top IPs:"]
    lines += [f"  {ip:<16} {count}" for ip, count in report["top_ips"]]
    lines += ["", "Top paths:"]
    lines += [f"  {path:<20} {count}" for path, count in report["top_paths"]]
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Analyze web-server access logs.")
    p.add_argument("logfile", type=Path, help="path to the access log")
    p.add_argument("-n", "--top", type=int, default=5, help="entries in top lists")
    p.add_argument("--status", help="only count status codes starting with this "
                                    "prefix (e.g. 4 for all 4xx, 404 for 404)")
    p.add_argument("--format", choices=["text", "json"], default="text")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if not args.logfile.exists():
        print(f"error: file not found: {args.logfile}", file=sys.stderr)
        return 1

    report = analyze(read_log(args.logfile), status=args.status, top=args.top)
    if args.format == "json":
        print(json.dumps(report, indent=2))
    else:
        print(format_text(report))
    return 0


if __name__ == "__main__":
    sys.exit(main())
