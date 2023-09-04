#ANSI codes for text color
class Color:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'

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
    while choice !=4:
        print('********** My Address Manager ***********')
        print(Color.GREEN + 'Choose one option from the options below:  ' '\n' + Color.RESET)
        print('1) Add a contact')
        print('2) Look up a contact')
        #print('3) Update or Delete a contact')
        print('3) Display all contacts')
        print('4) Quit', '\n')
        choice = int(input('What would you like to do?   '))

        if choice == 1:
            print(Color.GREEN + 'Adding a contact...' + Color.RESET)
            nPerson = input("Enter the contact's full name:   ").lower()
            
            while True:
                contact_input = input("Enter the contact number (11 digits):   ")
                # Remove any spaces or non-digit characters from the input
                contact_input = ''.join(filter(str.isdigit, contact_input))
                try:
                    contact = int(contact_input)
                    if len(contact_input) == 11:
                        break # exists the loop if the value is a valid value
                    else:
                        print(Color.RED + "***INVALID: the number must be 11 digits" + Color.RESET) 
                except ValueError:
                    print(Color.RED + "***INVALID: you need to enter a number!***" + Color.RESET)
                
            address = input("Enter the address:   ")
            addressList.append([nPerson, contact, address])
            # displays the newly added contact immediately
            print(Color.GREEN + f"New contact added: Name: {nPerson}, Contact: {contact}, Address: {address}" + Color.RESET)

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
