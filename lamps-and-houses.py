# This is my solution for AlgoDaily problem Lamps and Houses
# Located at https://algodaily.com/challenges/lamps-and-houses

import math


def get_radius(houses, lamps):
  i = 0
  find_dist = [0] * (len(houses) * len(lamps))
  if len(houses) > len(lamps):
    for lamp in lamps:
      for house in houses:
        find_dist[i] = abs(house-lamp)
        i += 1
    if len(lamps) > 1:
      radius = max(find_dist[len(houses):])
    else:
      radius = max(find_dist)
  #else:
    #for x in range(len(houses)):
    #  print(i,"here2")
    #  i+=1
    #radius = abs(max(houses) - max(lamps))
    return radius


import unittest


class Test(unittest.TestCase):
    def test_1(self):
        assert get_radius([1, 2, 3], [2]) == 1
        print("PASSED: Expect get_radius([1,2,3],[2]) to return 1")

    def test_2(self):
        assert get_radius([2, 3, 8], [2]) == 6
        print("PASSED: Expect get_radius([2,3, 8], [2]) to return 6")

    def test_3(self):
        assert get_radius([1, 3, 4], [0, 2]) == 2
        print("PASSED: Expect get_radius([1,3, 4], [0, 2]) to return 2")


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice job, 3/3 tests passed!")
