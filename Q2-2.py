numbers = [0, 7, 4, 8, 1, 3, 8, 10, 11, 2, 5, 12, 9]

# Sorterer tallene med list sin egen sort fordi jeg ikke gidder å lage en sorteringsalgoritme
#numbers.sort()

# print(numbers)

#oppsamlingsliste = list()
#tallrekke = list()
#oppsamlingsliste.append(tallrekke)

#for i in range(len(numbers)):
#
#    #   print("index: "+str(i)+", number: "+str(numbers[i])+" tallrekke length: "+str(len(tallrekke)))
#    if i > 0:
#        if numbers[i - 1] == numbers[i] or numbers[i - 1] + 1 == numbers[i]:
#            #           print ("en tallrekke!")
#            tallrekke.append(numbers[i])
#        else:
#            tallrekke = list()
#            tallrekke.append(numbers[i])
#            oppsamlingsliste.append(tallrekke)
#    else:
#        tallrekke.append(numbers[i])

# tallrekkeFunnet = 0

#for i in reversed(range(len(oppsamlingsliste))):
#    if tallrekkeFunnet == 0 and len(oppsamlingsliste[i]) > 1:
#        print("Tallrekke med hoyeste verdi: " + str(oppsamlingsliste[i]))
#        tallrekkeFunnet = 1

# print(oppsamlingsliste)




def sort_list(numbers):
    list1 = list()
    list2 = list()
    chain = list()
    list1.append(chain)
    found_chain = 0
    for i in numbers:
        list1 = [x for x in list1 if [i] > x] + [i] + [x for x in list1 if [i] <= x]
    for j in list2:
        if j not in list2:
            list2[:0] = [j]
            j = j + 1

        for numbers[i] in list:
            if i > 0:
                if numbers [i-1] == numbers[i] or numbers[i - 1] + 1 == numbers[i]:
                    chain.append(numbers[i])
                else:
                    chain = list()
                    chain.append(numbers[i])
                    list.append(chain)
            else:
                chain.append(numbers[i])

    for numbers[i] in list2:
        if found_chain == 0 and len(chain[i]) > 1:
            print("Longest chain found:" + str[chain[i]])
            found_chain = 1


sort_list(numbers)
