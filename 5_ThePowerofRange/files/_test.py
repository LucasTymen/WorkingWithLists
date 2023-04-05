load_file_in_context('script.py')
try:
  range_five_three
  if type(range_five_three) is not range:
    fail_tests("Did you define `range_five_three` as a `range`?")
  if range_five_three.start != 5:
    fail_tests("Does the `range_five_three` range start at 5?")
  if range_five_three.stop != 15:
    fail_tests("Does the `range_five_three` range end before 15?")
  if range_five_three.step != 3:
    fail_tests("Does the `range_five_three` range go by steps of 3?")
except NameError:
  fail_tests("Did you define `range_five_three`?")
pass_tests()
