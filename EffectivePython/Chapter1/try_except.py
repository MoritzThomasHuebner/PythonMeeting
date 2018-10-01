handle = open('example.txt')  # May raise IOError
try:
    data = handle.read()  # May raise UnicodeDecodeError
except UnicodeDecodeError:
    pass  # Do something else
else:
    it = (float(x) for x in open('example.txt'))
finally:
    handle.close()        # Always runs after try:


with open('example.txt') as f:
    it = (float(x) for x in open('example.txt'))