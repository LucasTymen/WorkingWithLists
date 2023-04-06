load_file_in_context('script.py')
try:
  addresses
except NameError:
  fail_tests("Did you leave `addresses` defined?")
full_equality('addresses', sorted(addresses))
pass_tests()
