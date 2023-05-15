import convert


# Task 2
# design Recipe:
# 1) use str_to_float function to make a list of inputted numbers and stop when "done" is inputted
# 2) gather_numbers()->list[float]
# 3) template of function
#     - make an empty list
#     - make the input into the variable i
#     - make while loop that continues as long as i isnt equal to "done"
#     - make a new variable that is the variable i when put through the str_to_float function
#     - if the new variable was able to go through the function then append it to the empty list
# 4) test case:
# 5)

def gather_numbers() -> list[float]:
    nums = []
    while True:
        i = input("?")
        if i.lower() == 'done':
            break
        number = convert.str_to_float(i)
        if number is not None:
            nums.append(number)
    return nums

if __name__ == '__main__':
    numbers = gather_numbers()
    print(sum(numbers))
