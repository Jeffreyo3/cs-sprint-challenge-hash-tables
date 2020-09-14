def intersection(arrays):
    """
    
    """
    # calculate how many arrays there are
    numOfLists = len(arrays)

    # base case
    if numOfLists == 0:
        return None

    # if only one array, return array
    # at zero idx since all nums are in that array
    if numOfLists == 1:
        return arrays[0]

    # for 2 or more arrays:
    # create hashtable/dictionary
    numberDict = {}
    
    # loop through array of arrays
    for array in arrays:
        # loop through all numbers in current array
        for number in array:
            # increment 'count' in dictionary for each number
            if number not in numberDict:
                numberDict[number] = 1
            else:
                numberDict[number] += 1
    # make a list to store common numbers
    commonNums = []
    # go through all unique numbers found in the array of arrays
    for key, value in numberDict.items():
        # if the number has shown up the same number of times 
        # as there are arrays in the arrays list, add to list
        if value == numOfLists:
            commonNums.append(key)


    return commonNums


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
