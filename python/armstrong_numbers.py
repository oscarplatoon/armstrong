
def find_armstrong_numbers(numbers):

    result = []

    for value in numbers:
        
    
        to_string = str(value)
        split = list(to_string)
    
        length = len(split)
    
        add_result = 0
    
        for num in split:
            add_result += int(num)**length
    
        if add_result == value:
            result.append(add_result)
    
    return result


#find_armstrong_numbers()