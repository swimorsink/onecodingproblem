#!/bin/python

def do_division(dividend, divisor):
  temp_sum = divisor
  quotient = 0
  while temp_sum <= dividend:
    quotient += 1
    temp_sum += divisor

  return quotient


def do_minimum_division(dividend, divisor):
  temp_sum = divisor
  squares = 0
  quotient = 0
  prev = 0
  while temp_sum <= dividend:
    squares += 1
    prev = temp_sum
    temp_sum += temp_sum

  if squares > 0:
    quotient += (2 ** (squares - 1))

  prev += divisor
  while prev <= dividend:
    quotient += 1
    prev += divisor

  return quotient

assert do_division(2, 5) == 0
assert do_division(5, 2) == 2
assert do_division(9, 4) == 2
assert do_division(9, 2) == 4
assert do_division(8, 2) == 4

assert do_minimum_division(2, 5) == 0
assert do_minimum_division(15, 4) == 3
assert do_minimum_division(9, 2) == 4
assert do_minimum_division(15, 8) == 1
assert do_minimum_division(64, 8) == 8
assert do_minimum_division(17, 3) == 5
assert do_minimum_division(4, 2) == 2
print 'W00T we passed!'

