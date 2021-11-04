from unittest import TestCase


class When_something(TestCase):

    # Runs before "all" tests
    @classmethod
    def setUpClass(cls):
        pass

    # Runs after "all" tests
    @classmethod
    def tearDownClass(cls):
        pass

    # Runs before "each" test
    def setUp(self):
        pass

    # Runs after "each" test
    def tearDown(self):
        pass

    # A test
    def test_something(self):
        self.assertEqual(1, 1)