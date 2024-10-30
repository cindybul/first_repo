#-------------------------------------------------------------------#
#  MenuDigicore.py                                                  #
#                                                                   #
#  Programmed and designed by Cindy Jayakumar                       #
#  Date Created 27 October 2024                                     #
#  Date Ended 28 October 2024                                       #
#                                                                   #
#  The script creates menu for record user credintials              #
#                                                                   #
#-------------------------------------------------------------------#

#colourful output
from colorama import Fore, Style, init
init(autoreset=True)

# import cipher module for encryption and decryption function
import cipher as cip               #from cipher import encrypted_value, decrypted_value           ####(another example import option)####

# import validation module for invalid input
from validation import get_valid_credentials


def menu():
    print('')
    print(Fore.YELLOW + '========================== Main Menu DigiCore =========================')
    print(Fore.YELLOW +'|                                                                      |')
    print(Fore.YELLOW +'|                          1. Add User Credentials                     |')
    print(Fore.YELLOW +'|                          2. View Credentials                         |')
    print(Fore.YELLOW +'|                          3. Exit                                     |')
    print(Fore.YELLOW +'|                                                                      |')
    print(Fore.YELLOW +'========================================================================')


 # Keep prompting until valid input is received
    while True:  
        option = input(Fore.CYAN + "Select the option (1-3) : ").strip()
        if option.isdigit() and int(option) in [1, 2, 3]:
            return int(option)
        else:
            print(Fore.RED + "Please input a valid option between 1, 2, or 3.")



# for adding user credentials function
def add_user():
        name, password = get_valid_credentials()
        encrypted_pass = cip.encrypted_value(password, shift = 3) # It encrypts the password using a Caesar cipher, which shifts each character by 3 positions in a defined character set.
        url = input('Input URL/Resources : ') # Prompts the user to input a URL
        return name, encrypted_pass, url #Returns the collected information as a tuple containing the name, encrypted_pass, and url

selected_opt = menu()


while selected_opt != 3:
    if selected_opt == 1:
         print('')
         print(Fore.YELLOW + '_________________________ Add User Menu ______________________')

         #add user credentials
         name, encrypted_pass, url = add_user()
         with open('digicore.txt', 'a') as file:  # create text file & Append new data input
            file.write(f'{name},{encrypted_pass},{url}\n') # insert data 
            print(Fore.GREEN + ">>>> Congratulation, Your data have been saved <<<<")
    
    elif selected_opt == 2:
        print('')
        print(Fore.YELLOW + '________________________ View Stored Credentials ______________________')
        print(f'{'Name':<15} | {'Password':<20} | {'URL':<30}')
        print('-' * 65)

        #view user credentials
        with open('digicore.txt', 'r') as file:  #read the file in text file
            for line in file:
                    name,encrypted_password,url = line.strip().split(',') #This code line reads a single line from the file, removes any extra spaces or newlines, splits the line into three parts based on commas,
                    decrypted = cip.decrypted_value(encrypted_password)
                    print(f'{name:<15} | {decrypted:<20} | {url:<30}')


    selected_opt = menu()

print(Fore.YELLOW + '             ******* Goodbye! *******                ')