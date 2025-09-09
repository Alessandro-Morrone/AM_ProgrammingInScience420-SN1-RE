# Function 1: Calculate the height of the ball after time t
# This function should take the initial height h0 and time t as inputs, and return the height at time t.
def calculate_height(h0, t):
    g = 9.8                    #gravitational constant
    result = h0-(0.5*g*t**2)   #height function to calculate
    return result    

print("Question 1")
h0 = float(input("Enter Initial Height: "))      #user imputs their intiial height
t = float(input("Enter Time: "))                 #user imputs their time
print("Height of the ball at time " + str(t) + " seconds = " + str(calculate_height(h0, t)) + " meters")         #Output message for Question 1 Function answer

# Function 2: Calculate the distance traveled by the car
# This function should take the time t as input and return the distance traveled by the car.
def calculate_car_distance(t):
    speed = 20                   #Constant given value in this question
    result = speed*time          #Distance function to calculate
    return result

print("Question 2")
time = float(input("Enter time for car (in seconds): "))             #User imputs their time
print("The car will travel " + str(calculate_car_distance(t)) + " meters in " + str(time) + " seconds.")              #Output message for Question 2 function answer

calculate_height(h0, t)              #Call Height Function
calculate_car_distance(time)          #Call distance Function