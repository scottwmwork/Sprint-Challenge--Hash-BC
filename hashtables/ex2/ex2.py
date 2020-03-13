#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """

    # Insert tickets into hashtable
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
    
    route = []
    destination = hash_table_retrieve(hashtable, 'NONE')
    route.append(destination)
    while destination != 'NONE':
        destination = hash_table_retrieve(hashtable, destination)
        if destination != "NONE":
            route.append(destination)

    return route



