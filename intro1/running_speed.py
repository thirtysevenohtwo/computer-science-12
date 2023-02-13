import input_ecc as ecc

distance = ecc.try_in("What is the distance you ran in kilometers?\n>| ", "float")
time_taken = ecc.try_in("How many hours did it take you to run " + str(distance) + "km?\n>| ", "float")

speed = str(round(distance / time_taken, 3)) + "km/h"

print("You ran " + str(distance) + "km in " + str(time_taken) + " hours, at an average speed of " + speed)
