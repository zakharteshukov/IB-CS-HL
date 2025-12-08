# Input data (must include the terminating -1)
temps = [75, 78, 84, 87, 91, 80, 75, 70, 65, 62, -1, 20]

print("Counter\tHot\tCold\tServe\tTemp\tError\tOutput")

# Initial values
Counter = 0
Hot = 0
Cold = 0
Serve = 0

for Temp in temps:

    # Stop when -1 appears
    if Temp == -1:
        # Compute error safely
        if Counter > 0:
            Error = ((Hot + Cold) / Counter) * 100
        else:
            Error = 0

        print(f"{Counter}\t{Hot}\t{Cold}\t{Serve}\t{Temp}\t{Error:.0f}%\tError")
        break

    # Apply conditions
    if Temp > 86:
        Hot += 1
        Output = "Too Hot"
    elif Temp < 63:
        Cold += 1
        Output = "Too Cold"
    else:
        Serve += 1
        Output = "Serve"

    # Print result of the decision (final state after decision)
    print(f"{Counter}\t{Hot}\t{Cold}\t{Serve}\t{Temp}\t-\t{Output}")

    # Increment count at end of loop
    Counter += 1