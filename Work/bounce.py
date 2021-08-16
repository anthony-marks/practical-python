# bounce.py
#
# Exercise 1.5
REBOUND = 3/5        # how much it bounces back
NUMBER_BOUNCES = 10  # number of bounces we measure
height = 100         # initial height in metres

bounce_count = 1
while bounce_count <= NUMBER_BOUNCES:
    height = height * REBOUND
    print(bounce_count, round(height, 4))
    bounce_count = bounce_count + 1



