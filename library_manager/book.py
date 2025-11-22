from dataclasses import dataclass, field

@dataclass
class Book:
    title: str
    author: str
    isbn: str
    status: str = field(default="available")

    def __post_init__(self):
        self.status = self.status.lower()

    def __str__(self):
        return f"{self.title} by {self.author} | ISBN: {self.isbn} | Status: {self.status}"

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "status": self.status
        }

    def is_available(self):
        return self.status == "available"

    def issue(self):
        if self.is_available():
            self.status = "issued"
            return True
        return False

    def return_book(self):
        if not self.is_available():
            self.status = "available"
            return True
        return False
