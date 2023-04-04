load_file_in_context('script.py')
try:
  front_display_list
  if type(front_display_list) is not list:
    fail_tests("Did you keep`front_display_list` defined as a `list`?")
  if front_display_list != ["Pineapple", "Mango", "Filet Mignon", "Chocolate Milk"]:
    fail_tests('Did you add `"Pineapple"` to the front of the list?')
except NameError:
  fail_tests("Did you define `front_display_list`?")
pass_tests()
