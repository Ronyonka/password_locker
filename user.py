class User:
    """
    Class that generates new instances of user
    """
    user_list = []
    def __init__(self, email, user_name, password):
        """
        __init__ methods helps us define properties for our objects
        """
        self.email = email
        self.user_name = user_name
        self.password = password

    def save_user(self):
        """
        save_user method saves users into user list
        """
        # self.save_user()
        User.user_list.append(self)

    def delete_user(self):
        """
        delete_user method deletes already saved users from user list
        """
        User.user_list.remove(self)

    @classmethod
    def user_exist(cls,user_name):
        '''
        Method that checks if a contact exists from the contact list.
        '''

        for user in cls.user_list:
            if user.user_name == user_name:
                return False

            return True

    
