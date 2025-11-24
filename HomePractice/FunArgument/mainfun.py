
import sys

squares = []
for arg in sys.argv[1:]:
    squares.append(int(arg) ** 2)

print(squares)