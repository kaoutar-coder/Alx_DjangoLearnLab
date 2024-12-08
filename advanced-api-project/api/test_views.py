from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from api.models import Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create sample books
        self.book1 = Book.objects.create(
            title="Test Book 1", author="Author 1", publication_year=2020
        )
        self.book2 = Book.objects.create(
            title="Test Book 2", author="Author 2", publication_year=2021
        )
        self.list_url = reverse('book-list')  # Adjust the name if using a different naming scheme

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book(self):
        data = {
            "title": "New Book",
            "author": "New Author",
            "publication_year": 2022
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book(self):
        update_url = reverse('book-detail', args=[self.book1.id])
        data = {"title": "Updated Title"}
        response = self.client.patch(update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_delete_book(self):
        delete_url = reverse('book-detail', args=[self.book1.id])
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_author(self):
        response = self.client.get(f"{self.list_url}?author=Author 1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], "Author 1")

    def test_search_books(self):
        response = self.client.get(f"{self.list_url}?search=Test Book 1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Test Book 1")

    def test_order_books_by_publication_year(self):
        response = self.client.get(f"{self.list_url}?ordering=-publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2021)
