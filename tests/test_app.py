import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        # Set up the testing environment
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        # Clean up after each test
        pass

    def test_home_page(self):
        # Test the home page
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to Autogen-Assisted-Reflection', response.data)

if __name__ == '__main__':
    unittest.main()
