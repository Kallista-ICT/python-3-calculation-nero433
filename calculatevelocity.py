# asks the user to input the distance and time
distance = float(input("Enter the distance (in meters)): "))
time = float(input("Enter the time (in seconds): "))

# calculates the velocity
velocity = distance / time

#prints the result 
print(f"The velocity is {velocity:.2f} m/s.")