class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # base case
    if length <= 1:
        return ["NONE"]
        
    # create hashtable/dictionary to store destinations
    destinationDict = {}
    # preallocate array memory
    route = ['NONE'] * length
    
    # add routes to dictionary
    for ticket in tickets:
        destinationDict[ticket.source] = ticket.destination

    # print(destinationDict)

    # reconstruct trip by enumerating through dictionary

    # set starting location
    route[0] = destinationDict["NONE"]
    # go through each destination and insert the next destination's value
    # by checking the current index's key.
    for i in range(length - 1):
        route[i+1] = destinationDict[route[i]]
    
    print(route)

    return route
