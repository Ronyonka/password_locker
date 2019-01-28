#!/usr/bin/env python3.6
from credentials import Credentials
from user import User 
import getpass

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
    user.save_user(user)

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
    print("Hello Welcome to Password. What is your name?")
    u_name = input() 

    print("Hello "+str(u_name)+" welcome")
    print('\n')
    
    print("Use these short codes:\n [y] - Yes \n [n] - No")
    status = input("Do you have a Password Locker account yet?")

    if status == 'y':
        print("Sign in")
    elif status == 'n':
        print("Let Me Help you Create an account")
        e_mail= input('Enter email: ')
        u_name= input('Select Username: ')
        key = getpass.getpass('Password: ')
        key2 = getpass.getpass('Re-enter Password: ')

        if key == key2:
            print("New Password Locker Account for " +str(u_name)+" has been created")
        else :
            print("Passwords do not match")
    else:
        print("Invalid input")


#    print(f"Hello {user_name}. what would you like to do?")
    #print('\n')

#     while True:
#     print("Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, ex -exit the contact list ")

#     short_code = input().lower()

#     if short_code == 'cc':
#     print("New Contact")
#     print("-"*10)

#     print ("First name ....")
#     f_name = input()

#     print("Last name ...")
#     l_name = input()

#     print("Phone number ...")
#     p_number = input()

#     print("Email address ...")
#     e_address = input()


#     save_contacts(create_contact(f_name,l_name,p_number,e_address)) # create and save new contact.
#     print ('\n')
#     print(f"New Contact {f_name} {l_name} created")
#     print ('\n')

# elif short_code == 'dc':

# if display_contacts():
#     print("Here is a list of all your contacts")
#     print('\n')

#     for contact in display_contacts():
#             print(f"{contact.first_name} {contact.last_name} .....{contact.phone_number}")

#     print('\n')
# else:
#     print('\n')
#     print("You dont seem to have any contacts saved yet")
#     print('\n')

# elif short_code == 'fc':

# print("Enter the number you want to search for")

# search_number = input()
# if check_existing_contacts(search_number):
#     search_contact = find_contact(search_number)
#     print(f"{search_contact.first_name} {search_contact.last_name}")
#     print('-' * 20)

#     print(f"Phone number.......{search_contact.phone_number}")
#     print(f"Email address.......{search_contact.email}")
# else:
#     print("That contact does not exist")

# elif short_code == "ex":
# print("Bye .......")
# break
# else:
# print("I really didn't get that. Please use the short codes")

# def main():
#     while True:
#         print("Welcome to your password locker. Do you have an account? y-yes n-no") 
#         status = input()
        
#         if status == 'n':
#             # print('Enter email:')
#             e_mail= input('Enter email:')

#             # print('Enter Username:')
#             u_name= input('Enter Username:')

#             # print('Enter Password')
#             p_word= str(input('Enter Password:'))

#         save_user(create_user(e_mail,u_name,p_word))
#         print('\n')
    
#         print("New Password Locker Account for has been created")

#         print('\n')
        
        
if __name__ == '__main__':

    main()