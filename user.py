
import pyperclip

class User:
    '''
    class that generates instances of users
    '''
    user_list = []
    def __init__(self,first_name,last_name,password):
        '''__init__ methods helps us define properties for out objects
        '''
       
        self.first_name = first_name
        self.last_name = last_name
        self.password = password



    def save_user(self):
        '''save_contact method saves contact objects into contact list
        '''
        User.user_list.append(self)
    
    def delete_user(self):

        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        User.user_list.remove(self)





# class User:
#     """
#     Class that generates new instances of user
#     """
#     user_list = []
#     def __init__(self, email, last_name, password):
#         """
#         __init__ methods helps us define properties for our objects
#         """
#         self.email = email
#         self.last_name = last_name
#         self.password = password

#     def save_user(self):
#         """
#         save_user method saves users into user list
#         """
#         # self.save_user()
#         User.user_list.append(self)

#     def delete_user(self):
#         """
#         delete_user method deletes already saved users from user list
#         """
#         User.user_list.remove(self)

#     @classmethod
#     def user_exist(cls,last_name):
#         '''
#         Method that checks if a contact exists from the contact list.
#         '''

#         for user in cls.user_list:
#             if user.last_name == last_name:
#                 return False

#             return True

    
