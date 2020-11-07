def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # dict_weights = {print(f"{x}:{i}") for i, x in enumerate(weights)}
    dict_weights = {}

    for i in range(len(weights)):
        if limit - weights[i] in dict_weights:
            return (i,dict_weights[limit - weights[i]] )
        else:
            dict_weights[weights[i]] = i

    return None

weights = [ 4, 6, 10, 15, 16 ]
length = 5
limit = 21
print(get_indices_of_item_weights(weights, length, limit))


