# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    result = []
    # using dictionary for queries
    q_dict = {key for i, key in enumerate(queries)}

    for el in files:
        split_el = el.split("/")
        if split_el[-1] in q_dict:
            result.append(el)


    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
