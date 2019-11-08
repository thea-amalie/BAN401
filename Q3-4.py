#making a tuple to store data:
# tuple = first name, last name, student ID, GPA, major, NHHS groups
#NHHS group membership is a tuple within a tuple
T1 = ("Mike", "Wheeler", "19710", 3.5, "FIE", ("it.gruppen")),\
     ("Nancy", "Wheeler", "19670", 3.6, "ENE", ("K7 Bulletin", "NHHS Opptur", "NHHS Energi")),\
     ("Steve", "Harrington", "19660", 2.4, "STR", ("NA")),\
     ("Mike", "Wazowski", "18119", 2.4, "BAN", ("NA")),\
     ("Jeffrey", "Lebowski", "69420", 4.2, "BLZ", ("NHHI Bowling", "NHHI Vinum")),\
     ("Ivan", "Belik", "12345", 1.8, "BAN", ("it.gruppen, NHHS Consulting")),\
     ("Sterling", "Archer", "11007", 2.7, "MBM", ("NHHI Lacrosse"))

#Making a "search engine":

while True:
    a = str(input("Who are you looking for?\n"))  # converting the input value into a string
    for value in T1: #checking every value in T1
        if a in value and a != "Wheeler" and a != "Mike": #if the input value is found in T1
            print("Retrieving data for student", value[0], value[1])
            print("- GPA:", value[3], "\n- Major:", value[4]) #printing the GPA and Major
            print("- NHHS group membership:\n", value[5], "\n") #printing a membership

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
                        print("Retrieving data for student", value[0], value[1])
                        print("- GPA:", value[3], "\n- Major:", value[4])  # printing the GPA and Major
                        print("- NHHS group membership:\n", value[5])  # printing a membership
                        c = str(input("Would you like to make a new search? (y/n)\n"))
                    elif a == "Wheeler":
                        print("Several results matched your query:\n 1.", T1[0][0], T1[0][1], "\n 2.", T1[1][0],
                              T1[1][1])
                        b = str(input("Enter a number of the search result for which you want to retrieve the info \nor enter 'all' to print info for all matching results:\n"))
                        if b == "1":
                            print("Retrieving data for student", value[0], value[1])
                            print("- GPA:", value[3], "\n- Major:", value[4])  # printing the GPA and Major
                            print("- NHHS group membership:\n", value[5])  # printing a membership
                            c = str(input("Would you like to make a new search? (y/n)\n"))
                            break
                        elif b == "2":
                            print("Retrieving data for student", T1[1][0], T1[1][1])
                            print("- GPA:", T1[1][3], "\n- Major:", T1[1][4])  # printing the GPA and Major
                            print("- NHHS group membership:\n", T1[1][5])  # printing a membership
                            c = str(input("Would you like to make a new search? (y/n)\n"))
                            break
                        elif b == "all":
                            print("Retrieving data for student", value[0], value[1])
                            print("- GPA:", value[3], "\n- Major:", value[4])  # printing the GPA and Major
                            print("- NHHS group membership:\n", value[5])  # printing a membership
                            print("")
                            print("Retrieving data for student", T1[1][0], T1[1][1])
                            print("- GPA:", T1[1][3], "\n- Major:", T1[1][4])  # printing the GPA and Major
                            print("- NHHS group membership:\n", T1[1][5])  # printing a membership
                            c = str(input("Would you like to make a new search? (y/n)\n"))
                            break
                        break

                    elif a == "Mike":
                        print("Several results matched your query:\n 1.", T1[0][0], T1[0][1], "\n 2.", T1[3][0],
                              T1[3][1])
                        b = str(input("Enter a number of the search result for which you want to retrieve the info \nor enter 'all' to print info for all matching results:\n"))
                        if b == "1":
                            print("Retrieving data for student", value[0], value[1])
                            print("- GPA:", value[3], "\n- Major:", value[4])  # printing the GPA and Major
                            print("- NHHS group membership:\n", value[5])  # printing a membership
                            c = str(input("Would you like to make a new search? (y/n)\n"))
                            break
                        elif b == "2":
                            print("Retrieving data for student", T1[3][0], T1[3][1])
                            print("- GPA:", T1[3][3], "\n- Major:", T1[3][4])  # printing the GPA and Major
                            print("- NHHS group membership:\n", T1[3][5])  # printing a membership
                            c = str(input("Would you like to make a new search? (y/n)\n"))
                            break
                        elif b == "all":
                            print("Retrieving data for student", value[0], value[1])
                            print("- GPA:", value[3], "\n- Major:", value[4])  # printing the GPA and Major
                            print("- NHHS group membership:\n", value[5])  # printing a membership
                            print("")
                            print("Retrieving data for student", T1[3][0], T1[3][1])
                            print("- GPA:", T1[3][3], "\n- Major:", T1[3][4])  # printing the GPA and Major
                            print("- NHHS group membership:\n", T1[3][5])  # printing a membership
                            c = str(input("Would you like to make a new search? (y/n)\n"))
                            break
                        break

            while c == "n":
                print("Exiting the program...")
                break
            break

        elif a == "Wheeler":
            print("Several results matched your query:\n 1.", T1[0][0], T1[0][1], "\n 2.", T1[1][0],T1[1][1])
            b = str(input(
                "Enter a number of the search result for which you want to retrieve the info \nor enter 'all' to print info for all matching results:\n"))

            if b == "1":
                print("Retrieving data for student", value[0], value[1])
                print("- GPA:", value[3], "\n- Major:", value[4])  # printing the GPA and Major
                print("- NHHS group membership:\n", value[5])  # printing a membership
                c = str(input("Would you like to make a new search? (y/n)\n"))
                break

            elif b == "2":
                print("Retrieving data for student", T1[1][0], T1[1][1])
                print("- GPA:", T1[1][3], "\n- Major:", T1[1][4])  # printing the GPA and Major
                print("- NHHS group membership:\n", T1[1][5])  # printing a membership
                c = str(input("Would you like to make a new search? (y/n)\n"))
                break

            elif b == "all":
                print("Retrieving data for student", value[0], value[1])
                print("- GPA:", value[3], "\n- Major:", value[4])  # printing the GPA and Major
                print("- NHHS group membership:\n", value[5])  # printing a membership
                print("")
                print("Retrieving data for student", T1[1][0], T1[1][1])
                print("- GPA:", T1[1][3], "\n- Major:", T1[1][4])  # printing the GPA and Major
                print("- NHHS group membership:\n", T1[1][5])  # printing a membership
                c = str(input("Would you like to make a new search? (y/n)\n"))
                break
            break

        elif a == "Mike":
            print("Several results matched your query:\n 1.", T1[0][0], T1[0][1], "\n 2.", T1[3][0],T1[3][1])
            b = str(input(
                "Enter a number of the search result for which you want to retrieve the info \nor enter 'all' to print info for all matching results:\n"))

            if b == "1":
                print("Retrieving data for student", value[0], value[1])
                print("- GPA:", value[3], "\n- Major:", value[4])  # printing the GPA and Major
                print("- NHHS group membership:\n", value[5])  # printing a membership
                c = str(input("Would you like to make a new search? (y/n)\n"))
                break

            elif b == "2":
                print("Retrieving data for student", T1[3][0], T1[3][1])
                print("- GPA:", T1[3][3], "\n- Major:", T1[3][4])  # printing the GPA and Major
                print("- NHHS group membership:\n", T1[3][5])  # printing a membership
                c = str(input("Would you like to make a new search? (y/n)\n"))
                break

            elif b == "all":
                print("Retrieving data for student", value[0], value[1])
                print("- GPA:", value[3], "\n- Major:", value[4])  # printing the GPA and Major
                print("- NHHS group membership:\n", value[5])  # printing a membership
                print("")
                print("Retrieving data for student", T1[3][0], T1[3][1])
                print("- GPA:", T1[3][3], "\n- Major:", T1[3][4])  # printing the GPA and Major
                print("- NHHS group membership:\n", T1[3][5])  # printing a membership
                c = str(input("Would you like to make a new search? (y/n)\n"))
                break
            break
    break
