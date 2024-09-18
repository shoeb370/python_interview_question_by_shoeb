array = [0, 1, 1, 2, 2, 3, 3]
i = 0

while i < len(array) - 1:
    if array[i] == array[i + 1]:
        del array[i + 1]  # Remove the duplicate element
    else:
        i += 1  # Move to the next element if no duplicate is found

print(array)  # Output: [0, 1, 2, 3]
