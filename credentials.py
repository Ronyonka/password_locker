class Credentials:
    """
     Class that generates new instances of credentials
    """
    credentials_list = []
    def __init__(self, account, account_name, account_password):
        self.account = account
        self.account_name = account_name
        self.account_password = account_password
    
    def save_credentials(self):

        '''
        save_credentials method saves credential objects into credentials_list
        '''

        Credentials.credentials_list.append(self)

    def delete_credentials(self):

        '''
        delete_credentials method deletes a saved credentials from the credentials_list
        '''

        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_account(cls, account):
        '''
        Method that takes in a string and returns an account that matches that name
        '''
        for credentials in cls.credentials_list:
            if credentials.account == account:
                return credentials