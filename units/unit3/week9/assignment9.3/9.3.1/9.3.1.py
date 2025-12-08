# Trace table for the flowchart algorithm
# Input data: 15, 8, 251, 35, 60, 3, 2, 1516, 19, 55

numbers = [15, 8, 251, 35, 60, 3, 2, 1516, 19, 55]

# Initialize variables
S = 0
C = 1

# Print header
print("S\tC\tN\tT\tOutput")
print("-" * 40)

# Process each input value
for i in range(10):
    N = numbers[i]
    T = N / 100
    
    # Check conditions and update S if needed
    if T < 1:
        if T >= 0.1:
            S = S + 1
    
    # Print trace row for this iteration
    # Output column shows "-" during iterations, final S value only after loop
    output = "-"
    print(f"{S}\t{C}\t{N}\t{T:.2f}\t{output}")
    
    # Increment C
    C = C + 1

# Print final output row
print(f"{S}\t{C}\t-\t-\t{S}")
