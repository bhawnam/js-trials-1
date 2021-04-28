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

# function snakeToCamel(string) {
#   const camelCase = [];

#   for (const word of string.split('_')) {
#     camelCase.push(`${word[0].toUpperCase()}${word.slice(1)}`);
#   }

#   return camelCase.join('');
# }

#def snake_to_camel(string):
    # camel_case = []

    # words = string.split('_')
    
    
    # for word in words:
        
    #     camel_case.append(word[0].upper())
    #     else: 



    # print(('').join(camel_case))

#snake_to_camel('hello_world')

def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code


# word = 'Hello Word'
# words = word.split('_')
# print (words)
# for i in words:
#     for n in i: 
#         print(n)