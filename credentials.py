import pyperclip
import random
import string

class Credentials:
    ''' The credentials class would hold all the information of the user
    '''
    credential_list = []
    def __init__(self,user_account,account_password):
         self.user_account = user_account
         self.account_password = account_password

    def save_credential(self):
        '''save_credential method saves credential objects into credential list
        '''
        Credentials.credential_list.append(self)

    def delete_credential(self):

        '''
        delete_credential method deletes a saved account from the credential_list
        '''

        Credentials.credential_list.remove(self)

    @classmethod
    def find_by_name(cls,user_account):
        '''
        This method helps to search through the credential list using the username.
        '''
        for credential in cls.credential_list:
            if credential.user_account == user_account:
                return credential

    @classmethod
    def copy_credential(cls,user_account):
        '''
        This method allows a user copy the generated password on the clipboard
        '''
        find_credential = Credentials.find_by_name(user_account)
        return pyperclip.copy(find_credential.account_password)



    @classmethod
    def display_credential(cls):
        """
        Method which displays all credentials list
        """
        return cls.credential_list


    @classmethod
    def generate_password(stringLength=8,char= string.ascii_letters+string.digits):
      '''
      This is a method to generate random string passwords for the application
      '''

      gen_pass = ''.join(random.choice(char) for i in range(stringLength))
      return gen_pass
      

    @classmethod
    def credential_exists(cls,name):
        """
        This method would check if a certain credential exists
        """
        for credential in cls.credential_list:
            if credential.user_account == name:
                return True
            return False

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
