def intersection(arrays):
    """
    YOUR CODE HERE
    """
    
    from collections import defaultdict
    #using a dictionary, key is a number, value is a sum of occurances in all arrays
    num_dict = defaultdict(int)
    # result array for output
    result = []

    # flatten_list = [j for sub in arrays for j in sub] 
    

    # for el in flatten_list:
    #     #counting the occurances of the same numbers
    #     num_dict[el] +=1
    #     if num_dict[el] >= len(arrays):
    #         result.append(el)


    for sub_array in arrays:
        for el in sub_array:
            # counting the occurances of the same numbers
            num_dict[el] +=1
            if num_dict[el] >= len(arrays):
                result.append(el)
    

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
