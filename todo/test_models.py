from django.test import TestCase
from .models import Item


class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        item = Item.objects.create(name='Test todo item')
        self.assertFalse(item.done)

    def test_string_returns_name(self):
        item = Item.objects.create(name='Test todo item')
        self.assertTrue(str(item), 'Test todo item')
