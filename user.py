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

    # def save_user(self):
    #     """
    #     save_user method saves users into user list
    #     """
    #     User.user_list.append(self)

    # def delete_user(self):
    #     """
    #     delete_user method deletes already saved users from user list
    #     """
    #     User.user_list.remove(self)

    

    
