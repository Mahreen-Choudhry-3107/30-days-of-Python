import sys
from datetime import date, timedelta
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from library import (BookUnavailableError, BorrowLimitError, Library,
                     NotBorrowedError)


@pytest.fixture
def lib():
    library = Library()
    for i in range(1, 6):
        library.add_book(str(i), f"Book {i}", "Author")
    library.add_member(1, "Ali")
    library.add_member(2, "Sara")
    return library


def test_borrow_marks_book_unavailable(lib):
    lib.borrow(1, "1")
    with pytest.raises(BookUnavailableError):
        lib.borrow(2, "1")


def test_borrow_limit(lib):
    for isbn in ("1", "2", "3"):
        lib.borrow(1, isbn)
    with pytest.raises(BorrowLimitError):
        lib.borrow(1, "4")


def test_return_without_borrow(lib):
    with pytest.raises(NotBorrowedError):
        lib.return_book(1, "1")


def test_late_fee(lib):
    start = date(2025, 1, 1)
    lib.borrow(1, "1", today=start)
    fee = lib.return_book(1, "1", today=start + timedelta(days=17))
    assert fee == 3 * 10


def test_search(lib):
    assert len(lib.search("book 2")) == 1
