"""Python functions for JavaScript Trials 1."""

def output_all_items(items):
    for item in items:
        print(item)

output_all_items([1, 'hello', True])


def get_all_evens(nums):
    even_nums = []
    for num in nums: 
        if num % 2 == 0: 
            even_nums.append(num)
    return even_nums

nums = [7, 8, 10, 1, 2, 2]
print(get_all_evens(nums))


def get_odd_indices(items):
    result = []

    for index in range(len(items)):
        if index % 2 != 0:
            result.append(items[index])    

    return result

print(get_odd_indices([1, 'hello', True, 500]))


def print_as_numbered_list(items):
    for index, item in enumerate(items): 
        print (f"{index+1}. {item}")

print_as_numbered_list([1, 'hello', True])


def get_range(start, stop):
    nums = []

    for number in range(start, stop):
        nums.append(number)

    return nums

print(get_range(0, 5))           


def censor_vowels(word):
    chars = []
    for letter in word: 
        if letter in 'aeiou': 
            chars.append('*')
        else: 
            chars.append(letter)

    return ('').join(chars)
    
print(censor_vowels('hello world!'))


def snake_to_camel(string):
    
    camel_case = []

    words = string.split('_')
    for word in words:
        camel_case.append(f"{word[0].upper()}{word[1:]}") 

    return (' ').join(camel_case)

print(snake_to_camel('hello_world'))


def longest_word_length(words):
    longest = len(words[0])

    for word in words:
        if longest < len(word):
            longest = len(word)

    return longest

print(longest_word_length(['jellyfish', 'zebra']))


def truncate(string):
    result = []

    for char in string:
        if len(result) == 0 or char != result[len(result) - 1]:
            result.append(char)

    return ('').join(result)        

print(truncate('hi***!!!! wooow'))

def has_balanced_parens(string):
    parens = 0

    for char in string:
        if (char == '('):
            parens = parens + 1 
        elif (char == ')'):
            parens = parens - 1

            if parens < 0:
                return False 

    return parens == 0            

print(has_balanced_parens('(Oh no!)('))

def compress(string):
    compressed = []

    curr_char = ''
    char_count = 0

    for char in string:
        if char != curr_char:
            compressed.append(curr_char)

            if(char_count > 1):
                compressed.append(str(char_count))

            curr_char = char
            char_count = 0  

        char_count = char_count + 1
    compressed.append(curr_char)
    
    if char_count > 1:
        compressed.append(str(char_count))

    return ('').join(compressed)              

print(compress('Hello, world! Cows go moooo...'))    