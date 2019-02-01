#!/usr/bin/env python3.6
import pyperclip
from user import User
from credentials import Credentials

def create_user(fname, uname, password):
    '''
    This is a function to create a new user
    '''
    new_user = User(fname , uname, password)
    return new_user

def save_user(user):
    '''
    This function saves a new user
    '''
    user.save_user()


def del_user(user):
    '''
    This function deletes a user 
    '''
    user.delete_user()

def create_new_credential(user_account, account_password):
    ''' 
    This function allows a user create a new credential account
    '''
    new_credential = Credentials(user_account , account_password)
    return new_credential

def save_new_credentials(credential):
    ''' 
    This is a function to save new credentials created 
    '''
    credential.save_credential()

def delete_credentials(credential):
    '''
    This is a function to delete credentials by the user 
    '''
    return Credentials.delete_credential(credential)

def verify_user(name):
	'''
	Function that checks if the username already exists in the system
	'''
	checking_user = Credentials.find_by_name(name)
	return checking_user
 
def find_credentials(user_account):
   '''
     Function to find stored credentials
    '''
   return Credentials.find_by_name(user_account)

def check_existing_credentials(name):
   '''
   Function to check if an inputed credential name exists
    '''
   return Credentials.find_by_name(name)

def copy_credential(user_account):
	'''
	Function to copy a credentials details to the clipboard
	'''
	return Credentials.copy_credential(user_account)

def display_credential():
    '''
    Function to display credentials of an account
    '''
    return Credentials.display_credential()

def generate_password():
    '''
    This is a function to generate random password
    '''
    gen_pass = Credentials.generate_password()
    return gen_pass







# from credentials import Credentials
# from user import User 
# import getpass

# def create_user(email, last_name, password):
#     '''
#     Function to create a new user
#     '''
#     new_user = User(email, last_name, password)
#     return new_user

# def create_credentials(account,account_name,account_password):
#     '''
#     Function to create a new credential
#     '''
#     new_credentials = Credentials(account,account_name,account_password)
#     return new_credentials

# def save_user(user):
#     '''
#     Function to save users
#     '''
#     user.save_user(user)

# def save_credentials(credentials):
#     '''
#     Function to save credentials
#     '''
#     credentials.save_credentials()

# def del_user(user):
#     '''
#     Function to delete a credentials
#     '''
#     user.delete_user()

# def del_credentials(credentials):
#     '''
#     Function to delete a credentials
#     '''
#     credentials.delete_credentials()

# def find_credentials(account_name):
#     '''
#     Function that finds a credentials by number and returns the credentials
#     '''
#     return Credentials.find_by_account(account_name)

# def check_existing_credentials(account_name):
#     '''
#     Function that check if a credentials exists with that number and return a Boolean
#     '''
#     return Credentials.credentials_exist(account_name)

# def display_credentials():
#     '''
#     Function that returns all the saved credentialss
#     '''
#     return Credentials.display_credentials()

# def generate_password():
#     '''
#     This is a function to generate random password
#     '''
#     gen_pass = Credentials.generate_password()
#     return gen_pass

# def main():
#     print("Hello Welcome to Password. What is your name?")
#     u_name = input() 

#     print(f"Hello {u_name} welcome")

#     while True:
#         print("Use these short codes:\n [y] - Yes \n [n] - No")
#         status = input("Do you have a Password Locker account yet?")

#         if status == 'y':
#             print("WELCOME")
#             print("-"*60)
#             print(" To login , enter your account deails : ")
#             last_name = input("Enter your usename name : ")
#             password = getpass.getpass('Password: ')
#             user_exists = last_name

#             if user_exists == last_name :
#                 print(" ")
#                 print (f"Welcome back {last_name}. /n Please choose an option to continue")
#                 print(" ")

#         elif status == 'n':
#             print("Let Me Help you Create an account")
#             e_mail= input('Enter email: ')
#             u_name= input('Select Username: ')
#             key = getpass.getpass('Password: ')
#             key2 = getpass.getpass('Re-enter Password: ')
            
        
#             while key != key2:
#                 print("sorry your passwords do not match")
#                 print("Enter your password again")
#                 key = getpass.getpass('Password: ')
#                 key2 = getpass.getpass('Re-enter Password: ')

        
#             else:
#                 print(f"New Password Locker Account for {u_name} has been created")
#                 print(" You can now login to your account : ")
#                 new_user = input("Enter your usename name : ")
#                 new_password = getpass.getpass('Password: ')

                
#             while new_user !=  u_name or new_password != key2:
#                 print("you have entered a wrong username or password")
#                 print("Please enter your login information again....") 
#                 new_user = input("Enter usename: ")
#                 new_password = getpass.getpass('Password: ')          

#             else:
#                 print(f"Welcome {new_user} to your Password locker account. \n")  

#                 while True:
#                     print("Select an option below to continue:")
#                     print("")

#                     print("[a] View your saved accounts \n [b] Add a new account \n[c] Delete credentials \n [d] Find an account \n [e] Logout \n [cp] Copy information")
#                     option = input()
                    
#                     if option == 'e':
#                         print("bye....")
#                         break

#                     elif option == "c":
#                         while True:
#                             print("Type credential name you want to delete......")
#                             search_account = input()
#                             if check_existing_credentials(search_account):
#                                 search_credential = find_credentials(search_account)
#                                 print(f"Account :{search_credential.user_account}\n Password: {search_credential.account_password}")
#                                 print(f"are you sure you want to delete {search_credential.user_account} ? \n [y] \n [n]")
#                                 answer = input().lower()

#                                 if answer == 'y':
#                                     del_credentials(search_credential)
#                                     print("Account has been deleted sucessfully")
#                                     break
#                                 elif answer == 'n':
#                                     continue
#                                 else:
#                                     break

#                     elif option == "b":
#                         while True:

#                             print ("Enter Account Name")
#                             user_account = input()
#                             print("Enter your desired password")
#                             print("To use your own password use [o] \n Generate a random one use [g] ")
#                             keyword = input().lower()
#                             if keyword == "o" :
#                                 print("Create your own password : ")
#                                 account_password = input()
#                                 print(f" Account : {user_account}")
#                                 print(f" Password : {account_password}")
#                                 print(" ")

                            # elif keyword == "g":
                            #     account_password = generate_password()
                            #     print(f" Account : {user_account}")
                            #     print(f" Password : {account_password}")
                            #     print(" ")
                            # else:
                            #     print("please create a password")
                                # save_credentials( create_credentials(user_account,account_password))

                    #     break

                    # elif option == "a":
                    #     print("")
                    #     if display_credentials(): 
                    #         for credential in display_credentials():
                    #             print(f"Account Name : {credential.user_account}") 
                    #             print(f"Password : {credential.account_password}")
                    #     else:
                    #         print("")
                    #         print(" You don't have any credentials yet")
                    #         print("")

                    # elif option == "d":
                    #     while True:
                    #         print("Enter an account name to find credentials")
                    #         search_account = input()
                    #         if check_existing_credentials(search_account):
                    #                 search_account = find_credentials(search_account)
                    #                 print(f"{search_account.user_account} \n {search_account.account_password}")
                    #                 print('-'*10)
                    #         else:
                    #                 print("The credential doesn't exist")
                    #                 break
                   
                    # elif option == "cp":
                    #     print("")
                    #     this_account = input("Enter Account name for password to copy: ")
                    #     copy_credential(this_account)
                    #     print("")

        
# if __name__ == '__main__':

#     main()