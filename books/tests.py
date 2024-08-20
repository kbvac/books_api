from django.test import TestCase
from django.urls import reverse
from .models import Book

class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
        title="A good title",
        description="An excellent subtitle",
        author="Tom Christie",
        isbn="1234567890123",
        year="2005",
        publisher='NEI'
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "A good title")
        self.assertEqual(self.book.description, "An excellent subtitle")
        self.assertEqual(self.book.author, "Tom Christie")
        self.assertEqual(self.book.isbn, "1234567890123")
        self.assertEqual(self.book.year, "2005")
        self.assertEqual(self.book.publisher, "NEI")

    def test_book_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "excellent subtitle")
        self.assertTemplateUsed(response, "books_list.html")