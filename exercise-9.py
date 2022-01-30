def firstlast(a_sequence):
    """Retrieve the first and last item of a sequence"""
    return a_sequence[:1] + a_sequence[-1:]

def even_odd_sums(a_sequence):
    """Return a two-element list, containing the sum of the even-indexed numbers
       and the sum of the odd-indexed numbers"""
    even_indexed = 0
    odd_indexed = 0
    for i, num, in enumerate(a_sequence, start=1):
        if i % 2 == 0:
            even_indexed = even_indexed + num
        else:
            odd_indexed = odd_indexed + num 
    return [even_indexed, odd_indexed]

def plus_minus(a_sequence):
    """Return the result of alternately adding and subtracting numbers form each other"""
    output = a_sequence[0]
    for i, num in enumerate(a_sequence[1:]):
        print(output)
        if i % 2 == 0:
            output = output + num
        else:
            output = output - num
    return output

def myzip(*a_sequence):
    """Partly emulates the built-in zip function"""
    step = len(a_sequence[0])
    n_items = len(a_sequence)

    # extract all the single elements from nested structure and put them in a list
    flattened  = list()
    for item1 in a_sequence:
        for item2 in item1:
            flattened.append(item2)

    # pair the elements into the required coupling order
    coupled = list()
    for i in range(n_items+1):
        for j in range(i, len(flattened), step):
            coupled.append(flattened[j])    
    
    # create couples
    output = list()
    for i in range(0, len(coupled)+1, n_items):
        output.append(tuple(coupled[i:i+1] + coupled[i+1:i+n_items]))

    return output[:len(output)-1]



if __name__ == "__main__":
    print(firstlast('abc'))
    print(firstlast([1, 2, 3, 4]))
    print(even_odd_sums([10, 20, 30, 40, 50, 60]))
    print(plus_minus([10, 20, 30, 40, 50, 60]))
    print(myzip([10, 20, 30], 'abc')) # [(10, 'a'), (20, 'b'),(30,'c')]