# 30 Days of Python — From Zero to Advanced

A structured, hands-on 30-day path to learn Python, from your very first `print()` to building, testing, and packaging real applications. Each day has detailed notes, code examples, common mistakes, exercises, and a mini project. Six complete projects are included.

**Who is it for?** Complete beginners, college students, freshers, and developers coming from other languages.
**Time needed:** about 2–3 hours per day.
**Python version:** 3.10 or newer.

## 🧭 How to use this repository

1. Follow the days **in order**; each builds on the previous one.
2. **Type the code yourself** instead of copying it.
3. Do the **exercises** before moving on; build the **mini project** of the day.
4. Try each weekly project yourself first, then compare with the solution in `projects/`.
5. Commit your own solutions to Git daily to build a streak and a portfolio.

## ⚙️ Setup

```bash
git clone https://github.com/<your-username>/30-days-of-python.git
cd 30-days-of-python

python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

pip install -r requirements.txt    # needed from Day 22 onwards
```

## 🗓️ Roadmap

### Phase 1 — Foundations (Days 1–7)
| Day | Topic |
|-----|-------|
| 01 | [Introduction to Python](phase-1-foundations/day-01-introduction/README.md) |
| 02 | [Variables & Data Types](phase-1-foundations/day-02-variables-and-data-types/README.md) |
| 03 | [Strings](phase-1-foundations/day-03-strings/README.md) |
| 04 | [Operators & Conditionals](phase-1-foundations/day-04-operators-and-conditionals/README.md) |
| 05 | [Loops](phase-1-foundations/day-05-loops/README.md) |
| 06 | [Lists & Tuples](phase-1-foundations/day-06-lists-and-tuples/README.md) |
| 07 | [Dictionaries & Sets + **Project 1**](phase-1-foundations/day-07-dictionaries-and-sets/README.md) |

### Phase 2 — Intermediate (Days 8–14)
| Day | Topic |
|-----|-------|
| 08 | [Functions](phase-2-intermediate/day-08-functions/README.md) |
| 09 | [Advanced Functions](phase-2-intermediate/day-09-advanced-functions/README.md) |
| 10 | [Modules, Packages & Standard Library](phase-2-intermediate/day-10-modules-and-packages/README.md) |
| 11 | [File Handling (Text, CSV, JSON)](phase-2-intermediate/day-11-file-handling/README.md) |
| 12 | [Exception Handling](phase-2-intermediate/day-12-exception-handling/README.md) |
| 13 | [Comprehensions, Iterators & Generators](phase-2-intermediate/day-13-comprehensions-and-generators/README.md) |
| 14 | [Review + **Project 2**](phase-2-intermediate/day-14-review-and-expense-tracker/README.md) |

### Phase 3 — Object-Oriented Python (Days 15–21)
| Day | Topic |
|-----|-------|
| 15 | [Classes & Objects](phase-3-object-oriented/day-15-classes-and-objects/README.md) |
| 16 | [Inheritance & Polymorphism](phase-3-object-oriented/day-16-inheritance-and-polymorphism/README.md) |
| 17 | [Encapsulation & Dunder Methods](phase-3-object-oriented/day-17-encapsulation-and-dunder-methods/README.md) |
| 18 | [Closures & Decorators](phase-3-object-oriented/day-18-closures-and-decorators/README.md) |
| 19 | [Context Managers, Dataclasses, Enums & Type Hints](phase-3-object-oriented/day-19-context-managers-dataclasses-enums/README.md) |
| 20 | [Regex & Datetime](phase-3-object-oriented/day-20-regex-and-datetime/README.md) |
| 21 | [Review + **Project 3**](phase-3-object-oriented/day-21-review-and-library-system/README.md) |

### Phase 4 — Advanced & Professional (Days 22–30)
| Day | Topic |
|-----|-------|
| 22 | [Testing, Debugging & Logging](phase-4-advanced/day-22-testing-debugging-logging/README.md) |
| 23 | [Concurrency: Threads, Processes, Asyncio](phase-4-advanced/day-23-concurrency/README.md) |
| 24 | [Databases with SQLite](phase-4-advanced/day-24-databases-with-sqlite/README.md) |
| 25 | [HTTP APIs & Web Scraping](phase-4-advanced/day-25-http-apis-and-web-scraping/README.md) |
| 26 | [REST API with FastAPI](phase-4-advanced/day-26-rest-api-with-fastapi/README.md) |
| 27 | [Data Analysis: NumPy, pandas, Matplotlib + **Project 5**](phase-4-advanced/day-27-data-analysis/README.md) |
| 28 | [CLI Tools & Automation + **Project 4**](phase-4-advanced/day-28-cli-tools-and-automation/README.md) |
| 29 | [Best Practices, Performance & Packaging](phase-4-advanced/day-29-best-practices-and-packaging/README.md) |
| 30 | [Capstone: **Project 6** & Next Steps](phase-4-advanced/day-30-capstone-and-next-steps/README.md) |

## 🛠️ Projects

| # | Project | Level | Skills |
|---|---------|-------|--------|
| 1 | [Number Guessing Game](projects/project-01-number-guessing-game/README.md) | ⭐ | loops, conditionals, functions, validation |
| 2 | [Expense Tracker](projects/project-02-expense-tracker/README.md) | ⭐⭐ | JSON storage, exceptions, comprehensions |
| 3 | [Library Management System](projects/project-03-library-management/README.md) | ⭐⭐⭐ | OOP, dataclasses, custom exceptions, tests |
| 4 | [Log Analyzer CLI](projects/project-04-log-analyzer-cli/README.md) | ⭐⭐⭐ | argparse, regex, generators |
| 5 | [Sales Data Analysis](projects/project-05-sales-data-analysis/README.md) | ⭐⭐⭐ | pandas, Matplotlib |
| 6 | [URL Shortener API (Capstone)](projects/project-06-url-shortener-api/README.md) | ⭐⭐⭐⭐ | FastAPI, SQLite, caching, rate limiting, pytest |

## 📚 Resources

- [Python Cheat Sheet](resources/python-cheatsheet.md)
- [Python Interview Questions](resources/interview-questions.md)
- [Further Resources](resources/further-resources.md)

## 📁 Repository structure

```
30-days-of-python/
├── README.md
├── requirements.txt
├── phase-1-foundations/            # Days 1-7
├── phase-2-intermediate/           # Days 8-14
├── phase-3-object-oriented/        # Days 15-21
├── phase-4-advanced/               # Days 22-30
├── projects/                       # 6 complete projects
└── resources/                      # cheat sheet, interview questions, links
```

## ✅ Progress tracker

Copy this into your own fork and tick the days as you go.

- [ ] Phase 1 (Days 1–7)
- [ ] Phase 2 (Days 8–14)
- [ ] Phase 3 (Days 15–21)
- [ ] Phase 4 (Days 22–30)
- [ ] All 6 projects completed

## 🤝 Contributing

Found a typo or want to improve an explanation? Open an issue or submit a pull request.

## 💡 Tips for success

- Consistency beats intensity: 2 focused hours daily is better than a weekend marathon.
- Read error messages carefully; they usually tell you what is wrong.
- When stuck, simplify the problem, print intermediate values, or use `breakpoint()`.
- Explain each concept in your own words; if you can teach it, you know it.
