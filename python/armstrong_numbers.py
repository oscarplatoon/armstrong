 # How can you make this more scalable and reusable later?
def find_armstrong_numbers(numbers):
    armstrong_array = []

    for x in range(len(numbers)):
        numbers_string = str(x)
        numbers_list = list(numbers_string)
        numbers_array = []

        for num in numbers_list:
            numbers_array.append(int(num))

        sum_of_digits = 0

        for digit in numbers_array:
            sum_of_digits += digit ** len(numbers_array)

        if x == sum_of_digits:
            armstrong_array.append(x)

    return armstrong_array