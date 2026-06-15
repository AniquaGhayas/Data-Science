filename = "sample_data.txt"# I. Append Data and Count Number of Lines, Words and Characters
file = open(filename, "a")
file.write("Appending a new line for analysis tasks.\n")
file.close()

# Counting metrics
line_count = 0
word_count = 0
char_count = 0

file = open(filename, "r")
for line in file:
    line_count = line_count + 1
    char_count = char_count + len(line)
    word_count = word_count + len(line.split())
file.close()

print("--- File Metrics ---")
print("Total Lines:", line_count)
print("Total Words:", word_count)
print("Total Characters:", char_count)