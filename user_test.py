import unittest 
from user import User 

class TestContact(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.
    '''
    def setUp(self):
        """
        Set up method to run before each test class
        """
        self.new_user = User("rononyonka@gmail.com","ronyonka","password")
        def test_init(self):
            """
            test_init test case to test if the object is initialized properly
            """

            self.assertEqual(self.new_user.email, "rononyonka@gmail.com")
            self.assertEqual(self.new_user.username, "ronyonka")
            self.assertEqual(self.new_user.password, "password")

        def test_save_user(self):
            """
            test_save_user test case to tesst if the user object is saved into the user list
            """
            self.new_user.save_user()
            self.assertEqual(len(User.user_list),1)

if __name__ == '__main__':
    unittest.main()