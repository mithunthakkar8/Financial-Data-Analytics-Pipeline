import sys

# check if the current environment is a virtual environment
print(sys.prefix)
print(sys.prefix != sys.base_prefix)
print(sys.executable)


