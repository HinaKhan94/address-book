def main():

    #creating an address list
    addressList = []

    choice = 0
    while choice !=4:
        print('** Address Manager **')
        print('1) Add a contact')
        print('2) Look up a contact')
        print('3) Display all contacts')
        print('4) Quit')
        choice = int(input())

        if choice == 1:
            print('Adding a contact...')
            nPerson = input("Enter the contact's full name:   ")
            contact = input("Enter the contact number:   ")
            address = input("Enter the address:   ")
            addressList.append([nPerson, contact, address])

        elif choice == 2:
            print('Looking up for a contact...')    
            term = input('Enter the name:  ')
            for i in addressList:
                if term in i:
                    print(i)


        elif choice == 3:
            print('Displaying all the contacts...')
            for x in range(len(addressList)):
                print(addressList[x])


    else:
        print('Terminating program...')        


if __name__ == '__main__':
    main()
