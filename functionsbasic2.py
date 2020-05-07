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

def biggie_size(numlist):
    for x in range(len(numlist)):
        if numlist[x] > 0:
            numlist[x] = "Big"
    return numlist
print(biggie_size([-5,5,3,-3]))

def count_positives(numlist):
    count = 0
    for x in range(len(numlist)):
        if numlist[x] > 0:
            count += 1
    numlist[len(numlist)-1] = count
    return numlist
print(count_positives([2,1,4,-3,-5,-1,-6,-9]))

def ultimate_analysis(alist):
    sum = 0
    max = alist[0]
    min = alist[0]
    for x in range(len(alist)):
        sum += alist[x]
        if alist[x] > max:
            max = alist[x]
        if alist[x] < min:
            min = alist[x]
    lnth = len(alist)
    avg = sum / lnth
    info = {"Sum": sum, "Maximum": max, "Minimum": min, "Length": lnth, "Average": avg}
    return info
print(ultimate_analysis([3,2,66,34,5,93,24,53,85,4,24,6,44,11,42,46,27,8,58,89,56,34,17]))

def reverse_list(dalist):
    for x in range(int((len(dalist)/2))):
        y = dalist[x]
        dalist[x] = dalist[len(dalist)-1-x]
        dalist[len(dalist)-1-x] = y
    return dalist
print(reverse_list([3,-2,-4,9]))