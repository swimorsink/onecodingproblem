#!/usr/bin/python2.7

import unittest
from test import test_support

example_one = [5, 1, 14, 28, 55, 3, 22]

def find_sums(input_array):
  running_sum = []
  reversed_sum = []
  final = []
  temp_sum = 0
  for i in input_array:
    temp_sum += i
    running_sum.append(temp_sum)

  temp_sum = 0
  for i in reversed(input_array):
    temp_sum += i
    reversed_sum.append(temp_sum)

  reversed_sum.reverse()
  for i in range(len(input_array)):
    my_sum = 0
    if (i - 1) >= 0:
      my_sum += running_sum[i - 1]

    if (i + 1) < len(input_array):
      my_sum += reversed_sum[i+1]

    final.append(my_sum)

  return final

print find_sums(example_one)

class TestSums(unittest.TestCase):
  def test_one(self):
    ret_array = find_sums(example_one)
    total_sum = sum(example_one)

    for i in range(len(example_one)):
      expected_sum = total_sum - example_one[i]
      self.assertEqual(expected_sum, ret_array[i])

if __name__ == '__main__':
   test_support.run_unittest(TestSums)












