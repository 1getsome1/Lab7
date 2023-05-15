import sys
# Task 3
# design Recipe:
# 1) make a function that processes command-line arguments by converting each into a float
# 2) command()
# 3) template of function
#     - make a sum variable and give the value 0
#     - cycle through the command-line arguments
#     - try making the argument into a float
#     - if the argument cant become a float then continue through the cycle
#     - add the argument turned into float into the sum variable
# 4) test case:
# 5)

def command():
    sum = 0
    for x in sys.argv[1:]:
        try:
            f_arg = float(x)
        except ValueError:
            continue
        sum += f_arg
    print(sum)

if __name__ == '__main__':
    command()