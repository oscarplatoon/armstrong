# How can you make this more scalable and reusable later?

#Write a function/method that takes in RANGE OF NUMBERS:
#Return an answer_list that is an array
#Iterate through the RANGE OF NUMBERS
# Create variable called EXPONENT that stores the length of the String number
# Create a variable called SUM that initial value = 0
# Create a TEMP variable that stores a number to extract each individual integer from the number
# Create a WHILE LOOP where Temp >= 0
# Find the remainder of the TEMP variable by using Modulus % 10 to get the last integer and store that into a variable called DIGIT
# Take DIGIT and add it to the SUM
# Reassign TEMP to the floor of the TEMP DIVIDED BY 10
# Write an IF STATEMENT that compares the SUM against NUM and if true append to the answer_list



def find_armstrong_numbers(numbers):
  answer = []
  for num in numbers:
    exponent = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
      digit = temp % 10
      sum += digit**exponent
      temp //= 10
    if num == sum:
      answer.append(num)
  return answer