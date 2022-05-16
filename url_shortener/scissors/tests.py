from django.test import Client
from django.test import TestCase
from django.urls import reverse
from .models import Url


class test_url_list_view(TestCase):

    def setUp(self):
        self.client = Client()
        Url.objects.create(original='https://www.google.com/', path='google')

    def test_list_view(self):
        response = self.client.get(reverse('scissors:list-url'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertTrue('form' in response.context)

    def test_create_view(self):
        data = {'original': 'https://www.w3schools.com/', 'path': 'w3schools'}
        response = self.client.post(reverse('scissors:create-url'), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('scissors:list-url'))

    def test_redirect_view(self):
        response = self.client.get(
            reverse('scissors:redirect-url', args=['google']))
        self.assertEqual(response.status_code, 200)

    def test_copy_path_view(self):
        response = self.client.get(reverse('scissors:copy-url', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_edit_path_view(self):
        url = Url.objects.get(path='google')
        response = self.client.post(reverse('scissors:edit-url', kwargs={'pk': url.id}), {
                                    'original': 'https://www.google.com/', 'path': 'google2'})
        self.assertEqual(response.status_code, 302)

        url.refresh_from_db()
        self.assertEqual(url.path, 'google2')

    def test_redirect_page(self):
        response = self.client.get(reverse('scissors:redirect-page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about_us.html')
