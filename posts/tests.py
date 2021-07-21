from unittest.case import expectedFailure
from django.http import response
from django.test import TestCase
from django.urls.base import reverse
from .models import Post

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text = 'I am a test case')
        
    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'I am a test case')

class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text= 'home view test')
        
    def test_view_url_exists_at_proper_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')