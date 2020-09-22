from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Post
from django.urls import reverse
# Create your tests here.

class SnackTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='Dana',
            email='dana@gmail.com',
            password='password'
        )

        self.snack = Post.objects.create(
            title='Hackona Matata',
            author=self.user,
            body='Carton Film'
        )

    def test_snack_list_view(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)

    def test_snack_details_view(self):
        response = self.client.get(reverse('blogs_detail', args='1'))
        self.assertEqual(response.status_code, 200)

    def test_snack_update_view(self):
        response = self.client.post(reverse('update_plog', args='1'), {
            'title': 'Temon',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Temon')

    def test_create_view(self):
        response = self.client.post(reverse('create_blog'), {
            'title': 'Dragon',
            'author': self.user,
            'body' :'Angry Dragon',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dragon')
        self.assertContains(response, 'Angry Dragon')
        self.assertContains(response, 'Dana')

    def test_delete_view(self):
        response = self.client.get(reverse('delete_plog',args='1'))
        self.assertEqual(response.status_code, 200)