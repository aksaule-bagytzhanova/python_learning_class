'''Exercise 1: two-sum

- Declare 2 numbers and calculate their sum
- Print result'''
from sys import flags

number1 = 2
number2 = 4
sum_numbers = number1 + number2
print(number1 + number2)
print(sum_numbers)



'''
Exercise 2: reverse-string
Declare a string
Reverse the string
Print the reversed string
'''

string_normal = "SultanAksaulebestcouple"
s_r = ''.join(reversed(string_normal))
print(s_r)
print(string_normal[::-1])


'''
Exercise 3: string-length
Declare a string
Calculate the length of the string
Print the length
'''

string_len = "SultanAksaulebestcouple"
print(len(string_len))

'''
Exercise 4: concatenate-string
Declare 2 strings
Concatenate the strings
Print the concatenated string
'''
str_1 = "Sultan"
str_2 = "Aksaule"
adding_str = str_1 + str_2

print(adding_str)

'''
Exercise 5: is-vowel
Declare a character
Check if the character is a vowel
Print the result
'''
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
character_1 = 'e'
def is_vowel(char):
    if character_1 in vowels:
        return True
    return False
print(is_vowel(character_1))

'''
Exercise 6: swap-first-last
Declare a string
Swap the first and last characters of the string
Print the modified string'''

sw_string = "Sultan"
swapping_string = sw_string[-1]+sw_string[1:-1]+sw_string[0]
print(swapping_string)


'''
Exercise 7: to-uppercase
Declare a string
Convert the string to uppercase
Print the uppercase string'''

to_up_string = 'sultan'
print(to_up_string.upper())

'''
Exercise 8: rectangle-area
Declare the length and width of a rectangle
Calculate the area of the rectangle
Print the area
'''

rec_len = 5
rec_width = 8
S = rec_len * rec_width
print(f"This is rectangle area {S}")

'''

Exercise 9: is-even
Declare a number
Check if the number is even
Print the result
'''
number_is_even = 6
def is_even(num):
    if num%2 == 0:
        return True
    return False

print(is_even(number_is_even))

'''
Exercise 10: extract-first-three
Declare a string
Extract the first three characters of the string
Print the extracted characters
'''
first_three_str = "sultan"
print(first_three_str[:3])

'''

Exercise 11: string-interpolation
Declare 2 variables, name and age
Use string interpolation to create a message
Print the message
'''
name = "Sultan"
age = 26

print(f'My name is {name} and I am {age} years old')


'''
Exercise 12: string-slicing
Declare a string
Extract the characters from index 2 to 5 (inclusive)
Print the extracted characters


Exercise 13: type-conversion
Declare a number as a string
Convert the string to an integer
Print the integer


Exercise 14: string-repetition
Declare a string
Repeat the string 3 times
Print the repeated string

Exercise 15: calculate-quotient-remainder
Declare 2 numbers
Calculate the quotient and remainder
Print the quotient and remainder


Exercise 16: float-division
Declare 2 numbers
Calculate the result of float division
Print the result


Exercise 17: string-methods
Declare a string
Use a string method to count the occurrences of a character
Print the count


Exercise 18: escape-sequences
Declare a string with double quotes inside
Use escape sequences to include the quotes
Print the string


Exercise 19: multi-line-string
Declare a multi-line string
Print the multi-line string


Exercise 20: exponentiation
Declare 2 numbers, base and exponent
Calculate the result of base to the power of exponent
Print the result

💎 Exercise 21: exponentiation
Declare a palindrome string (A palindrome is a word that is spelled the same forward and backward. ex: "racecar")
Check if it is palindromic without using loops

💎 Exercise 22: check-anagrams
Declare 2 strings
Check if the strings are anagrams (ignoring case)
Print the result

*Anagram - a word, phrase, or name formed by rearranging the letters of another, such as spar, formed from rasp.
'''