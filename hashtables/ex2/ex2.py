#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # memory allocation for output array
    route = [None]*length
    # using a dictionary, where key is a source, value i a destination
    hash_table = {}

    for i in range(length):
        hash_table[tickets[i].source] = tickets[i].destination

    # writing the first element of route with source NONE
    route[0] = hash_table["NONE"]
    for i in range(1,len(tickets)):
        route[i] = hash_table[route[i-1]]
   

    return route

#----------------tests----------------------
ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
                   ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]
print(reconstruct_trip(tickets, 10))
