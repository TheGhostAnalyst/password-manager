from datetime import datetime
import pyinputplus as Pyip
from pathlib import Path
import re


def write(password):
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M")
    with open('password_manager.txt', 'a') as f:
        contents = f.write(f"{timestamp}\n{password}\n")
        print(f"Password saved in: {Path('password_manager.txt').resolve()}")

def display_passwords():
    file_path = Path('password_manager.txt')
    if file_path.exists():
        with open(file_path, 'r') as f:
            contents = f.read()
            print(f"{contents}\n")
    else:
        print("No saved passwords found.")

def search_by_app(app_name):
    file_path = Path('password_manager.txt')
    if not file_path.exists():
        print("No saved passwords found.")
        return

    with open(file_path, 'r') as f:
        contents = f.read()
        matches = re.findall(rf"Website/App:\s*{app_name}.*?##############################", contents, re.DOTALL | re.IGNORECASE)
        if matches:
            for match in matches:
                print(match)
        else:
            print(f"No saved passwords found for '{app_name}'.")



while True:
    try:
        print('\nPassword manager tool by The Ghost Analyst')
        first = Pyip.inputNum("""Which of these operations would you like to perform:
        1. Save a new password
        2. Check saved passwords
        3. Find likely websites you stored passwords for 
        4. Exit                      
        >>>>>> """)
        if first == 1:
            print('Save a new password')
            app_name = input('Enter the website or app you want to save password for: ')
            contact = input('Enter your phone number, email or username: ')
            password = input('Enter your password for the app or website you want to save: ')
            content = (f"Website/App: {app_name}\nUsername/Num/Email: {contact}\nPassword: {password}\n##############################\n")
            write(content)

        elif first == 2:
            print('Getting saved passwords from database\n')
            display_passwords()
        elif first == 3:
            search_web = input('What app or website do you want to search for: ')
            search_by_app(search_web)
        elif first == 4:
            print('Preparing a smooth exit........')
            break
    except KeyboardInterrupt:
        print("Exit successful")
        break
    
    

    
