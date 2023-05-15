from typing import Optional


# Task 1
# design Recipe:
# 1) convert a string to a float if possible. If not return none
# 2) str_to_float(s: str)->Optional[float]:
# 3) template of function
#     - use try to see if the string can be made into a float if it can then return the float
#     - if the string cant be made into a float then return none
# 4) test case:         def test_str_to_float_2(self):
#                           words = '3 s2t8'
#                           assert convert.str_to_float(words) == None
# 5)


def str_to_float(s: str) -> Optional[float]:
    try:
        new_s = float(s)
        return new_s
    except ValueError:
        return None
