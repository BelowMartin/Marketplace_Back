from django.test import TestCase
from django.contrib.auth.models import User
from .models import Photo

# Create your tests here.
class PhotoTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_photo = Photo.objects.create(url="test_url")
        test_photo.save()
    
    def test_photo_content(self):
        photo = Photo.objects.get(id=1)
        url = f'{photo.url}'
        self.assertEqual(url, 'test_url')
