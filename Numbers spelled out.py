def dict_of_numbers():
    # Define dictionaries for numbers 0-19 and multiples of 10
    ones = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen'
    }

    tens = {
        2: 'twenty',
        3: 'thirty',
        4: 'forty',
        5: 'fifty',
        6: 'sixty',
        7: 'seventy',
        8: 'eighty',
        9: 'ninety'
    }

    # Initialize an empty dictionary to store the result
    numbers_dict = {}

    for num in range(100):
        if num < 20:
            numbers_dict[num] = ones[num]
        else:
            tens_digit = num // 10
            ones_digit = num % 10

            if ones_digit == 0:
                numbers_dict[num] = tens[tens_digit]
            else:
                numbers_dict[num] = tens[tens_digit] + '-' + ones[ones_digit]

    return numbers_dict

# Usage example:
numbers = dict_of_numbers()
print(numbers[2])    # Output: "two"
print(numbers[11])   # Output: "eleven"
print(numbers[45])   # Output: "forty-five"
print(numbers[99])   # Output: "ninety-nine"
print(numbers[0])    # Output: "zero"
