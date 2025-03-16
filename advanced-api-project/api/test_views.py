from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Author, Book

class BookAPITestCase(TestCase):
    """Test CRUD operations for the Book model endpoints"""

    @classmethod
    def setUpTestData(cls):
        """Set up test data in a separate test database"""
        cls.user = User.objects.create_user(username="testuser", password="testpassword")
        cls.author = Author.objects.create(name="J.K. Rowling")
        cls.book_data = {"title": "Harry Potter", "publication_year": 1997, "author": cls.author}
        cls.book = Book.objects.create(**cls.book_data)

    def setUp(self):
        """Set up test client and authenticate user"""
        self.client = APIClient()
        self.client.login(username="testuser", password="testpassword")  # ✅ Ensures authentication

    def test_create_book(self):
        """Test creating a book"""
        new_book = {"title": "The Hobbit", "publication_year": 1937, "author": self.author.id}
        response = self.client.post("/api/books/", new_book, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], new_book["title"])

    def test_get_book_list(self):
        """Test retrieving a list of books"""
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_get_book_detail(self):
        """Test retrieving a book by ID"""
        response = self.client.get(f"/api/books/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book.title)

    def test_update_book(self):
        """Test updating a book"""
        update_data = {"title": "Harry Potter and the Chamber of Secrets", "publication_year": 1998, "author": self.author.id}
        response = self.client.put(f"/api/books/{self.book.id}/", update_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], update_data["title"])

    def test_delete_book(self):
        """Test deleting a book"""
        response = self.client.delete(f"/api/books/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    def test_search_books(self):
        """Test searching for a book"""
        response = self.client.get("/api/books/?search=Harry")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_filter_books_by_year(self):
        """Test filtering books by publication year"""
        response = self.client.get("/api/books/?publication_year=1997")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_order_books_by_title(self):
        """Test ordering books by title"""
        response = self.client.get("/api/books/?ordering=title")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
