

data_list = [12,11,10,9,8,7,6,5,4,3]

def reverse(data_list):
    length = len(data_list)
    s = length

    new_list = [None]*length

    for item in data_list:
        s = s - 1
        new_list[s] = item
    print (data_list)

reverse(data_list)