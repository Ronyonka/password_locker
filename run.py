#!/usr/bin/env python3.6
from credentials import Credentials

def create_credentials(account,account_name,account_password):
    '''
    Function to create a new credential
    '''
    new_credentials = Credentials(account,account_name,account_password)
    return new_credentials

def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()

def del_credentials(credentials):
    '''
    Function to delete a credentials
    '''
    credentials.delete_credentials()

def find_credentials(account_name):
    '''
    Function that finds a credentials by number and returns the credentials
    '''
    return Credentials.find_by_account(account_name)

def check_existing_credentials(account_name):
    '''
    Function that check if a credentials exists with that number and return a Boolean
    '''
    return Credentials.credentials_exist(account_name)

def display_credentials():
    '''
    Function that returns all the saved credentialss
    '''
    return Credentials.display_credentials()


