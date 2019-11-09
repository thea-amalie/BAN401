numbers = [0, 7, 4, 8, 1, 3, 8, 10, 11, 2, 5, 12, 9]

# Sorterer tallene med list sin egen sort fordi jeg ikke gidder å lage en sorteringsalgoritme
numbers.sort()

# print(numbers)

oppsamlingsliste = list()
tallrekke = list()
oppsamlingsliste.append(tallrekke)

for i in range(len(numbers)):

    #   print("index: "+str(i)+", number: "+str(numbers[i])+" tallrekke length: "+str(len(tallrekke)))
    if i > 0:
        if numbers[i - 1] == numbers[i] or numbers[i - 1] + 1 == numbers[i]:
            #           print ("en tallrekke!")
            tallrekke.append(numbers[i])
        else:
            tallrekke = list()
            tallrekke.append(numbers[i])
            oppsamlingsliste.append(tallrekke)
    else:
        tallrekke.append(numbers[i])

tallrekkeFunnet = 0

for i in reversed(range(len(oppsamlingsliste))):
    if tallrekkeFunnet == 0 and len(oppsamlingsliste[i]) > 1:
        print("Tallrekke med hoyeste verdi: " + str(oppsamlingsliste[i]))
        tallrekkeFunnet = 1

# print(oppsamlingsliste)