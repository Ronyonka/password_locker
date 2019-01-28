import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    """
    Test class that defines test cases for the credential class behaviours.
    """

    def setUp(self):

        self.new_credentials = Credentials('Twitter','ron_onyonka','password3')

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_credentials.account, "Twitter")
        self.assertEqual(self.new_credentials.account_name, "ron_onyonka")
        self.assertEqual(self.new_credentials.account_password, "password3")

    def test_save_credentials(self):
        '''
        test case to test if the credentials objects are saved into the contact list
        '''
        self.new_credentials.test_save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

if __name__ == '__main__':
    unittest.main()


