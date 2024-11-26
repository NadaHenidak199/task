while True:
    str_steps = input("Enter  the number of steps taken each day in the month as numbers separated by spaces: ").split()
    if len(str_steps) != 5:
        print("Enter 30 values")
        continue
    try:
        steps = list(map(int , str_steps))
    except ValueError:
        print("ُError: Enter only numbers.")
    else:
        break
max_steps = max(steps)
min_steps = min(steps)
avg_steps = (sum(steps) / 30)
sorted_steps = sorted(steps, reverse=True)
print( steps)
print("Max: " ,  max_steps)
print("Min: " ,  min_steps)
print("Average: " ,  avg_steps)
print("sorted list: " ,  sorted_steps)