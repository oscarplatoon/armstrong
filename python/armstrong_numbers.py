# How can you make this more scalable and reusable later?

# ----- PSUDOCODE -----
# Write a FUNCTION/METHOD that takes in an argument that is a RANGE OF NUMBERS
# creat an ANSWER variable that is an array
# ITERATE/LOOP through the range of number (num)
# create a variable called EXPONENT and have it equal to the length of the string number
# create a variable called SUM and have it's initial value = 0
# create a TEMP variable that stores a number to extract each individual integer from the number inital value is NUM
# create a WHILE LOOP where TEMP is GREATER THAN 0
# find the remainder of the the TEMP variable by using MODULUS 10 to get the last integer and store that into a variable called DIGIT
# take the DIGIT variable and take to the power of the EXPONENT variable and ADD to the SUM
# reassing the TEMP variable ot the floor of the TEMP DIVIDED BY 10
#  write an IF STATEMENT that checks if NUM is equal to SUM and if it's true add it to the ANSWER array

def find_armstrong_numbers(numbers):
  answer = []
  for num in numbers:
    exponent = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
      digit = temp % 10
      sum += digit ** exponent
      temp //= 10
    if num == sum:
      answer.append(num)
  return answer
