from random import *
import math

# Ask the user for the number of elements and create an array of random integers from -45 to 45
n = int(input("Enter the number of elements in the array: "))
A = [randint(-45, 45) for _ in range(n)]
print(*A, sep=' ')

# Extract a subarray from index 4 to 20 (inclusive), but not beyond the first half of the array
subset = A[4:min(21, len(A)//2)]

# If the subarray is not empty, calculate the root mean square (RMS) of its elements
if subset:
    S = math.sqrt(sum(x**2 for x in subset) / len(subset))
    print(f"Root mean square of elements [4;20] in the first half of the array: {S}")
else:
    print("No elements with indices from 4 to 20 in the first half of the array")

# Ask for a number d and find the elements in the subarray closest to it
d = int(input("Enter the number d: "))

if subset:
    minDiff = min(abs(n - d) for n in subset)  # Find the minimum difference
    val = [n for n in subset if abs(n - d) == minDiff]  # All values with the minimum difference
    ind = [i for i in range(4, min(21, len(A)//2)) if A[i] in val]  # Indices of those values in the original array

    print("Indices of elements closest to d in the original array:")
    print(*ind, sep=' ')
    print("Values of elements closest to d:")
    print(*val, sep=' ')
else:
    print("No elements to compare in the given range")

# Extract the first third of the array
firstThird = A[:len(A)//3]
print("First third of the array:")
print(*firstThird, sep=' ')

# Filter even numbers and sort them in descending order by absolute value
evenNum = [x for x in firstThird if x % 2 == 0]
sortedEven = sorted(evenNum, key=abs, reverse=True)

if sortedEven:
    print("Even elements of the first third sorted by descending absolute value:")
    print(*sortedEven, sep=' ')
else:
    print("No even elements in the first third of the array.")
