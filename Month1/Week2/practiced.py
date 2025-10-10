# Week 2 - Practice: Data Structures and Functions
# Remove duplicates using set
nums = [1, 2, 2, 3, 4, 4, 5]
unique_nums = list(set(nums))
print("Unique numbers:", unique_nums)

# Sum of squares using list comprehension
numbers = [1, 2, 3, 4]
sum_squares = sum([x**2 for x in numbers])
print("Sum of squares:", sum_squares)

# Filter even numbers using function
def filter_even(num_list):
    return [x for x in num_list if x % 2 == 0]

sample_list = [1, 2, 3, 4, 5, 6]
print("Even numbers:", filter_even(sample_list))
