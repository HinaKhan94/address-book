import gspread
import re
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Address Manager')


class Color:
    # ANSI codes for text color
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    PURPLE = '\033[95m'
    BLUE = '\033[34m'


def update_contact(address_list):
    '''
    The user is asked for entering first,
    last or full-name of the contact they want to update
    the program shows a list of matching contacts
    from which the user can select the one they want to update
    the selected option is then displayed with questions
    to update the currect information the contact_number has
    certain data validation and will throw an error if user types incorrectly

    '''
    print(Color.GREEN +
          """\nUpdating a contact...\n"""
          + Color.RESET)
    while True:
        search_name = input(
            '\nEnter the name to update:\n').lower()
        matching_contacts = find_duplicate_contacts(
            search_name, address_list
            )
        if not matching_contacts:
            print(Color.RED +
                  """\nContact not Found!\n"""
                  + Color.RESET)
        else:
            print(Color.GREEN + """\nContacts found:\n""" + Color.RESET)
            number = 0
            for i, contact in matching_contacts:
                number += 1
                print(Color.PURPLE + f"\n{number}. Name: {contact[0]}," +
                      f" Contact: {contact[1]}, Address: {contact[2]}" +
                      Color.RESET + "\n")
            while True:
                user_choice = input(
                    '\nSelect the number to update or "q" to quit!\n')
                print(f"Debug: user_choice = '{user_choice}'")
                if user_choice.lower() == 'q':
                    print("Exiting loop.")
                    break
                try:
                    user_choice_index = int(user_choice) - 1
                    if (user_choice_index >= 0 and
                       user_choice_index < len(matching_contacts)):
                        contact_index, selected_contact = matching_contacts[
                            user_choice_index]
                        print(Color.PURPLE +
                              f"\nYou selected {selected_contact}\n"
                              + Color.RESET)
                        break  # breaks the loop once valid selection is made
                    else:
                        print(Color.RED + """\nInvalid input.""" +
                              """Please enter a valid number or """ +
                              """'q' to quit.\n"""
                              + Color.RESET)
                except ValueError:
                    print(Color.RED + """\nInvalid input.""" +
                          """Please enter a valid number or 'q' to quit.\n"""
                          + Color.RESET)
            # Prompts the user for the updated information
            while True:
                new_name = (input("""\nEnter the updated full name """ +
                            """(press Enter to keep the same): """ + '\n')
                            .lower()
                            .strip())
                if not new_name:
                    # use the existing name if the input is empty
                    new_name = contact[0]
                if re.match(r'^[A-Za-z ]+$', new_name):
                    break
                else:
                    print(Color.RED + """\nInvalid input.Please enter a """ +
                          """ valid name with only letters and spaces.\n"""
                          + Color.RESET)
            print(Color.BLUE +
                  """\nName is being updated....\n"""
                  + Color.RESET)
            print(Color.BLUE +
                  """\nName is updated....\n"""
                  + Color.RESET)
            while True:
                new_contact = input("""\nEnter the updated contact number """ +
                                    """(press Enter to keep the same): \n""")
                if not new_contact:
                    # Use the existing contact number if the input is empty
                    new_contact = contact[1]
                    # validate the new number provided
                new_contact = ''.join(
                    filter(lambda char: char.isdigit() or char == '+',
                           new_contact))
                if not new_contact or \
                   (new_contact.startswith("+49") and len(new_contact) == 14):
                    break  # exits the loop if the input is invalid or empty
                else:
                    print(Color.RED + """\nINVALID: The phone number must """ +
                          """ start with +49 and must have 11 digits\n"""
                          + Color.RESET)
                # checks if the phone number is a duplicate
                if is_duplicate_phone_number(new_contact, address_list):
                    print(Color.RED + """\nINVALID: This number is """ +
                          """ already assigned to another contact\n"""
                          + Color.RESET)
            print(Color.BLUE +
                  """\nContact number is being updated....\n"""
                  + Color.RESET)
            print(Color.BLUE +
                  """\nContact number is updated....\n"""
                  + Color.RESET)
            new_address = (input("""\nEnter the updated address """ +
                                 """(press Enter to keep the same): \n""")
                           .lower())
            print(Color.BLUE +
                  """\nAddress is being updated....\n"""
                  + Color.RESET)
            print(Color.BLUE +
                  """\nAddress is updated....\n"""
                  + Color.RESET)
            # Updates the contact information
            if new_name:
                selected_contact[0] = new_name
            if new_contact:
                selected_contact[1] = new_contact
            if new_address:
                selected_contact[2] = new_address
            address_list[contact_index] = selected_contact
            print(Color.GREEN + "\nContact updated.\n" + Color.RESET)
            print(Color.GREEN + f"\nContact Updated:" +
                  f"Name: {selected_contact[0]}," +
                  f"Contact: {selected_contact[1]}," +
                  f"Address: {selected_contact[2]}\n"
                  + Color.RESET)
            break


