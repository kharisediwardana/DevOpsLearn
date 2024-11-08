import unittest
from app import app
from datetime import datetime

class IdentityTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.app = app.test_client()
        cls.app.testing = True

    def test_get_time(self):
        current_time = datetime.now()
        print(f"Current Time: {current_time}")

    def test_get_ip(self):
        response = self.app.get('/whoami?whoami=1')
        ip_address = response.get_json()
        print(f"IP Address: {ip_address['client_ip']}") 


if __name__ == '__main__':
    unittest.main()
