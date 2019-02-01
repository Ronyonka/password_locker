#!/usr/bin/env python3.6
import pyperclip
from user import User
from credentials import Credentials
import getpass

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




def main():

    print(" Hello, what is your name?")
    first_name = input()

    print(f"Hello {first_name} welcome to Password Locker. What would you like to do today?\n")
   

    while True:  
        print("Please use the following short codes :\n [c] - Create new account  ,\n [l] - Log in ,\n [e] -  Exit password locker") 
        short_code = input().lower()


        if short_code == "c":
            print ("-"*15)
            print ("\n")
            print ("To create a new user account: ")
            first_name = input(" Enter First name:-  ")
            last_name = input("Select Username :-  ")
            password = getpass.getpass (" Select password: ")
            confirm_password = getpass.getpass ("Confirm password:")
            save_user(create_user(first_name,last_name,password))
            print("")
            print(f" New account has been created for : {first_name} \n with username :{last_name} \n using password: {password}")
            print("\n")

            while confirm_password != password :
                print("sorry your passwords do not match")
                print("Enter your password again")
                password = getpass.getpass (" Please enter your desired password:")
                confirm_password =getpass.getpass ("Please confirm your password:")

            else:
                print(f" Congratulations {last_name}! You have created your account.")
                print("\n")
                print(" You can now login to your Password Locker account")
                new_last_name = input("Username: ") 
                new_password = getpass.getpass("Password:")
                save_user(create_user(first_name,last_name,password))
                print("")
                print(f"New account has been created for : {first_name} \n with username :{last_name} ")
                
            while new_last_name !=  last_name or new_password != password:
                print("Oops! You seem to have entered a wrong username or password")
                print("Please re-enter your login information.")
                new_last_name = input("Please enter your username :-  ") 
                new_password = getpass.getpass("Please enter your password:- ")
            else:
                print(f"Welcome {new_last_name} to your Credential Account")
                print("\n")

            while True:
                print("Select an option to continue:")
                print("")
                print("[a]Add a new account")
                print("[b] View your saved account")
                print("[c] Delete Credentials")
                print("[d] Find an account")
                print("[e] Logout")
                print("[cp] Copy account info")
                
                option = input()
                if option == 'e':
                    print("Byeeeeee")
                    break
                elif option == "a":
                    
                    while True:
                        print("Do you want to add an account? [y] \n [n]")

                    choice = input().lower()
                    if choice == "y":
                        print ("Enter Account Name")
                        user_account = input()
                        print("Enter your desired password")
                        print("To use your own password use [o] or Generate a random one use [g] ")
                        keyword = input().lower()
                        if keyword == "o" :
                            print("Create your own password : ")
                            account_password = input()
                            print(f" Account : {user_account}")
                            print(f" Password : {account_password}")
                            print(" ")

                        elif keyword == "g":
                            account_password = generate_password()
                            print(f" Account : {user_account}")
                            print(f" Password : {account_password}")
                            print(" ")
                        else:
                            print("please create a password")
                            save_new_credentials(create_new_credential(user_account,account_password))
                    elif choice == "n":
                        print("Bye .....")
                        break
                elif option == "b":
                    print("")
                    if display_credential(): 
                        for credential in display_credential():
                            print(f"Account Name : {credential.user_account}") 
                            print(f"Password : {credential.account_password}")
                    else:
                        print("")
                        print(f"Sorry we can't find any credentials for {last_name}")
                        print("")
                elif option == "d":
                    while True:
                        print("Enter an account name to find credentials")
                        search_account = input()
                        if check_existing_credentials(search_account):
                                search_account = find_credentials(search_account)
                                print(f"{search_account.user_account} \n {search_account.account_password}")
                                print('-'*10)
                        else:
                                print("The credential doesn't exist")
                                break
                elif option == "cp":
                    print("")
                    this_account = input("Enter Account name for password to copy: ")
                    copy_credential(this_account)
                    print("")
                


        elif short_code == "l":
                print("WELCOME")
                print("-"*60)
                print(" To login , enter your account deails : ")
                last_name = input("Enter your usename :- ")
                password = getpass.getpass("Enter your password :- ")
                user_exists = verify_user(last_name)

                if user_exists == last_name :
                    print(" ")
                    print (f"Welcome back {last_name} . \n Please choose an option to continue")
                    print(" ")

                while True:
                    print("Select an option to continue:")
                    print("")
                    print("[a]Add a new account")
                    print("[b] View your saved account")
                    print("[c] Delete Credentials")
                    print("[d] Find an account")
                    print("[e] Logout")
                    
                    option = input()
                    if option == 'e':
                        print("Byeeeeee")
                        break
                    elif option == "a":
                        while True:
                            print("Do you want to add an account? [y] \n [n]")

                        choice = input().lower()
                        if choice == "y":
                            print ("Enter Account Name")
                            user_account = input()
                            print("Enter your desired password")
                            print("To use your own password use [o] or Generate a random one use [g] ")
                            keyword = input().lower()
                            if keyword == "o" :
                                print("Create your own password : ")
                                account_password = input()
                                print(f" Account : {user_account}")
                                print(f" Password : {account_password}")
                                print(" ")

                            elif keyword == "g":
                                account_password = generate_password()
                                print(f" Account : {user_account}")
                                print(f" Password : {account_password}")
                                print(" ")
                            else:
                                print("please create a password")
                                save_new_credentials(create_new_credential(user_account,account_password))
                        elif choice == "n":
                            print("Bye .....")
                            break
                    elif option == "b":
                        print("")
                        if display_credential(): 
                            for credential in display_credential():
                                print(f"Account Name : {credential.user_account}") 
                                print(f"Password : {credential.account_password}")
                        else:
                            print("")
                            print(f"Sorry we can't find any credentials for {last_name}")
                            print("")
                    elif option == "d":
                        while True:
                            print("Enter an account name to find credentials")
                            search_account = input()
                            if check_existing_credentials(search_account):
                                    search_account = find_credentials(search_account)
                                    print(f"{search_account.user_account} \n {search_account.account_password}")
                                    print('-'*10)
                            else:
                                    print("The credential doesn't exist")
                                    break
        elif short_code == "e":
            print("Bye....we hope you again visit soon")
            break
    if __name__ == '__main__':
        main()






