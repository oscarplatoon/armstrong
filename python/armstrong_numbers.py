# How can you make this more scalable and reusable later?
def find_armstrong_numbers(numbers):
    answers =[]
    for number in numbers:
        hold_number=number
        sum = 0
        digits = len(str(hold_number))
        for x in range(digits,0,-1):
            value = hold_number // (10 ** (x-1))
            hold_number -= ((10 ** (x-1)) * value)
            sum +=  (value ** digits)
        if(sum == number):
            answers.append(number) 

    return(answers)

