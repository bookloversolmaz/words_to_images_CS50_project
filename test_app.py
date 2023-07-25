import unittest
from app import app

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
        self.assertIn(b'<h1>Words to images</h1>', response.data)
        self.assertIn (b'Enter a word or phrase here', response.data)
    def setUp(self):
        # Create a test client for the app
        self.app = app.test_client()
    def images(self):
        response = self.app.post("/images")
        self.assertIn(b'<h1>Images</h1>', response.data)
if __name__ == "__main__":
    unittest.main()