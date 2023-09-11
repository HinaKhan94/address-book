import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('address_manager')


class Color:
    #ANSI codes for text color
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    PURPLE = '\033[95m'


def update_contact(address_list):
    '''
    The user is asked for entering first, last or full-name of the contact they want to update
    the program shows a list of matching contacts from which the user can select the one they want to update
    the selected option is then displayed with questions to update the currect information
    the contact_number has certain data validation and will throw an error if user types incorrectly

    '''
   
    print(Color.GREEN + 'Updating a contact...' + Color.RESET)
    while True:
        search_name = input('Enter the full name of the contact (with a space between first and last name) you want to update: ').lower()
        matching_contacts = find_duplicate_contacts(search_name, address_list)

        if not matching_contacts:
            print(Color.RED + "Contact not Found!" + Color.RESET)
        else:
            print(Color.GREEN + "Contacts found:" + Color.RESET)
            for i, contact in matching_contacts:
                print(Color.PURPLE + f"{i + 1}. Name: {contact[0]}, Contact: {contact[1]}, Address: {contact[2] + Color.RESET}")
            
            user_choice = input('Select which contact you would like to update or "q" to quit!')
            if user_choice.lower() == 'q':
                break
          
            try:
                user_choice_index = int(user_choice) - 1 #
                if user_choice_index >= 0 and user_choice_index < len(matching_contacts):
                    
                    contact_index, selected_contact = matching_contacts[user_choice_index]
                    print('you selected',matching_contacts[user_choice_index])
            except ValueError:
                print(Color.RED + "Invalid input. Please enter a valid number or 'q' to quit." + Color.RESET)

            # Prompts the user for the updated information
           
            new_name = input("Enter the updated full name (press Enter to keep the same): ").lower().strip()
            while True:
                new_contact = input("Enter the updated contact number (press Enter to keep the same): ")
                if not new_contact:
                    new_contact = contact[1]  # Use the existing contact number if the input is empty
                #validate the new number provided    
                new_contact = ''.join(filter(lambda char: char.isdigit() or char == '+', new_contact))
                if not new_contact or (new_contact.startswith("+49")) and len(new_contact) == 14:
                    break #exits the loop if the input is invalid or empty
                else:
                    print(Color.RED + "INVALID: The phone number must start with +49 and must have 11 digits" + Color.RESET)
    
                # checks if the phone number is a duplicate
                if is_duplicate_phone_number(new_contact, address_list):
                    print(Color.RED + 'INVALID: this number is already assigned to another contact' + Color.RESET)
                    
            new_address = input("Enter the updated address (press Enter to keep the same): ").lower()   
            
            # Updates the contact information
            
            if new_name:
                selected_contact[0] = new_name
            if new_contact:
                selected_contact[1] = new_contact
            if new_address:
                selected_contact[2] = new_address

            address_list[contact_index] = selected_contact

            print(Color.GREEN + "Contact updated." + Color.RESET)
            print(Color.GREEN + f"New contact added: Name: {selected_contact[0]}, Contact: {selected_contact[1]}, Address: {selected_contact[2]}" + Color.RESET)
            break

def find_duplicate_contacts(full_name, address_list):
    '''
    When the find_duplicate_contacts function is called, it iterates through the address_list, which is a list of contacts.
    For each contact in the list, it checks if the full_name (the name the user entered) is found within the contact's full name (which may include both first and last names).
    If a match is found, the function creates a tuple containing two values: index number at which the ocntact is located and the contact info itself

    '''
    matching_contacts = []
    number = 0
    for index, contact in enumerate(address_list):
        names = contact[0].split() #splitting the full name of a contact (which is stored in contact[0]) into a list of individual words
        if any(full_name in names for name in names):
            print(number, contact)
            matching_contacts.append((number,contact))
            number += 1
    
    return matching_contacts

def is_duplicate_phone_number(phone_number, address_list):
    '''
    Function to check if a phone number is already assigned to another contact 
    and not a duplicate. If it is, it will throw an error to the user 
    '''
    
    for contact in address_list:
        if phone_number == contact[1]:
            return True
    return False

def delete_contact(address_list):
    '''
    the delete function allows the user to find the contact by typing in the first, last or the full name 
    of the contact it wants to delete. Once the contact is selected, it will ask her to confirm the deletion
    when pressed Yes in the confirmation message, the contact gets deleted and is also updated in the address_list
    when pressed No in the confirmation message, the user is taken back to the main menu 

    '''

    print(Color.GREEN + 'Deleting a contact...' + Color.RESET)
    contact_to_delete = input('Enter the full name of the contact you want to delete: ').strip().lower()

    contact_deleted = False
    for people in address_list:
        if contact_to_delete == people[0]:
            confirm_delete= input(f"Do you want to delete {people}\nYes/No? \n")
            if confirm_delete.lower() == ("yes"):
                address_list.remove(people)
                contact_deleted = True
                print(Color.GREEN + 'Contact deleted!' + Color.RESET)
                break #exits the loop after the contact is deleted
            else: 
                print(Color.GREEN + 'Contact not deleted!' + Color.RESET)
                break #exits the loop after processing the contact

    if not contact_deleted and confirm_delete.lower() == ("yes"): 
        print(Color.RED + 'Contact not found!' + Color.RESET)

