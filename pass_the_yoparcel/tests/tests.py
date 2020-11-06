from django.test import TestCase


class SomeTests(TestCase):

    def test_something(self):
        print('testing something!')
        a = 1
        b = 1
        self.assertEqual(a, b)