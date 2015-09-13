#!/bin/python

import sys

example_one = 15
expected = 4

def find_count(input_int):
  byte_count = sys.getsizeof(input_int)
  bit_count = byte_count * 8

  one_count = 0
  for i in range(bit_count):
    if (input_int & 1) == 1:
      one_count += 1

    input_int = input_int >> 1

  return one_count

def find_count_while(input_int):

  one_count = 0
  while input_int > 0:
    if (input_int & 1) == 1:
      one_count += 1
    input_int = input_int >> 1

  return one_count

def find_count_division(input_int):
  one_count = 0
  while input_int > 0:
    if (input_int % 2) == 1:
      one_count += 1
    input_int = input_int / 2;

  return one_count

returned = find_count(example_one)
assert expected == returned

returned = find_count_while(example_one)
assert expected == returned

returned = find_count_division(example_one)
assert expected == returned
print 'W00T we passed.'

