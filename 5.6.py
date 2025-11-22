###
# Calculates the sum of even numbers from 1 to a given number N
#
N = 116
sum_even = 0
runs = 0 

# Calculate the sum of even numbers
while runs < N:
    runs += 1
    if runs %2 == 0:
        sum_even += runs 
        
print(f"The sum of even numbers from 1 to {N} is: {sum_even}")