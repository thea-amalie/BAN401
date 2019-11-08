#  MANGLER WHILE "Y" = TRUE I NEDERSTE DEL
# MANGLER SØKBARHET PÅ BÅDE ETTERNAVN OG FORNAVN


T1 = ("Mike", "Wheeler", "19710", 3.5, "FIE", ("it.gruppen")), \
     ("Nancy", "Wheeler", "19670", 3.6, "ENE", ("K7 Bulletin", "NHHS Opptur", "NHHS Energi")), \
     ("Steve", "Harrington", "19660", 2.4, "STR", ("NA")), \
     ("Mike", "Wazowski", "18119", 2.4, "BAN", ("NA")), \
     ("Jeffrey", "Lebowski", "69420", 4.2, "BLZ", ("NHHI Bowling", "NHHI Vinum")), \
     ("Ivan", "Belik", "12345", 1.8, "BAN", ("it.gruppen, NHHS Consulting")), \
     ("Sterling", "Archer", "11007", 2.7, "MBM", ("NHHI Lacrosse"))

def call_retrieve():
    print("Retrieving data for student", value[0], value[1])
    print("- GPA:", value[3], "\n- Major:", value[4])  # printing the GPA and Major
    print("- NHHS group membership:\n", value[5], "\n")  # printing a membership

def call_choice():
    print("Retrieving data for student", value[0], value[1])
    print("- GPA:", value[3], "\n- Major:", value[4])  # printing the GPA and Major
    print("- NHHS group membership:\n", value[5])  # printing a membership

def call_choiceWheeler():
    print("Several results matched your query:\n 1.", T1[0][0], T1[0][1], "\n 2.", T1[1][0], T1[1][1])


def call_Wheeler1():
    print("Retrieving data for student", value[0], value[1])
    print("- GPA:", value[3], "\n- Major:", value[4])  # printing the GPA and Major
    print("- NHHS group membership:\n", value[5])  # printing a membership

def call_Wheeler2():
    print("Retrieving data for student", T1[1][0], T1[1][1])
    print("- GPA:", T1[1][3], "\n- Major:", T1[1][4])  # printing the GPA and Major
    print("- NHHS group membership:\n", T1[1][5])  # printing a membership

def call_all():
    print("Retrieving data for student", value[0], value[1])
    print("- GPA:", value[3], "\n- Major:", value[4])  # printing the GPA and Major
    print("- NHHS group membership:\n", value[5])  # printing a membership
    print("")
    print("Retrieving data for student", T1[1][0], T1[1][1])
    print("- GPA:", T1[1][3], "\n- Major:", T1[1][4])  # printing the GPA and Major
    print("- NHHS group membership:\n", T1[1][5])  # printing a membership
    c = str(input("Would you like to make a new search? (y/n)\n"))

def call_choiceMike():
    print("Several results matched your query:\n 1.", T1[0][0], T1[0][1], "\n 2.", T1[3][0],T1[3][1])

def call_Mike1():
    print("Retrieving data for student", value[0], value[1])
    print("- GPA:", value[3], "\n- Major:", value[4])  # printing the GPA and Major
    print("- NHHS group membership:\n", value[5])  # printing a membership

def call_Mike2():
    print("Retrieving data for student", T1[3][0], T1[3][1])
    print("- GPA:", T1[3][3], "\n- Major:", T1[3][4])  # printing the GPA and Major
    print("- NHHS group membership:\n", T1[3][5])  # printing a membership

def call_allMike():
    print("Retrieving data for student", value[0], value[1])
    print("- GPA:", value[3], "\n- Major:", value[4])  # printing the GPA and Major
    print("- NHHS group membership:\n", value[5])  # printing a membership
    print("")
    print("Retrieving data for student", T1[3][0], T1[3][1])
    print("- GPA:", T1[3][3], "\n- Major:", T1[3][4])  # printing the GPA and Major
    print("- NHHS group membership:\n", T1[3][5])  # printing a membership


# Making a "search engine":


while True:
    a = str(input("Who are you looking for?\n"))  # converting the input value into a string
    for value in T1:  # checking every value in T1
        if a in value and a != "Wheeler" and a != "Mike":  # if the input value is found in T1
            call_retrieve()
            c = str(input("Would you like to make a new search? (y/n)\n"))

            while c != "y" and c != "n":
                print("Incorrect input. Please try again")
                print("---------------")
                c = str(input("Would you like to make a new search? (y/n)\n"))

            while c == "y":
                print("---------------")
                a = str(input("Who are you looking for?\n"))  # converting the input value into a string
                for value in T1:  # checking every value in T1
                    if a in value and a != "Wheeler" and a != "Mike":  # if the input value is found in T1
                        call_choice()
                        c = str(input("Would you like to make a new search? (y/n)\n"))

                    elif a == "Wheeler":
                        call_choiceWheeler()
                        b = str(input("Enter a number of the search result for which you want to retrieve the info"
                                      " \nor enter 'all' to print info for all matching results:\n"))
                        if b == "1":
                            call_Wheeler1()
                            c = str(input("Would you like to make a new search? (y/n)\n"))
                            break
                        elif b == "2":
                            call_Wheeler2()
                            c = str(input("Would you like to make a new search? (y/n)\n"))
                            break
                        elif b == "all":
                            call_all()
                            break
                        break

                    elif a == "Mike":
                        call_choiceMike()
                        b = str(input("Enter a number of the search result for which you want to retrieve the info \n"
                            "or enter 'all' to print info for all matching results:\n"))
                        if b == "1":
                            call_Mike1()
                            c = str(input("Would you like to make a new search? (y/n)\n"))
                            break
                        elif b == "2":
                            call_Mike2()
                            c = str(input("Would you like to make a new search? (y/n)\n"))
                            break
                        elif b == "all":
                            call_allMike()
                            c = str(input("Would you like to make a new search? (y/n)\n"))
                            break
                        break

            while c == "n":
                print("Exiting the program...")
                break
            break

        # må inn en while om at så lenge c = y så fortsetter vi

        elif a == "Wheeler":
            call_choiceWheeler()
            b = str(input("Enter a number of the search result for which you want to retrieve the info \n"
                          "or enter 'all' to print info for all matching results:\n"))
            if b == "1":
                call_Wheeler1()
                c = str(input("Would you like to make a new search? (y/n)\n"))
                break
            elif b == "2":
                call_Wheeler2()
                c = str(input("Would you like to make a new search? (y/n)\n"))
                break
            elif b == "all":
                call_all()
                c = str(input("Would you like to make a new search? (y/n)\n"))
                break
            break

        elif a == "Mike":
            call_choiceMike()
            b = str(input(
                "Enter a number of the search result for which you want to retrieve the info \n"
                "or enter 'all' to print info for all matching results:\n"))
            if b == "1":
                call_Mike1()
                c = str(input("Would you like to make a new search? (y/n)\n"))
                break
            elif b == "2":
                call_Mike2()
                c = str(input("Would you like to make a new search? (y/n)\n"))
                break
            elif b == "all":
                call_allMike()
                c = str(input("Would you like to make a new search? (y/n)\n"))
                break
            break
    break
