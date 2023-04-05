load_file_in_context('script.py')
try:
  zero_to_seven
  if type(zero_to_seven) is not range:
    fail_tests("Did you define `zero_to_seven` as a `range`?")
  if zero_to_seven.start != 0:
    fail_tests("Does the `zero_to_seven` range start at 0?")
  if zero_to_seven.stop != 8:
    fail_tests("Does the `zero_to_seven` range end at 7?")
except NameError:
  fail_tests("Did you define `zero_to_seven`?")
pass_tests()
