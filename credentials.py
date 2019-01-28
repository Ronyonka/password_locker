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