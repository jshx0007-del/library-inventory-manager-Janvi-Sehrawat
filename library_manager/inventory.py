import json
import logging
from pathlib import Path
from typing import List, Optional

from library_manager.book import Book

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class LibraryInventory:
    def __init__(self, storage_path="data/books.json"):
        self.storage_path = Path(storage_path)
        self.books: List[Book] = []
        self.load_from_file()

    def add_book(self, book: Book):
        if any(b.isbn == book.isbn for b in self.books):
            raise ValueError("Book with this ISBN already exists.")
        self.books.append(book)
        self.save_to_file()

    def search_by_title(self, title: str):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def search_by_isbn(self, isbn: str) -> Optional[Book]:
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def issue_book(self, isbn: str):
        book = self.search_by_isbn(isbn)
        if not book:
            raise ValueError("Book not found.")
        if not book.issue():
            raise ValueError("Book already issued.")
        self.save_to_file()

    def return_book(self, isbn: str):
        book = self.search_by_isbn(isbn)
        if not book:
            raise ValueError("Book not found.")
        if not book.return_book():
            raise ValueError("Book was not issued.")
        self.save_to_file()

    def display_all(self):
        return self.books

    def save_to_file(self):
        try:
            self.storage_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.storage_path, "w", encoding="utf-8") as file:
                json.dump([b.to_dict() for b in self.books], file, indent=4)
            logger.info("Books saved successfully.")
        except Exception as e:
            logger.error(f"Error saving file: {e}")

    def load_from_file(self):
        if not self.storage_path.exists():
            logger.warning("No file found. Starting with empty library.")
            return

        try:
            with open(self.storage_path, "r", encoding="utf-8") as file:
                data = json.load(file)
            self.books = [Book(**item) for item in data]
            logger.info("Books loaded successfully.")
        except json.JSONDecodeError:
            logger.error("JSON file corrupted. Resetting inventory.")
            self.books = []
        except Exception as e:
            logger.error(f"Error loading file: {e}")
            self.books = []
