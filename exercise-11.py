from operator import itemgetter

def alphabetize_names(list_of_people):
    """Function returns the list of dicts sorted by last name and then first name"""    
    def person_dict_to_list(d):
        return [d['last'], d['first']]
    
    return sorted(list_of_people, key=person_dict_to_list)


def alphabetize_names_alternative(list_of_people):
    """Function returns the list of dicts sorted by last name and then first name"""    
    for person in sorted(list_of_people, key=itemgetter('last', 'first')):
        print(f'{person["last"]}, {person["first"]}: {person["email"]}')


def alphabetize_names_alternative_2(list_of_people):
    """Function returns the list of dicts sorted by last name and then first name"""    
    return sorted(list_of_people, key=itemgetter('last', 'first'))


def sort_by_abs_value(sequence_of_numbers):
    """Given a sequence of positive and negative numbers, sort them by absolute value"""
    print(f'The unsorted sequence of numbers is: {sequence_of_numbers}')
    return sorted(sequence_of_numbers, key=abs)

def sort_by_numb_of_vowels(list_of_strings):
    """Given a list of strings, sort them according to how many vowels they contain"""
    
    # find how many vowels in each string
    vowels = 'aeiou'
    n_vowels = list()
    for string in list_of_strings:
        counter = 0
        for vowel in vowels:
            n = string.lower().count(vowel)
            counter = counter + n
        n_vowels.append(counter)
    n_vowels_string = dict(zip(list_of_strings, n_vowels))

    # order the dictionary by value
    sorted_dict = dict(sorted(n_vowels_string.items(), key=itemgetter(1)))
    return list(sorted_dict.keys())

def by_vowel_count(one_word):
    counter = 0
    for one_chr in one_word.lower():
        if one_chr in 'aeiou':
            counter = counter + 1
    return counter

def sort_by_vowel_count(word):
    """Given a list of strings, sort them according to how many vowels they contain"""
    return sorted(word, key=by_vowel_count)


def sort_by_sum(list_of_lists):
    """Given a list of lists, with each list containing zero or more numbers, 
       sort by the sum of each inner list's numbers."""
    return sorted(list_of_lists, key=sum)



if __name__ == "__main__":
    
    import random
    PEOPLE = [{'first':'Reuven', 'last':'Lerner','email':'reuven@lerner.co.il'},
                {'first':'Donald', 'last':'Trump', 'email':'president@whitehouse.gov'},
                    {'first':'Vladimir', 'last':'Putin','email':'president@kremvax.ru'}]

    print(alphabetize_names(PEOPLE))
    print(alphabetize_names_alternative(PEOPLE))
    print(alphabetize_names_alternative_2(PEOPLE))

    list_of_numbers = [random.randint(-100, 100) for i in range(0, 10)]
    print(sort_by_abs_value(list_of_numbers))

    list_of_strings = ['Reuven', 'Lerner', 'Donald', 'Trump', 'Vladimir', 'Putin']
    print(sort_by_numb_of_vowels(list_of_strings))

    list_of_lists_containing_numbers = [[23, 3232], [54], [543,9,23], []]
    print(sort_by_sum(list_of_lists_containing_numbers))




