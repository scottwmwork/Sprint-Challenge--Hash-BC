#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(length)

    """
    YOUR CODE HERE
    """

    # Insert data into hashtable
    for index in range(0,length):
        hash_table_insert(ht, weights[index], index)

    # Find the two values whose sum equals the weights limit
    for index in range(0,length):
        find_val = limit - weights[index]
        found = hash_table_retrieve(ht, find_val)
        
        if found is not None:
            if index > found:
                return (index, found)
            else:
                return (found, index)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
