#!/usr/bin/env python3.6
from credentials import Credentials
from user import User 

def create_user(email, user_name, password):
    '''
    Function to create a new user
    '''
    new_user = User(email, user_name, password)
    return new_user

def create_credentials(account,account_name,account_password):
    '''
    Function to create a new credential
    '''
    new_credentials = Credentials(account,account_name,account_password)
    return new_credentials

def save_user(user):
    '''
    Function to save users
    '''
    user.save_user()

def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()

def del_user(user):
    '''
    Function to delete a credentials
    '''
    user.delete_user()

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

def main():
  print("Welcome to your password locker. Do you have an account? y-yes n-no") 


if __name__ == '__main__':

    main()