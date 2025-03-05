from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from book.models import Book, Category, Author, Review
from django.contrib.auth import get_user_model

User = get_user_model()


class BookViewSetTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testadmin', password='testpass')
        self.staff_user = User.objects.create_user(username='staffadmin', password='staffpass', is_staff=True)

        self.author1 = Author.objects.create(full_name='Author1')
        self.author2 = Author.objects.create(full_name='Author2')

        self.category1 = Category.objects.create(name='Category1')
        self.category2 = Category.objects.create(name='Category2')

        self.book1 = Book.objects.create(title="Book1", author=self.author1, description="yaxshi kitob",
                                         category=self.category1, price=30000, file='book/otgan_kunlar.txt',
                                         publication_date='2025-03-04')
        self.book2 = Book.objects.create(title="Book2", author=self.author2, description="zor kitob",
                                         category=self.category2, price=40000, file='book/otm.db',
                                         publication_date='2025-03-04')

        Review.objects.create(book=self.book1, rating=5, user_id=1)
        Review.objects.create(book=self.book2, rating=3, user_id=2)
        Review.objects.create(book=self.book1, rating=4, user_id=1)

    def test_book_list(self):
        url = reverse('book-list')
        self.client.force_login(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

    def test_book_filter_by_categoory(self):
        url = reverse('book-list') + '?category=' + str(self.category1.id)
        self.client.force_login(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_book_detail(self):
        url = reverse("book-detail", args=[self.book1.id])
        self.client.force_login(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['book']['title'], 'Book1')

    def test_top_rated(self):
        url = reverse('book-top-rating')
        self.client.force_login(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[1]['title'], 'Book2')

    def test_average_rating(self):
        url = reverse('book-average-rating', args=[self.book2.id])
        self.client.force_login(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['average_rating'], 3)

    def test_permission_denied_for_anonymous_create(self):
        self.client.logout() # "Log out" to make the client anonymous
        url = reverse('book-list')
        data = {'title': 'Test Book', 'description': 'This is a test book', 'price': 10000}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_permisson_granted_for_staff(self):
        url = reverse('book-list')
        self.client.force_login(user=self.staff_user)
        file = SimpleUploadedFile("test_book.pdf", b"file_content", content_type="application/pdf")

        data = {'title': 'Test Book', 'author': self.author1.id, 'category': self.category1.id, 'description': 'This is a test book', 'file': file, 'price': 10000}
        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_permission_granted_for_staff_update(self):
        url = reverse('book-detail', args=[self.book2.id])
        self.client.force_login(user=self.staff_user)
        response = self.client.patch(url, data={'title': 'Test Book'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_permission_granted_for_staff_delete(self):
        url = reverse('book-detail', args=[self.book2.id])
        self.client.force_login(user=self.staff_user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

