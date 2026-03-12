# Import the Book class to make it accessible when importing the package
from .book import Book
from .user import User
# Optional: define __all__ to specify public API
__all__ = ["Book", "User"]