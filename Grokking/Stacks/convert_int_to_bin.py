import unittest

class Test(unittest.TestCase):
    def test_case(self):
        self.assertEqual(convert_int_to_bin(39), "100111")



def convert_int_to_bin(decimal: int):
    binary = ""
    my_stack = []

    while decimal > 0:
        remainder = decimal % 2
        my_stack.append(remainder)
        decimal = decimal // 2

    while my_stack:
        binary += str(my_stack.pop())
    # for element in my_stack:
    #     binary += str(my_stack.pop())
    return binary

if __name__ == "__main__":
    unittest.main()