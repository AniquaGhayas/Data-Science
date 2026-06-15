# H. Read Data and Write Data from a Text File
filename = "sample_data.txt"

# Writing to a file
file = open(filename, "w")
file.write("Hello, welcome to the Data Science Lab.\n")
file.write("Python is the primary language used here.\n")
file.close()

print("--- File created successfully. ---")