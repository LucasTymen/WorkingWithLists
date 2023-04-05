load_file_in_context('script.py')
try:
  list1
  if type(list1) is not range:
    fail_tests("Did you define `list1` as a `range`?")
  if list1.step != 3:
    fail_tests("Does the `list1` range go by steps of 3?")
except NameError:
  fail_tests("Did you define `list1`?")
pass_tests()
