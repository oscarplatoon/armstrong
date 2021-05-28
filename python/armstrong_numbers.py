# How can you make this more scalable and reusable later?
def find_armstrong_numbers(numbers_list):
    counter = len(numbers_list)
    answer_list = []
    # while loop over over argument
    while counter > 0:
        powered_list = []
        separated_numbers = [int(x) for x in str(numbers_list[counter - 1])]
    
        # multiply each split number by the length of the orginal num
        # then append it to a new list
        for num in separated_numbers:
            powered_list.append(num * len(separated_numbers))
        
        # sum up the multiplied new list into a new variable
        powered_sum = 0
        for powered in powered_list:
            powered_sum += powered

        #compare if powered_sum == counter, if so push it to answer list
        if powered_sum == numbers_list[counter - 1]:
            answer_list.append(counter)

        # decriment counter
        counter -= 1

    if numbers_list == [0]:
        return [0]
    return sorted(answer_list)
        
print(find_armstrong_numbers(list(range(0, 8))))