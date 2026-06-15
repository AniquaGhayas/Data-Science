# Program to find the average of numbers and trace execution variables
print("--- Debugging Demonstration ---")

numbers_list = [10, 20, 30, 40, 50]

total_sum = 0
count = 0

for num in numbers_list:
    total_sum = total_sum + num
    count = count + 1

    # IDE DEBUGGING TIP: 
    # You can uncomment the line below to trigger the interactive debugger loop.
    # breakpoint() 
    
    print("Loop Step - Item:", num, "| Running Sum:", total_sum, "| Count:", count)

# Calculating final value
average = total_sum / count

print()
print("Final Total Sum:", total_sum)
print("Final Element Count:", count)
print("Calculated Average:", average)