# Example on how to convert an hexadecimal number to a decimal one:
# 8ef = (8 x 16^2) + (14 x 16^1) + (15 x 16^0)

def hex_output():
    '''Convert a hexadecimal number to decimal'''
    decnum = 0
    hexnum = input('Enter a hex number to convert: ')

    for power, digit in enumerate(reversed(hexnum)):
         decnum = decnum + int(digit, 16) * (16 ** power)
    print(decnum)

def hex_output2():
    '''Convert a hexadecimal number to decimal without using the 
    built-in int() function'''
    decnum = 0
    hexnum = input('Enter a hex number to convert: ')

    for power, digit in enumerate(reversed(hexnum)):
        if 48 <= ord(digit) <= 57:
            dd = ord(digit) - 48
        elif 97 <= ord(digit) <= 102:
            dd = ord(digit) - 97 - 10
        decnum = decnum + dd * (16 ** power)
    print(decnum)

def name_triangle():
    '''Create a name triangle'''
    user_name = input('Please, provide your name: ')

    name = ''
    for letter in user_name:
        name = name + letter
        print(name)
            
def name_triangle2():
    """Get the user's name. Print a name triangle, starting
    with the first letter, then the first two letters, etc.
    """
    name = input("Enter your name: ")

    for i in range(len(name)):
        print(name[:i+1])

if __name__ == "__main__":
    hex_output()
    hex_output2()
    name_triangle()
    name_triangle2()



