# Question 2: Number in Sequence

# Recursive solution

def num_in_seq(n):
    # base case
    if n == 1:
        return 8
    # recursive case
    else:
        return num_in_seq(n-1) + 7

print(num_in_seq(1))
print(num_in_seq(5))
print(num_in_seq(10))

# Non-recursive solution

#def num_in_seq(n):
#    return 8 + (n-1) * 7

#print(num_in_seq(1))
#print(num_in_seq(5))
#print(num_in_seq(10))