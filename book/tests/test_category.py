from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from book.models import Book, Category
from django.contrib.auth import get_user_model

User = get_user_model()


class CategoryTests(APITestCase):
    # python manage.py dumpdata book.Category --format=yaml --indent=4 > book/fixtures/categories.yaml
    fixtures =['categories']

    def setUp(self):
        self.user = User.objects.create_user(username='testadmin', password='testpass')
        self.client.force_login(user=self.user)
        self.category1 = Category.objects.first()

    def test_category_list(self):
        url = reverse('book-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_category_detail(self):
        url = reverse('category-detail', args=[self.category1.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_category_create(self):
        url = reverse('category-list')
        response = self.client.post(url, data={'name': 'Test Category'}, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_category_update(self):
        url = reverse('category-detail', args=[self.category1.id])
        response = self.client.put(url, data={'name': 'Category1'}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_category_delete(self):
        url = reverse('category-detail', args=[self.category1.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)