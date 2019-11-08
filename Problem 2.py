
numbers = [0,7,4,8,1,3,8,10,11,2,5,12,9]


#create function to access the longest chain in the list
# without any duplicates

# can use LEN + PRINT + LIST


#def get_the_chain(numbers):
#    length = len(numbers)
#    i = 0
#    list = []
#    list2 = []
#    while i < length:
#        if i in numbers:
#            while i in numbers:
#                if i in numbers:
#                    i = i + 1
#                if i in numbers:
#                    return i
#                    chain1 = list + [i]

                    # mangler kode her som sjekker etter ny liste

                    # return y
                    # chain2 = list2 + [y]

#                    if chain1 and chain2 > 0:
#                        if len(chain1) > len(chain2):
#                            print (chain1)
#                        elif len(chain1) == len(chain2):
#                            if chain1[0] > chain2[0]:
#                                print (chain1)
#                            else:
#                                print (chain2)


def sort_chain(numbers):
    list = []
    for i in numbers:
        list = [x for x in list if i > x] + [i] + [x for x in list if i <= x]
    print(list)
    if [1] in list == ([0]+1):                      #hvis 1 = 0+1
            if [2] in list == ([1]+1):                  #hvis 2 = 1+1
                if [3] in list == ([2]+1):              #hvis 3 = 2+1
                    if [4] in list ==([3]+1):           #hvis 4 = 3+1
                        if [5] in list == ([4]+1):      #hvis 5 = 4+1
                            if [6] in list == ([5]+1):  #hvis 7 = 5+1   NOT
                                for [1] and [2] and [3] and [4] and [5] in list:
                                    chain1.append(x)
                                    print(chain1)





sort_chain(numbers)

#store the return string as list
# say it returns as a value a, then make that value into list

# if len(list1) > len (list2) -> print(list1) -> else...
#                                               ckeck if...
# len(list1) == len(list2); print den listen som har høyest verdi
# i index nr 0
# if list1[0] > list2[0] -> print list1 -> else print list 2


#def longest(numbers):
#    result = []
#    for i in numbers:
#        for a in result:
#            if i == 1[-1]+1:



# ADDING TO LIST WITHOUT APPEND
# make a list thats empty: x = []
# in the function add:
#   y = x + [7]


# if i+1 is in numbers







