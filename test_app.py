import unittest
from app import app, get_letter_value, flash

# In Flask, the app object should not be called as a function (i.e., app()), 
# but it should be used directly as the test client.

class TestApp(unittest.TestCase):
    # The setUp method is called before each test method. It 
    # creates a test client for the Flask app using app.test_client().
    def setUp(self):
        # Create a test client for the app
        self.app = app.test_client()

    def test_home(self):
        response = self.app.get("/")
        # The b before the string indicates that it's a byte-string, 
        # as response data is usually in bytes.
        self.assertIn (b'<h1>Words to images</h1>', response.data)

    def test_get_letter_value(self):
        response = get_letter_value('E')
        self.assertEqual(response, 2)
        response = get_letter_value('c')
        self.assertEqual(response, 1)
        response = get_letter_value('b')
        self.assertEqual(response, 4)
        response = get_letter_value(' ')
        self.assertEqual(response, 0)
        response = get_letter_value('3')
        self.assertEqual(response, 0)

if __name__ == "__main__":
    unittest.main()