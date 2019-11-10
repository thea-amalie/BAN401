Tuple = ("Mike", "Wheeler", 'Mike Wheeler', "19710", 3.5, "FIE", ("it.gruppen")), \
        ("Nancy", "Wheeler", 'Nancy Wheeler', "19670", 3.6, "ENE", ("K7 Bulletin \n   NHHS Opptur \n   NHHS Energi")), \
        ("Steve", "Harrington",'Steve Harrington', "19660", 2.4, "STR", ("None")), \
        ("Mike", "Wazowski",'Mike Wazowski', "18119", 2.4, "BAN", ("None")), \
        ("Jeffrey", "Lebowski",'Jeffrey Lebowski', "69420", 4.2, "BLZ", ("NHHI Bowling \n    NHHI Vinum")), \
        ("Ivan", "Belik",'Ivan Belik', "12345", 1.8, "BAN", ("it.gruppen \n    NHHS Consulting")), \
        ("Sterling", "Archer",'Sterling Archer', "11007", 2.7, "MBM", ("NHHI Lacrosse"))

def retrieve():
    print('----------------')
    print("Retrieving data for student", value[0], value[1],
          ' (student ID ', value[3],').')
    print("- GPA:", value[4], "\n- Major:", value[5])                       # printing the GPA and Major
    print("- NHHS group membership:\n   ", value[6])                        # printing a membership
    print('----------------')
def choice_Wheeler():
    print("Several results matched your query:\n 1.", Tuple[0][0], Tuple[0][1], ' ( ID ', Tuple[0][3],')'
          "\n 2.", Tuple[1][0], Tuple[1][1], '( ID ', Tuple[1][3],')')
def Wheeler1():
    print('----------------')
    print("Retrieving data for student", value[0], value[1],
          ' (student ID ', value[3], ').')
    print("- GPA:", value[4], "\n- Major:", value[5])  # printing the GPA and Major
    print("- NHHS group membership:\n   ", value[6])  # printing a membership
    print('----------------')
def Wheeler2():
    print('----------------')
    print("Retrieving data for student", Tuple[1][0], Tuple[1][1],
          ' (student ID ', Tuple[1][3], ').')
    print("- GPA:", Tuple[1][4], "\n- Major:", Tuple[1][5])                                   # printing the GPA and Major
    print("- NHHS group membership:\n  ", (Tuple[1][6]))                                       # printing a membership
    print('----------------')
def all_Wheeler():
    print('----------------')
    print("Retrieving data for student", value[0], value[1],
          ' (student ID ', value[3], ').')
    print("- GPA:", value[4], "\n- Major:", value[5])  # printing the GPA and Major
    print("- NHHS group membership:\n   ", value[6])  # printing a membership
    print('----------------')
    print("Retrieving data for student", Tuple[1][0], Tuple[1][1],
          ' (student ID ', Tuple[1][3], ').')
    print("- GPA:", Tuple[1][4], "\n- Major:", Tuple[1][5])  # printing the GPA and Major
    print("- NHHS group membership:\n", Tuple[1][6])  # printing a membership
    print('----------------')
    c = str(input("Would you like to make a new search? (y/n)\n"))
def choice_Mike():
    print("Several results matched your query:\n 1.", Tuple[0][0], Tuple[0][1], ' ( ID ', Tuple[0][3],')'
          "\n 2.", Tuple[3][0],Tuple[3][1], '( ID ', Tuple[3][3],')')
def Mike1():
    print('----------------')
    print("Retrieving data for student", value[0], value[1],
          ' (student ID ', value[3], ').')
    print("- GPA:", value[4], "\n- Major:", value[5])  # printing the GPA and Major
    print("- NHHS group membership:\n   ", value[6])  # printing a membership
    print('----------------')
def Mike2():
    print('----------------')
    print("Retrieving data for student", Tuple[3][0], Tuple[3][1],
          ' (student ID ', Tuple[1][3], ').')
    print("- GPA:", Tuple[3][4], "\n- Major:", Tuple[3][5])                                   # printing the GPA and Major
    print("- NHHS group membership:\n", Tuple[3][6])                                       # printing a membership
    print('----------------')
def all_Mike():
    print('----------------')
    print("Retrieving data for student", value[0], value[1],
          ' (student ID ', value[3], ').')
    print("- GPA:", value[4], "\n- Major:", value[5])  # printing the GPA and Major
    print("- NHHS group membership:\n   ", value[6])  # printing a membership
    print('----------------')
    print("Retrieving data for student", Tuple[3][0], Tuple[3][1],
          ' (student ID ', Tuple[1][3], ').')
    print("- GPA:", Tuple[3][4], "\n- Major:", Tuple[3][5])  # printing the GPA and Major
    print("- NHHS group membership:\n", Tuple[3][6])  # printing a membership
    print('----------------')

while True:
    a = str(input('Who are you looking for?\n'))
    for value in Tuple:
            if a in (set(Tuple[0])-set(Tuple[0][2:])) and a in (set(Tuple[3])-set(Tuple[3][2:])): #MIKE
                choice_Mike()
                b = str(input("Enter a number of the search result for which you want to retrieve the info"
                              " \nor enter 'all' to print info for all matching results:\n"))
                if b == '1':
                    Mike1()
                    pass
                elif b == '2':
                    Mike2()
                    pass
                elif b == 'all':
                    all_Mike()
                    pass
                c = str(input('Would you like to make a new search? (y/n)\n'))
                if c == 'y':
                    break  # returns to the top of the loop                         M
            if a in (set(Tuple[0])-set(Tuple[0][2:])) and a in (set(Tuple[1])-set(Tuple[1][2:])):
                choice_Wheeler()
                b = str(input("Enter a number of the search result for which you want to retrieve the info"
                              " \nor enter 'all' to print info for all matching results:\n"))
                if b == '1':
                    Wheeler1()
                    pass
                elif b == '2':
                    Wheeler2()
                    pass
                elif b == 'all':
                    all_Wheeler()
                    pass
                c = str(input('Would you like to make a new search? (y/n)\n'))
                if c == 'y':
                    break  # returns to the top of the loop
            if a in value:
                print('----------------')
                print('One match found.')
                retrieve()
                c = str(input('Would you like to make a new search? (y/n)\n'))
                if c == 'y':
                    continue #returns to the top of the loop

                if c == 'n':
                    print('Exiting the program...')
                    exit()

                else:
                    print('----------------')
                    print('Incorrect input. Please try again')
                    print('----------------')
                    c = str(input('Would you like to make a new search? (y/n)\n'))
                    if c == 'y':
                        continue
                    elif c == 'n':
                        exit()









