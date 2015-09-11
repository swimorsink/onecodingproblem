#!/bin/python

example_one = [1,5,15,-5,-6,-5,15]
expected = [1,5,15,-5,-6]
expected.sort()

def part_one(input_array):
  seen = {}
  for i in input_array:
    seen[i] = True
  return seen.keys()

def part_two(input_array):
  output_array = []
  curr = None
  for i in input_array:
    if i not in output_array:
      output_array.append(i)
  return output_array

def part_three(input_array):
  input_array.sort()
  output_array = []
  prev = input_array[0]
  output_array.append(prev)
  for i in input_array[1:]:
    if i != prev:
      output_array.append(i)
      prev = i

  return output_array

def part_four(input_array):
  input_array.sort()
  insert_point = 1
  temp = input_array[0]
  for i in input_array[1:]:
    if i != temp:
      input_array[insert_point] = i
      temp = i
      insert_point += 1

  return input_array[0:insert_point]



returned = part_one(example_one)
returned.sort()
assert returned == expected

returned = part_two(example_one)
returned.sort()
assert returned == expected

returned = part_three(example_one)
assert returned == expected

returned = part_four(example_one)
assert returned == expected


print 'W00T we passed.'
