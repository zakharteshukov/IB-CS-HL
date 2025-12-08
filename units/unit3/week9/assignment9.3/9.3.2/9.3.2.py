# ---- INPUT SET (10 numbers) ----
numbers = [15, -2, 0, 8, 0, 21, -8, -12, 1, 25 ]

print("Count\tNumber\tTotal\tX\tAverage\tOutput Average")

# ---- INITIAL VALUES ----
count = 1
total = 0
X = 0

# ---- PROCESS LOOP ----
for i in range(10):
    number = numbers[i]

    if number > 0:
        total = total + number
        X = X + 1
    
    # Calculate average
    if X > 0:
        average = total / X
    else:
        average = 0
    
    # Print trace row for this iteration
    output_avg = "-" if count <= 10 else average
    print(f"{count}\t{number}\t{total}\t{X}\t{average:.1f}\t{output_avg}")
    
    count = count + 1

# ---- FINAL OUTPUT ----
if X > 0:
    final_average = total / X
else:
    final_average = 0

# Print final output row
print(f"{count}\t-\t{total}\t{X}\t{final_average:.1f}\t{final_average:.1f}")
