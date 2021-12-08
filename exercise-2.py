def my_sum(*input_numbers):
    result = 0
    for n in input_numbers:
        result = result + n
    return result

def my_sum2(numbers_to_sum, starting_point=0):
    result = 0
    for n in numbers_to_sum:
        result = result + n
    return result + starting_point

def my_mean(*input_numbers):
    n = len(input_numbers)
    print(f'The length is {n}')
    sum = 0
    for n in input_numbers:
        sum = sum + n
    return sum/n

def my_string_function(*input_string):
    n = len(input_string)
    strings_lenght = list()
    for str in input_string:
        strings_lenght.append(len(str))
    strings_lenght = tuple(strings_lenght)
    print(strings_lenght)
    return (max(strings_lenght), min(strings_lenght), sum(strings_lenght)/n)

def my_sum3(*input_objects):
    final_sum = 0
    for item in input_objects:
        try:
            final_sum = final_sum + int(item)
        except (TypeError, ValueError):
            continue
    return final_sum

def my_void_function():
    '''Returns none'''
    pass


if __name__== "__main__":
    print(my_sum(3,5,21))
    #print(my_sum(3, 5, "a"))
    #print(my_sum([3, 5, 5]))
    print(my_sum(*[3,5,21]))
    print(sum([1,2,3],4))
    print(my_sum2([1,2,3], 1))
    print(my_sum2([1,2,3]))
    print(my_mean(1, 2, 3))
    print(my_string_function("abc", "ab", "a"))
    print(my_sum3('10', 5, 'abs'))
<<<<<<< HEAD
=======
    # 'abs' would throw a ValueError, whereas ['abc', '10', 10] a TypeError
>>>>>>> f2dba97 (Add exercise-2.py)
    print(my_sum3('10', 5, 'abs', ['abc', '10', 10]))
    print(my_sum3(['abc', '10', 10], '10', 5, 'abs'))

    
