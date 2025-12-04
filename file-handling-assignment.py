# Write a Python program that creates a text file named "output.txt" and writes the string "Hello, Python!" into it.
with open('output.txt', 'w') as f:
    f.write("Hello, Python!")

# Read the contents of "sample.txt" and print it to the console
with open('sample.txt', 'r') as f:
    content = f.read()
    print(content)

# read "word.txt", count the number of words in it, and print the count.
with open('word.txt', 'r') as f:
    content = f.read()
    print(f"number words: {content.split(' ').__len__()}")


# Create a CSV file named "students.csv" with the specified data
data = [
    ["Name", "Roll Number", "Marks"],
    ["Alice", "101", "85"],
    ["Bob", "102", "90"],
    ["Charlie", "103", "88"]
]

with open('students.csv', 'w') as f:
    for row in data:
        f.write(','.join(row) + '\n')

# Write a generator function that reads a file named "500_lines.txt" and yields one line at a time.
def read_file():
    with open('500_lines.txt', 'r') as f:
        for line in f:
            yield line

content = read_file()

for _ in range(100):
    print(next(content).strip())