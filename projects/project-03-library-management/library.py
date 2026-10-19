"""Library Management System - Week 3 project.

Concepts used: classes, dataclasses, enums, custom exceptions,
composition, dates/timedelta, comprehensions, and type hints.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, timedelta

LOAN_DAYS = 14
MAX_BOOKS_PER_MEMBER = 3
LATE_FEE_PER_DAY = 10  # currency units


# ---------- exceptions ----------
class LibraryError(Exception):
    """Base class for library errors."""


class BookNotFoundError(LibraryError):
    pass


class MemberNotFoundError(LibraryError):
    pass


class BookUnavailableError(LibraryError):
    pass


class BorrowLimitError(LibraryError):
    pass


class NotBorrowedError(LibraryError):
    pass


# ---------- models ----------
@dataclass
class Book:
    isbn: str
    title: str
    author: str
    available: bool = True


@dataclass
class Loan:
    book: Book
    due_date: date
    borrowed_on: date = field(default_factory=date.today)

    def days_overdue(self, today: date | None = None) -> int:
        today = today or date.today()
        return max((today - self.due_date).days, 0)

    def late_fee(self, today: date | None = None) -> int:
        return self.days_overdue(today) * LATE_FEE_PER_DAY


@dataclass
class Member:
    member_id: int
    name: str
    loans: dict[str, Loan] = field(default_factory=dict)  # isbn -> Loan

    def can_borrow(self) -> bool:
        return len(self.loans) < MAX_BOOKS_PER_MEMBER


# ---------- service ----------
class Library:
    def __init__(self) -> None:
        self._books: dict[str, Book] = {}
        self._members: dict[int, Member] = {}

    # --- setup ---
    def add_book(self, isbn: str, title: str, author: str) -> Book:
        book = Book(isbn, title, author)
        self._books[isbn] = book
        return book

    def add_member(self, member_id: int, name: str) -> Member:
        member = Member(member_id, name)
        self._members[member_id] = member
        return member

    # --- lookups ---
    def get_book(self, isbn: str) -> Book:
        try:
            return self._books[isbn]
        except KeyError:
            raise BookNotFoundError(f"No book with ISBN {isbn}") from None

    def get_member(self, member_id: int) -> Member:
        try:
            return self._members[member_id]
        except KeyError:
            raise MemberNotFoundError(f"No member with id {member_id}") from None

    def search(self, query: str) -> list[Book]:
        q = query.lower()
        return [b for b in self._books.values()
                if q in b.title.lower() or q in b.author.lower()]

    # --- operations ---
    def borrow(self, member_id: int, isbn: str, today: date | None = None) -> Loan:
        today = today or date.today()
        member = self.get_member(member_id)
        book = self.get_book(isbn)
        if not book.available:
            raise BookUnavailableError(f"'{book.title}' is already borrowed")
        if not member.can_borrow():
            raise BorrowLimitError(
                f"{member.name} reached the limit of {MAX_BOOKS_PER_MEMBER} books")

        loan = Loan(book, due_date=today + timedelta(days=LOAN_DAYS), borrowed_on=today)
        member.loans[isbn] = loan
        book.available = False
        return loan

    def return_book(self, member_id: int, isbn: str, today: date | None = None) -> int:
        """Return a book. Gives back the late fee (0 if on time)."""
        member = self.get_member(member_id)
        loan = member.loans.get(isbn)
        if loan is None:
            raise NotBorrowedError(f"{member.name} has not borrowed ISBN {isbn}")
        fee = loan.late_fee(today)
        del member.loans[isbn]
        loan.book.available = True
        return fee

    def overdue_report(self, today: date | None = None) -> list[tuple[str, str, int]]:
        today = today or date.today()
        return [
            (m.name, loan.book.title, loan.days_overdue(today))
            for m in self._members.values()
            for loan in m.loans.values()
            if loan.days_overdue(today) > 0
        ]


# ---------- demo ----------
def demo() -> None:
    lib = Library()
    lib.add_book("111", "Clean Code", "Robert Martin")
    lib.add_book("222", "Fluent Python", "Luciano Ramalho")
    lib.add_member(1, "Ali")

    loan = lib.borrow(1, "111")
    print(f"Borrowed '{loan.book.title}', due {loan.due_date}")

    try:
        lib.borrow(1, "111")
    except BookUnavailableError as err:
        print("Error:", err)

    late_day = date.today() + timedelta(days=20)
    print("Overdue:", lib.overdue_report(late_day))
    print("Late fee:", lib.return_book(1, "111", late_day))
    print("Search 'python':", [b.title for b in lib.search("python")])


if __name__ == "__main__":
    demo()
