def countdown(num):
    newList = []
    for x in range(num, -1, -1):
        newList.append(x)
    return newList

def print_and_return(someList):
    print(someList[0])
    return someList[1]
print(print_and_return([1,2]))

def first_plus_length(someList):
    sum = someList[0] + len(someList)
    return sum
print(first_plus_length([11,2,32,64,53,2,6,17,81,4]))

def values_greater_than_second(someList):
    if len(someList) < 2:
        return False
    else:
        newList = []
        for x in range(len(someList)):
            if someList[x] > someList[1]:
                newList.append(someList[x])
        count = len(newList)
        print(count)
        return newList
print(values_greater_than_second([5,2,3,2,1,4]))

def length_and_value(size, value):
    newList = []
    for x in range(size):
        newList.append(value)
    return newList
print(length_and_value(6,2))
