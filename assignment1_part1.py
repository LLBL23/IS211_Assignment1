# -*- coding: utf-8 -*-
def list_divide(numbers, divide=2):
    """
    The function returns the number of elements in the numbers list that are divisibleby divide
    """
    items = [x for x in numbers if x % divide == 0]
    return len(items)

class ListDivideException(Exception):
    """
    Raise List Divide Exception
    """
    pass

def test_list_divide():
    """
    Test listDivide
    """
    listDivide = [([1,2,3,4,5]), 2, 2,
                  ([2,4,6,8,10]),2, 5,
                  ([30, 54, 63,98, 100], 10), 2,
                  ([]), 2, 0,
                  ([1,2,3,4,5], 1), 2, 5]

    for nums, div, res in listDivide:
        comp = list_divide(nums, div)
        if comp != res:
            raise ListDivideException()



if __name__ == "__main__":
    print (test_list_divide())
