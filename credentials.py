





# import pyperclip
# import random
# import string

# class Credentials:
#     """
#      Class that generates new instances of credentials
#     """
#     credentials_list = []
#     def __init__(self, account, account_name, account_password):
#         self.account = account
#         self.account_name = account_name
#         self.account_password = account_password
    
#     def save_credentials(self):

#         '''
#         save_credentials method saves credential objects into credentials_list
#         '''

#         Credentials.credentials_list.append(self)

#     def delete_credentials(self):

#         '''
#         delete_credentials method deletes a saved credentials from the credentials_list
#         '''

#         Credentials.credentials_list.remove(self)

    # def generate_password(self,stringLength=8,char= string.ascii_letters+string.digits):
    #     '''
    #     This is a method to generate random string passwords for the application
    #     '''

    #     gen_pass = ''.join(random.choice(char) for i in range(stringLength))
    #     return gen_pass

    # @classmethod
    # def find_by_account(cls, account):
    #     '''
    #     Method that takes in a string and returns an account that matches that name
    #     '''
    #     for credentials in cls.credentials_list:
    #         if credentials.account == account:
    #             return credentials

    # @classmethod
    # def credentials_exist(cls,account):
    #     '''
    #     Method that checks if a contact exists from the contact list.
    #     '''

    #     for credentials in cls.credentials_list:
    #         if credentials.account_name == account:
    #             return False

    #         return True

    # @classmethod
    # def display_credentials(cls):
    #     '''
    #     method that returns the credentials list
    #     '''
    #     return cls.credentials_list

    # @classmethod
    # def copy_credential(cls,account_name):
    #     '''
    #     This method allows a user copy the generated password on the clipboard
    #     '''
    #     find_credentials = Credentials.find_by_account(account_name)
    #     return pyperclip.copy(find_credentials.account_password)
