# python-practice
# commands
- pip list  # list all installed modules
- pip freeze > req.txt # copy all installed modules to req.txt file

1. Python print statement. Print vs Return
A: - Python Print is similar to echo in shell script
   - Python print dont return any value
   - Python return is used to return a value from a function

* python is a dynamically typed language

Python has the following data types built-in by default, in these categories:

  Text Type:	str
  Numeric Types:	int, float, complex
  Sequence Types:	list, tuple, range
  Mapping Type:	dict
  Set Types:	set, frozenset
  Boolean Type:	bool
  Binary Types:	bytes, bytearray, memoryview
  None Type:	NoneType

understanding python strings and fstrings.
  str.upper()
  str.lower()
  str.title()
  str.capitalize()
  str.split()
  str.rsplit(separate,maxsplit)
  info2.strip()

'wlecome-to-python-training-in-telugu'
>>> info2.strip().replace("-", " ")
'wlecome to python training in telugu'
>>> info2.strip().replace("-", "&&")
'wlecome&&to&&python&&training&&in&&telugu'
info2 = "welcome to python training in telugu"
   info2.count("to")
   info2.find("telugu)

# Using python Fstrings
  - f"Hello {name}, welcome to {place}"
  - f"Hello {name.upper()}, welcome to {place.lower()}"