def find_duplicate_contacts(full_name, address_list):
    '''
    When the find_duplicate_contacts function is called,
    it iterates through the address_list, which is
    a list of contacts. For each contact in the list,
    it checks if the full_name (the name the user entered) is
    found within the contact's full name (which may include
    both first and last names). If a match is found, the function
    creates a tuple containing two values: index number at which
    the ocntact is located and the contact info itself

    '''
    matching_contacts = []
    for index, contact in enumerate(address_list):
        names = contact[0]
        if any(full_name in names for name in names):
            matching_contacts.append((index, contact))
    return matching_contacts


def is_duplicate_phone_number(phone_number, address_list):
    '''
    Function to check if a phone number is already
    assigned to another contact and not a duplicate.
    If it is, it will throw an error to the user
    '''
    for contact in address_list:
        if phone_number == contact[1]:
            return True
    return False


def delete_contact(address_list):
    '''
    the delete function allows the user to find the
    contact by typing in the first, last or the full name
    of the contact it wants to delete. Once the contact is selected,
    it will ask her to confirm the deletion
    when pressed Yes in the confirmation message, the contact
    gets deleted and is also updated in the address_lis
    when pressed No in the confirmation message,
    the user is taken back to the main menu

    '''
    while True:
        print(Color.GREEN +
              """\nDeleting a contact...\n"""
              + Color.RESET)
        contact_to_delete = (input("""\nEnter the name of the """ +
                                   """ contact you want to delete: \n """)
                             .lower())
        matching_contacts = find_duplicate_contacts(
            contact_to_delete, address_list)
        confirm_delete = ""
        if not matching_contacts:
            print(Color.RED + "\nContact not Found!\n"
                  + Color.RESET)
            break
        else:
            print(Color.GREEN + "\nContacts found:\n"
                  + Color.RESET)
            number = 0
            for i, contact in matching_contacts:
                number += 1
                print(Color.PURPLE + f"\n{number}. Name: {contact[0]}," +
                      f"Contact: {contact[1]}, Address: {contact[2]}" +
                      Color.RESET + "\n")
            user_choice = input("""\nSelect the number you would """ +
                                """like to delete or "q" to quit!\n""")
            if user_choice.lower() == 'q':
                break
            try:
                user_choice_index = int(user_choice) - 1
                if (user_choice_index >= 0 and
                   user_choice_index < len(matching_contacts)):
                    contact_index, selected_contact = matching_contacts[
                        user_choice_index]
                    print(Color.PURPLE + f"\nYou selected" +
                          f"{selected_contact}\n" +
                          Color.RESET)
                    confirm_delete = input(f"\nDo you want to delete " +
                                           f"{selected_contact}\nYes/No?\n")
                    if confirm_delete.lower() == ("yes"):
                        address_list.remove(selected_contact)
                        contact_deleted = True
                        print(Color.GREEN +
                              """\nContact deleted!\n""" + Color.RESET)
                        break   # exits the loop after the contact is deleted
                    else:
                        print(Color.GREEN + '\nContact not deleted!\n'
                              + Color.RESET)
                        break   # exits the loop after processing the contact
                else:
                    print(Color.RED + """\nInvalid: Please enter """ +
                          """a valid number or 'q' to quit.\n"""
                          + Color.RESET)
            except ValueError:
                print(Color.RED + """\nInvalid input. Please enter """ +
                      """a valid number or 'q' to quit.\n"""
                      + Color.RESET)


def update_google_sheet(sheet, data):
    '''
    it updates data whenever a user adds,
    updates and deletes a contact

    '''
    worksheet = SHEET.worksheet('alldata')
    worksheet.clear()
    worksheet.insert_rows(data)


def get_data_from_googlesheet(sheet):
    '''
    this function gets the data from the sheet
    named 'alldata' in the google sheets
    and displays the data in the main program function
    at the start so that user can views all
    contacts present in the list

    '''
    worksheet = sheet.worksheet('alldata')
    data = worksheet.get_all_values()
    return data


