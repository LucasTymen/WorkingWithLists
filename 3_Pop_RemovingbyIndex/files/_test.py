# if (!Components.CodeEditor.codeContains('script.py', /data_science_topics\s*\.\s*pop\s*\(.*\)/)) {
#   return createErr('Did you call the `.pop()` method? on `data_science_topics`');
# }

load_file_in_context("script.py")

try:
	data_science_topics
except NameError:
  fail_tests("Expected `data_science_topics` to be defined.")

if data_science_topics != ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics"]:
	fail_tests('Did you remove `"Python 3"` from `data_science_topics`')

pass_tests()
