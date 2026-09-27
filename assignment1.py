""" 
Q1. Write a program to read three numbers from user and compare
the greatest and smallest of those numbers and print the appropriate message. 
"""

def compare():
    a = int(input("1) Enter a number : "))
    b = int(input("2) Enter a number : "))
    c = int(input("3) Enter a number : "))

    # GREATEST
    print("using built-in max() : ",max(a,b,c))

    if a >= b and a >= c:
        greatest = a
    elif b >= a and b >= c:
        greatest = b
    else:
        greatest = c

    # SMALLEST
    print("using built-in min() : ",min(a,b,c))

    if a <= b and a <= c:
        smallest = a
    elif b <= a and b <= c:
        smallest = b
    else:
        smallest = c

    print("Manually: greatest = ", greatest, "smallest = ", smallest)



compare()




"""
Q2. Write a program to print the addition of first 30 natural numbers.
(Use while statement)
"""

def sum_of_30():
    i = 1
    total_sum = 0
    while i < 31:
        total_sum += i
        i += 1
    print(f"sum of first 30 natural numbers : {total_sum}")

sum_of_30()


"""
Q3. Write a program to print even numbers in between 10 to 20 by using while loop.
"""

def even_nums():
    i = 10
    while i <= 20:
        if i%2 == 0:
            print(i,end=" ")
        i += 1
    print()

even_nums()


"""
Q4. Write a program to search a number or a string in a list and print it.
Read the number /string to be searched, from the user. Make use of for and 
if statements.
"""

def item_search():
    lst = ['abc',1,2,3,4,"xyz","pqr",10,11,12,13]
    item = input("Enter an element to search : ")

    if item.isdigit():
        item = int(item)

    for element in lst:
        if element == item:
            print(f"{item} found in given list.")
            break
    else:
        print(f"{item} not found in given list.")

item_search()


"""
Q5. Write a program to print the prime and non-prime numbers.
(Can also decide a range like in between 20 to 50 numbers).
"""

def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

def prime_non_prime():
    primes = []
    non_primes = []
    for i in range(20,51):
        if is_prime(i):
            primes.append(i)
        else:
            non_primes.append(i)

    print(f"Between 20 to 50 : \nPrime numbers: {primes}")
    print(f"Non-Prime numbers: {non_primes}")

prime_non_prime()


"""
Q6. Write a program to read a string from the user.
Also, get a substring from the user and search it in the given string.
"""

def substr_search():
    str1 = input("enter a string : ")
    str2 = input("enter a sub string : ")

    # Built-in way-
    if str2 in str1:
        print(f"{str2} found in {str1}")
    else:
        print(f"{str2} not found in {str1}")

    # MANUAL WAY-
    found = False

    for i in range(len(str1) - len(str2) + 1):
        match = True

        for j in range(len(str2)):
            if str1[i + j] != str2[j]:
                match = False
                break

        if match:
            found = True
            print(f"{str2} found in {str1} at {i}:{i+len(str2)}")
            break

    if not found:
        print(f"{str2} not found in {str1}")    

substr_search()


"""
Q7. Write a program to read a string and read the substring 
from a specific position and print it.
"""

def slicing():
    string = input("Enter a string : ")
    start = int(input("enter start index of slice : "))
    end = int(input("enter end index (exclusive) of slice : "))

    substring = string[start:end]
    print(f"extracted substring : {substring}")

slicing()


"""
Q8. Write a program to count the occurrences of a character in the given string.
(For e.g., in string 'Hello World' count the occurrences of the letter 'l').
"""

def count_occurrences():
    string = input("Enter a string : ")
    letter = input("Enter a character to count occurrence : ")

    count = 0
    for s in string:
        if s == letter:
            count += 1
    print(f"occurrence of '{letter}' in {string} is {count} times.")

    # Built-in way-
    print("Using built-in count() : ",string.count(letter))

count_occurrences()


"""
Q9. Write a program to capitalize the first letter of a given string.
(e.g., this is an example)
"""

def cap():
    text = input("Enter a string: ")
    cap_text = text[0].upper() + text[1:]
    cap_text_1 = text.capitalize()
    cap_text_2 = text.title()
    print("using upper() : ",cap_text)
    print("using capitalize() : ",cap_text_1)
    print("using title() : ",cap_text_2)

cap()

"""
Q10. Write a program to replace a substring in a string with any other
substring or special characters. (e.g. In string s = 'This has to be the beginning
of the chapter', where replace the substring 'the beginning' with 'the end')
"""

def str_replace():
    string = input("Enter a string: ")
    target = input("Enter a substring to replace: ")
    replacement = input("Enter a substring to replace with: ")

    modified_string = string.replace(target, replacement)
    print(f"Modified string: {modified_string}")

str_replace()

"""
Q11. Count all lower case, upper case, digits,
and special symbols from a given string. For e.g. string = 'Py#@th12)ON'
"""

def count_characters():
    string = input("Enter a string: ")
    l = u = d = sy = 0

    for s in string:
        if s.isupper():
            u += 1
        elif s.islower():
            l += 1
        elif s.isdigit():
            d += 1
        else:
            sy += 1

    print(f"Lower case = {l}")
    print(f"upper case = {u}")
    print(f"digits = {d}")
    print(f"special symbols = {sy}")

count_characters()

"""
Q12. Given a string of odd length greater than 7, return a string made
of the middle three chars of a given String. For e.g., str1 = 'Pythonexample'
and str2 = 'trialprograms', the resulting string = 'exarog' (Note: This appears
to combine the middle three letters of both strings, 'exa' and 'rog').
"""

def get_middle_three():
    str1 = input("Enter a string: ")
    
    if len(str1) > 7 and len(str1) % 2 != 0:
        mid = len(str1) // 2
        return str1[mid : mid + 3]
    return "Invalid string length or type"

get_middle_three()


"""
Q13. Find all occurrences of 'sample' in a given string ignoring the case.
For e.g., string = 'This is a SAMPLE program. Solve the sample program'.
"""

def find_all():
    lower_string = input("Enter a string: ").lower()
    lower_target = input("Enter a string: ").lower()

    indices = []
    start = 0
    while True:
        pos = lower_string.find(lower_target, start)
        if pos == -1:
            break
        indices.append(pos)
        start = pos + len(lower_target)

    return indices

find_all()



"""
Q14. Given a string, calculate the occurrences of each character in the string.
For e.g., 'Hello' -> H:1, e:1, l:2, o:1
"""

def count_characters(input_string):
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

s = 'Hello'
result = count_characters(s)
for char, count in result.items():
    print(f"{char}: {count}")


# My Counter practice -
def freq():
    from collections import Counter
    string = input("Enter a string: ")
    frequencies = Counter(string)
    
    for c, f in frequencies.items():
        print(f"{c} = {f}")

freq()