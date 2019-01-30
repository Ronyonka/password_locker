import unittest
from credentials import Credentials
import pyperclip

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
        test case to test if the credentials objects are saved into the credentials list
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []


    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_credentials to check if we can save multiple credentials
        objects to our credentials_list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Test","test user","testpassword") 
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)
 
    def test_delete_credentials(self):
        '''
        test_delete_credentials to test if we can remove a credentials from our credentials list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Test","test user","testpassword")
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_find_credentials_by_account(self):
        '''
        test to check if we can find a credentials by phone account and display information
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Test","test user","testpassword")
        test_credentials.save_credentials()

        found_credentials = Credentials.find_by_account("Test")
        self.assertEqual(found_credentials.account_name, test_credentials.account_name)

    def test_credentials_exists(self):
        '''
        test to check if we can return a boolean if we can not find the credentials
        '''

        self.new_credentials.save_credentials()
        test_credentials =  Credentials("Test","test user","testpassword")
        test_credentials.save_credentials()

        credentials_exist = Credentials.credentials_exist("Test")

        self.assertTrue(credentials_exist)

    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials
        '''

        self.assertEqual(Credentials.display_credentials(), Credentials.credentials_list)





if __name__ == '__main__':
    
    unittest.main()


