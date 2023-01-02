import os, time, brickpi3

# Initialize the EV3 Brick
BP = brickpi3.BrickPi3()

# Initialize EV3 infrared remote sensor
# Set the red slider to the top position
BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.EV3_INFRARED_REMOTE)

# Without a delay reading sensor data can cause an error
time.sleep(0.5)

# Quite loop when CTRL+C is pressed
try:

    # Create a loop to react to buttons
    while True:

        try:

            # Retrieve the current sensor data
            distance = BP.get_sensor(BP.PORT_1)

            # Retrieve data from channel one
            channel = distance[0]

            # Output all channel one data
            print(
                "Red Up: " + str(channel[0]) + " " + 
                "Red Down: " + str(channel[1]) + " " + 
                "Blue Up: " + str(channel[2]) + " " + 
                "Blue Down: " + str(channel[3]) + " " + 
                "Toggle: " + str(channel[4])
            )

            # Turn motor clockwise if red up is pressed
            if channel[0] == 1:

                BP.set_motor_power(BP.PORT_B, 100)

            # Turn motor counter clockwise if red down is pressed
            elif channel[1] == 1:

                BP.set_motor_power(BP.PORT_B, -100)

            # Turn motors off if neither are pressed
            else:

                BP.set_motor_power(BP.PORT_B, 0)


        except brickpi3.SensorError as error:
            
            print(error)

        # Loop delay
        time.sleep(0.5)

# Result of CTRL+C
except KeyboardInterrupt:
    
    # Unconfigure the sensors
    BP.reset_all() 