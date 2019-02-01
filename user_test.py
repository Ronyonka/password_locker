import unittest 
from user import User 
import pyperclip

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for user class behaviours.
   '''

    def setUp(self):
            '''
            Set up method to run before each test cases tp check if the class initialized
            '''
            self.new_user = User("Ron","Onyonka","sibsmars7")



    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Ron")
        self.assertEqual(self.new_user.last_name,"Onyonka")
        self.assertEqual(self.new_user.password,"sibsmars7")
     
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() 
        self.assertEqual(len(User.user_list),1)  

    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("user","user","users") 
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)
            
if __name__ ==  '__main__':
    unittest.main()
