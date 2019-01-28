import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    """
    Test class that defines test cases for the credential class behaviours.
    """

    def setUp(self):

        self.new_credential = Credentials('Twitter','ron_onyonka','password3')

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_credential.account, "Twitter")
        self.assertEqual(self.new_credential.account_name, "ron_onyonka")
        self.assertEqual(self.new_credential.account_password, "password3")


if __name__ == '__main__':
    unittest.main()


