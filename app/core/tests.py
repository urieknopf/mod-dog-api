from core.models import *
from django.test import TestCase

class KeyTestCase(TestCase):

    def setUp(self):
        key_a = Key()
        key_a.save()
    
    def test_key_exists(self):
        key_count = Key.objects.all().count()
        self.assertEqual(key_count, 1)
        self.assertNotEqual(key_count, 0)

class ImageTestCase(TestCase):

    def setUp(self):
        image_a = OriginalImage() # TODO: Figure out how to properly test assigning data to this given the imageField ?
        image_a.save()
    
    def test_image_exists(self):
        image_count = OriginalImage.objects.all().count()
        self.assertEqual(image_count, 1)
        self.assertNotEqual(image_count, 0)