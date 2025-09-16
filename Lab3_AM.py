import math
# Function 1 (30): Convert the given polar coordinates (r,θ) to Cartesian coordinates (x,y). 
# This function should take the polar coordinates (r,θ) and return Cartesian coordinates (x,y).
def polar_to_cartesian(r, theta):     #Function 1
    x = r*math.cos(math.radians(theta))    #Calculation to convert r into x
    y = r*math.sin(math.radians(theta))      #Calculation to convert theta into y
    return (round(x,5), round(y,5))          #Rounding to 5 decimal points

print("Question 1: Polar to Cartesian Coordinate")
r = float(input("Enter distance (r) value: "))      
theta = float((input("Enter angle theta (degrees): ")))        #Degrees because it gets converted into radians by the function above
print("Cartesian coordinates are " + str(polar_to_cartesian(r, theta)))

# Function 2(30): Convert Cartesian coordinates (x,y) to polar coordinates (r,θ).
# This function should take the Cartesian coordinates (x,y) as input and return the polar coordinates (r,θ).
def cartesian_to_polar(x, y):
    r = math.sqrt(x**2 + y**2)
    theta = math.degrees(math.atan(y/x))
    return (round(r,5), round(theta,5))         #rounding to 5 decimal points

print("Question 2: Cartesian to Polar Coordinate")
x = float(input("What is your x value: "))
y = float(input("What is your y value: "))
print("Your polar coordinates are " + str(cartesian_to_polar(x, y)))

# Function 3 (40): Calculate the position of pendulum for (A, f, ϕ, t).
# This function should take (A, f, ϕ, t) as input and return the position value x.
def pendulum_position(A, f, phi, t):
    position = A*math.cos(2*math.pi*f*t + math.radians(phi))         #SHM position function with cosine
    return position

print("Question 3: Position during Oscillatory motion")
A = float(input("What is your Amplitude (m): "))
f = float(input("What is your frequency (Hz): "))
phi = float(input("What is your phase constant (degrees): "))      #Degrees get converted into radians in the function
t = float(input("What is your time (s): "))
print("Your position is " + str(pendulum_position(A, f, phi, t)))