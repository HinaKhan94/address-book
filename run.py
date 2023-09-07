#ANSI codes for text color
class Color:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'


def update_contact(addressList):
    # the update_contact function
    print(Color.GREEN + 'Updating a contact...' + Color.RESET)
    term = input('Enter the full name of the contact (with a space between first and last name) you want to update: ').lower()

    # Check if the input contains a space
    if ' ' not in term:
        print(Color.RED + "INVALID: You must enter the full name (with a space between first and last name." + Color.RESET)
        return

    contact_found = False
    for contacts in addressList:
        if term == contacts[0]:
            print(Color.GREEN + "Contact found:" + Color.RESET)
            print(f"Name: {contacts[0]}, Contact: {contacts[1]}, Address: {contacts[2]}")
            contact_found = True

            # Prompts the user for the updated information
            new_name = input("Enter the updated full name (press Enter to keep the same): ")
            new_contact = input("Enter the updated contact number (press Enter to keep the same): ")
            new_address = input("Enter the updated address (press Enter to keep the same): ")

            # Updates the contact information
            if new_name:
                contacts[0] = new_name
            if new_contact:
                contacts[1] = new_contact
            if new_address:
                contacts[2] = new_address

            print(Color.GREEN + "Contact updated." + Color.RESET)
            print(Color.GREEN + f"New contact added: Name: {contacts[0]}, Contact: {contacts[1]}, Address: {contacts[2]}" + Color.RESET)
            break

    if not contact_found:
        print(Color.RED + "Contact not found." + Color.RESET)

# Function to check if a phone number is already assigned to another contact and not a duplicate
def is_duplicate_phone_number(phone_number, addressList):
    for contact in addressList:
        if phone_number == contact[1]:
            return True
    return False


# main function that runs all the options displayed to the user
def main():
    # To make sure the application runs even if the txt file is deleted somehow
    # the except argument will throw an error and start making a new file 
    try:
        #creating an address list
        addressList = []
        infile = open('theaddresslist.txt', 'r') # 'r' is for reading the file in the second argument
        row = infile.readline()

        # starring a loop to append and read rows over and over again
        while row:
            addressList.append(row.rstrip("\n").split(','))
            row = infile.readline()
        infile.close()

    except FileNotFoundError :
        print('The address list is unavailable')
        print('Starting a new list of address!')
        addressList = []



    choice = 0
    while choice !=5:
        print('********** Welcome to Address Manager ***********' '\n' '** Add, Find, Update, Delete and View contacts **' '\n')
        print(Color.GREEN + 'Choose one option from the options below:  ' '\n' + Color.RESET)
        print('1) Add a contact')
        print('2) Look up a contact')
        print('3) Update or Delete a contact')
        print('4) Display all contacts')
        print('5) Quit', '\n')
        choice = int(input('What would you like to do?   '))

        if choice == 1:
            while True:
                print(Color.GREEN + 'Adding a contact...' + Color.RESET)
                full_name = input("Enter the contact's full name with a space between first and last names:   ").lower().strip()
            
             # Check if the user provided a full name with a space
                if full_name and ' ' in full_name:
                    break
                else:
                    print(Color.RED + "INVALID: Please enter full name with a space between first and last names." + Color.RESET)
            
            
            while True:
                contact_number = input("Enter the contact number (starting with +49):   ")
                # Remove any spaces or non-digit characters from the input
                contact_number = ''.join(filter(lambda char: char.isdigit() or char == '+', contact_number))

                 # Validate that the phone number starts with '+49' and a length of 11 digits for Germany
                if contact_number.startswith("+49") and len(contact_number) == 14:
                
                    # checks if the phone number is a duplicate
                    if is_duplicate_phone_number(contact_number, addressList):
                        print(Color.RED + 'INVALID: this number is already assigned to another contact' + Color.RESET)
                
                    else:
                        # If the input passes validation, proceed to add the contact
                        address = input("Enter the address:   ")
                        addressList.append([full_name, contact_number, address])
                        print(Color.GREEN + 'Contact added...' + Color.RESET)
                        
                        # displays the newly added contact immediately
                        print(Color.GREEN + f"New contact added: Name: {full_name}, Contact: {contact_number}, Address: {address}" + Color.RESET)
                        break
                else:
                    print(Color.RED + "INVALID: The phone number must start with +49 and must have 11 digits" + Color.RESET)


        elif choice == 2:
            while True:
                print(Color.GREEN + 'Looking up for a contact...' + Color.RESET)    
                term = input('Enter the full name (with a space between first and last name):  ').lower()
                # checking for the valid format
               
                if ' ' not in term:
                    print(Color.RED + "INVALID: please make sure you have enetered the full name and there is space between first and last name" + Color.RESET)
            
                else:
                    contact_found = False 
                    for contacts in addressList:
                        if term == contacts[0]:
                            print(Color.GREEN + "Contact found:" + Color.RESET)
                            print(f"Name: {contacts[0]}, Contact: {contacts[1]}, Address: {contacts[2]}")
                            contact_found = True
                            break
                    if not contact_found:
                        print(Color.RED + "Contact not found!" + Color.RESET)        
                
                another_search = input(Color.GREEN + "Do you want to look for another contact? (Yes/No:)" '\n' + Color.RESET)
                if another_search == 'no':
                    break # exits the loop

        elif choice == 3:
            update_contact(addressList)
        
        elif choice == 4:
            print(Color.GREEN + 'Displaying all the contacts...')
            for person in range(len(addressList)):
                print(addressList[person])


    else:
        print(Color.GREEN + 'Terminating program...' + Color.RESET)   

        # Saving to external file in txt.file
    outfile = open('theaddresslist.txt', 'w') # 'w' for the writing mode in the second argument
    for x in addressList:
        outfile.write(','.join(str(item) for item in x) + '\n')  
    outfile.close()    



if __name__ == '__main__':
    main()

