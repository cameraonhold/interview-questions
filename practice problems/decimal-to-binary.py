# This is my solution for AlgoDaily problem Decimal To Binary
# Located at https://algodaily.com/challenges/decimal-to-binary

def decimalToBinary(num):
    ans = ""
    while int(num) >= 1:
      rem = num % 2
      num = num // 2
      ans = str(rem) + ans
    return ans


import unittest


class Test(unittest.TestCase):
    def test_1(self):
        assert decimalToBinary(3) == "11"
        print("PASSED: decimalToBinary(3) should return 11")

    def test_2(self):
        assert decimalToBinary(8) == "1000"
        print("PASSED: decimalToBinary(8) should return 1000")

    def test_3(self):
        assert decimalToBinary(1000) == "1111101000"
        print("PASSED: decimalToBinary(1000) should return 1111101000")

    def test_4(self):
        assert callable(decimalToBinary) == True
        print("PASSED: `decimalToBinary` is a function")


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice job, 4/4 tests passed!")
