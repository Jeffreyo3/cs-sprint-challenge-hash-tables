def get_indices_of_item_weights(weights, length, limit):
    """
    find two items whos sum of weights == weight limit
    returns a tuple of indexes. the lower value on the left and higher on the right

    """
    # base case
    if length <= 1:
        print(None)
        return None

    # create a hashtable/dictionary
    weightsDict = {}

    for idx, weight in enumerate(weights):
        # print(weight, idx)
        # find difference between current weight & limit
        missingVal = limit - weight
        # if difference is already in the dictionary,
        # return the two items as a tuple
        if missingVal in weightsDict:
            missingIdx = weightsDict[missingVal]
            print("~~~~~~~")
            if missingVal > weight:
                print("values")
                print((missingVal, weight))
                print("indexes")
                print((missingIdx, idx))
                return(missingIdx, idx)
            else:
                print("values")
                print((weight, missingVal))
                print("indexes")
                print((idx, missingIdx))
                return (idx, missingIdx)
                
        # if check fails, add the current weight to the dict
        weightsDict[weight] = idx
        
        # print(weightsDict)
    return None