def main():
    '''
    To make sure the application runs even
    if the file is deleted somehow the except argument
    will throw an error and terminates the program. The user is
    displayed with 5 options to choose from as the main menu of the program.
    It also contains some data validations and if user's input
    does not meet the validation, it will throw validation errors.

    '''
    try:
        # taking existing data from the sheet
        address_list = get_data_from_googlesheet(SHEET)
    except FileNotFoundError:
        print('The address list is unavailable')
        print('Starting a new list of address!')
        address_list = []

    choice = 0
    run_program = True
    while run_program:
        print('******* Welcome to Address Manager *******' '\n')
        print('** Add, Find, Update, Delete and View contacts **' '\n')
        print(Color.GREEN + """Choose one option from the options below:  """
              '\n' + Color.RESET)
        print('1) Add a contact')
        print('2) Look up a contact')
        print('3) Update a contact')
        print('4) Delete a contact')
        print('5) Display all contacts')
        try:
            choice = int(input('\nWhat would you like to do?  \n'))
        except ValueError:
            print((Color.RED +
                  """\nInvalid input: Please enter a valid number(1-5)\n"""
                   + Color.RESET))
            continue
        if choice < 1 or choice > 5:
            print(Color.RED +
                  """\nInvalid choice: Please select number between(1-5)\n"""
                  + Color.RESET)
        if choice == 1:
            # adding a contact
            while True:
                print(Color.GREEN + """\nAdding a contact...\n"""
                      + Color.RESET)
                while True:
                    full_name = input("""\nEnter the full name with only""" +
                                      """ letters and a space in between """ +
                                      """ the first and last name: \n""")
                    # only letters and space
                    if re.match(r'^[A-Za-z ]+$', full_name):
                        break
                    else:
                        print(Color.RED + """\nInvalid input: Please enter""" +
                              """ a valid name with only letters""" +
                              """ and spaces.\n"""
                              + Color.RESET)
                # Check if the user provided a full name with a space
                if full_name and ' ' in full_name:
                    break
                else:
                    print(Color.RED + """INVALID: Please enter full name""" +
                          """ with a space between first and last names."""
                          + Color.RESET)
            while True:
                contact_number = input("""\nEnter the contact number """ +
                                       """(starting with +49 and have 11 """ +
                                       """digits)Example(+4912345678912):\n""")
                # Remove any spaces or non-digit characters from the input
                contact_number = ''.join(
                    filter(lambda char: char.isdigit() or char == '+',
                           contact_number))
                # Validate that the phone number starts with
                # '+49' and a length of 11 digits for Germany
                if (contact_number.startswith("+49") and
                   len(contact_number) == 14):
                    # checks if the phone number is a duplicate
                    if is_duplicate_phone_number(contact_number, address_list):
                        print(Color.RED + """\nINVALID:This number is""" +
                              """ already assigned to another contact\n"""
                              + Color.RESET)
                    else:
                        # If the input passes validation,
                        # proceed to add the contact
                        address = input("\nEnter the address:   \n").lower()
                        address_list.append([
                            full_name,
                            contact_number,
                            address
                            ])
                        print(Color.GREEN + """\nContact added...\n"""
                              + Color.RESET)
                        # displays the newly added contact immediately
                        print(Color.PURPLE + f"\nNew contact added:" +
                              f"Name: {full_name}," +
                              f"Contact: {contact_number}," +
                              f"Address: {address}\n" + Color.RESET)
                        # Call update_google_sheet
                        update_google_sheet(SHEET, address_list)
                        break
                else:
                    print(Color.RED + """\nINVALID:The phone number must""" +
                          """ start with +49 and must have 11 digits\n"""
                          + Color.RESET)
        elif choice == 2:
            # looking for a contact
            print(Color.GREEN + """\nLooking up for a contact...\n"""
                  + Color.RESET)
            while True:
                full_name = (input('\nEnter the name of the person:  \n')
                             .lower())
                matching_contacts = find_duplicate_contacts(
                        full_name, address_list)
                if not matching_contacts:
                    print(Color.RED + "\nContact not Found!\n"
                          + Color.RESET)
                else:
                    print(Color.GREEN + "\nContacts found:\n"
                          + Color.RESET)
                    number = 0
                    for i, contact in matching_contacts:
                        number += 1
                        print(Color.PURPLE + f"\n{number}." +
                              f"Name: {contact[0]}," +
                              f"Contact: {contact[1]}," +
                              f"Address: {contact[2]}" +
                              Color.RESET + '\n')
                    another_search = input(Color.GREEN + """\nDo you want""" +
                                           """ to look for another""" +
                                           """ contact? (Yes/No:)\n"""
                                           + Color.RESET)
                    if another_search.lower() == 'no':
                        break  # exits the loop
        elif choice == 3:
            # updating a contact and calling the update function
            update_contact(address_list)
            update_google_sheet(SHEET, address_list)
        elif choice == 4:
            # deleting a contact and calling the delete function
            delete_contact(address_list)
            update_google_sheet(SHEET, address_list)
        elif choice == 5:
            print(Color.GREEN + "\nDisplaying all contacts...\n"
                  + Color.RESET)
            all_contacts = get_data_from_googlesheet(SHEET)
            number = 0
            for contact in all_contacts:
                if contact[1].strip() and contact[1] != 'Contact_number':
                    number += 1
                    print(Color.PURPLE + f"\n{number} Name: {contact[0]}," +
                          f"Contact: {contact[1]}, Address: {contact[2]}\n"
                          + Color.RESET)


if __name__ == '__main__':
    main()
