def main():
    # To make sure the application runs even if the txt file is deleted somehow
    # the except argument will throw an error and start making a new file 
    try:
        #creating an address list
        addressList = []
        infile = open('theaddresslist', 'r') # 'r' is for reading the file in the second argument
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
        print('** Address Manager **')
        print('Choose one option from the options below:  ' '\n')
        print('1) Add a contact')
        print('2) Look up a contact')
        print('3) Display all contacts')
        print('4) Quit', '\n')
        choice = int(input('What would you like to do?   '))

        if choice == 1:
            print('Adding a contact...')
            nPerson = input("Enter the contact's full name:   ").lower()
            contact = int(input("Enter the contact number:   "))
            #try:
                #contact = int(input("Enter the contact number:   "))
            #except ValueError:
                #print("INVALID: you need to enter a number!")
            address = input("Enter the address:   ")
            addressList.append([nPerson, contact, address])

        elif choice == 2:
            print('Looking up for a contact...')    
            term = input('Enter the name:  ').lower()
            for i in addressList:
                if term in i:
                    print(i)


        elif choice == 3:
            print('Displaying all the contacts...')
            for x in range(len(addressList)):
                print(addressList[x])


    else:
        print('Terminating program...')   

        # Saving to external file in txt.file
    outfile = open('theaddresslist.txt', 'w') # 'w' for the writing mode in the second argument
    for x in addressList:
        outfile.write(','.join(x) + '\n')  
    outfile.close()    



if __name__ == '__main__':
    main()
