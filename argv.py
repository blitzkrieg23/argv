import sys

try:
    print("Hello, my name is", sys.argv[1])

except IndexError as e:
    print(e)