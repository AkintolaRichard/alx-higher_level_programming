#!/usr/bin/python3
for i in range(9):
    for j in range(i + 1, 10):
        if (i == 0 and j == i + 1):
            print(f"{i}{j}", end="")
        else:
            print(f", {i}{j}", end="")
print()
