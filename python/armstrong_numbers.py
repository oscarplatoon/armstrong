# 371
def find_armstrong_numbers(numbers):
	answer = []

	for num in numbers:
		exponent = len(str(num)) # = 3
		sum = 0
		temp = num 
		while temp > 0:
			digit = temp % 10 # = 1, 7
			sum += digit ** exponent
			temp //= 10
		if num == sum:
			answer.append(num)
	return answer

print(find_armstrong_numbers(list(range(0, 999))))