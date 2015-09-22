
example_one = '1??'
example_two = '1011?11??1?'
example_three = '???'

example_one = '101???'

def compute_perms(in_string):
  index = in_string.find('?')
  if index < 0:
    return [in_string]

  branch1 = [(in_string[:index] + '0' + '{0}').format(i) for i in compute_perms(in_string[index+1:])]
  branch2 = [(in_string[:index] + '1' + '{0}').format(i) for i in compute_perms(in_string[index+1:])]
  return branch1 + branch2

def compute_perms_iterative(in_string):
  result_set = []
  result_set.append('')
  for index,c in enumerate(in_string):
    if c == '?':
      result_set *= 2
      for i in range(len(result_set)):
        if i < len(result_set) / 2:
          result_set[i] += '0'
        else:
          result_set[i] += '1'
    else:
      for i in range(len(result_set)):
        result_set[i] += c


def check_result(results, input_str):
  print results
  question_mark_count = input_str.count('?')
  assert len(results) == 2 ** question_mark_count

check_result(compute_perms(example_one), example_one)
check_result(compute_perms(example_two), example_two)
check_result(compute_perms(example_three), example_three)

compute_perms_iterative(example_one)
print 'W00t We Passed!'



