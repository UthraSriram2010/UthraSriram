def integer_number(number):
    even_numbers = []
    odd_numbers = []
    for num in number:
        if num%2 == 0:
            even_numbers.append(num**2)
        else:
            odd_numbers.append(num)
    return even_numbers, odd_numbers
number=[1,2,3,4,5,-3,-6,-9,-10]
print(integer_number(number))