def update_google_sheet(sheet,data):
    # it updates data whenever a user adds, updates and deletes a contact
    worksheet = SHEET.worksheet('alldata')
    worksheet.clear()
    worksheet.insert_rows(data)  

def get_data_from_googlesheet(sheet):
    '''
    this function gets the data from the sheet named 'alldata' in the google sheets
    and displays the data in the main program function at the start so that user can views
    all contacts present in the list

    '''

    worksheet = sheet.worksheet('alldata')
    data = worksheet.get_all_values()
    return data


def main():
    '''
    To make sure the application runs even if the file is deleted somehow
    the except argument will throw an error and terminates the program
    The user is displayed with 6 options to choose from as the main menu of the program
    It also contains some data validations and if user's input does not meet the validation, it will throw validation errors

    '''
   
    try:
        #taking existing data from the sheet
        address_list = get_data_from_googlesheet(SHEET)
        

    except FileNotFoundError :
        print('The address list is unavailable')
        print('Starting a new list of address!')
        address_list = []



    choice = 0
    while choice !=6:
        print('********** Welcome to Address Manager ***********' '\n' '** Add, Find, Update, Delete and View contacts **' '\n')
        print(Color.GREEN + 'Choose one option from the options below:  ' '\n' + Color.RESET)
        print('1) Add a contact')
        print('2) Look up a contact')
        print('3) Update a contact')
        print('4) Delete a contact')
        print('5) Display all contacts')
        print('6) Quit', '\n')
        choice = int(input('What would you like to do?   '))

        if choice == 1:
            #adding a contact
            while True:
                print(Color.GREEN + 'Adding a contact...' + Color.RESET)
                full_name = input("Enter the contact's full name with a space between first and last names:   ").lower().strip()
            
             # Check if the user provided a full name with a space
                if full_name and ' ' in full_name:
                    break
                else:
                    print(Color.RED + "INVALID: Please enter full name with a space between first and last names." + Color.RESET)
            
            
            while True:
                contact_number = input("Enter the contact number (starting with +49 and have 11 digits)\n Example:+4912345678912:   ")
                # Remove any spaces or non-digit characters from the input
                contact_number = ''.join(filter(lambda char: char.isdigit() or char == '+', contact_number))

                 # Validate that the phone number starts with '+49' and a length of 11 digits for Germany
                if contact_number.startswith("+49") and len(contact_number) == 14:
                
                    # checks if the phone number is a duplicate
                    if is_duplicate_phone_number(contact_number, address_list):
                        print(Color.RED + 'INVALID: this number is already assigned to another contact' + Color.RESET)
                
                    else:
                        # If the input passes validation, proceed to add the contact
                        address = input("Enter the address:   ").lower()
                        address_list.append([full_name, contact_number, address])
                        print(Color.GREEN + 'Contact added...' + Color.RESET)
                        
                        # displays the newly added contact immediately
                        print(Color.PURPLE + f"New contact added: Name: {full_name}, Contact: {contact_number}, Address: {address}" + Color.RESET)
                        update_google_sheet(SHEET, address_list) # Call update_google_sheet after collecting all new contacts
                        break
                    
                else:
                    print(Color.RED + "INVALID: The phone number must start with +49 and must have 11 digits" + Color.RESET)
                
            
                


        elif choice == 2:
            #looking for a contact
                print(Color.GREEN + 'Looking up for a contact...' + Color.RESET)  
                while True:  
                    full_name = input('Enter the full name (with a space between first and last name):  ').lower()
                    # checking for the valid format
               
                    if ' ' not in full_name:
                        print(Color.RED + "INVALID: please make sure you have enetered the full name and there is space between first and last name" + Color.RESET)
                    else:
                        contact_found = False 
                        for contacts in address_list:
                            if full_name == contacts[0]:
                                print(Color.GREEN + "Contact found:" + Color.RESET)
                                print(f"Name: {contacts[0]}, Contact: {contacts[1]}, Address: {contacts[2]}")
                                contact_found = True
                                break
                        if not contact_found:
                            print(Color.RED + "Contact not found!" + Color.RESET)        
                
                    another_search = input(Color.GREEN + "Do you want to look for another contact? (Yes/No:)" '\n' + Color.RESET)
                    if another_search.lower() == 'no':
                        break # exits the loop

        elif choice == 3:
            #updating a contact and calling the update function
            update_contact(address_list)
            update_google_sheet(SHEET, address_list)
        
        elif choice == 4:
            #deleting a contact and calling the delete function
            delete_contact(address_list)
            update_google_sheet(SHEET, address_list)
        
        elif choice == 5:
            print(Color.GREEN + 'Displaying all the contacts...')
            all_contacts = get_data_from_googlesheet(SHEET)
            number = 0
            for contact in all_contacts:
                if contact[1].strip() and contact[1] != 'contact_number':
                    number +=1
                    print(f"{number} Name: {contact[0]}, Contact: {contact[1]}, Address: {contact[2]}")
                

    else:
        print(Color.GREEN + 'Terminating program...' + Color.RESET)   

      
    

if __name__ == '__main__':
    main()

