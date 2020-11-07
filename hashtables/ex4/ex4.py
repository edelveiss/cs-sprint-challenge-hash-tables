def has_negatives(a):
    """
    YOUR CODE HERE
    """
    
    set_num = set()
    result = []
    
    for i in range(len(a)):
        n = abs(a[i])
        if n in set_num:
            result.append(n)
        else:
            set_num.add(n)
            
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
