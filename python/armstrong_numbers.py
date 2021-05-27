# How can you make this more scalable and reusable later?
def find_armstrong_numbers(numbers):
    #all single nums as edge case
    #armstrong is 0, 1, 153, 370, 407
    results = []
    for i in range(numbers + 1):
        number_of_digits = len(str(i))
        #list of digits i.e 1, 3, 7
        num_to_string = list(str(i))
        sum = 0
        for count in num_to_string:
            sum += int(count) ** number_of_digits
        if sum == i:
            results.append(i)
    return results
            
