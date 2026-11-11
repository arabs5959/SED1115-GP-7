from machine import PWM, Pin, ADC
import math
import time

#Arm length


#Set up the pins for the knobs to controll the arm
x_axis =
y_axis =



#PWM for shoulder and elbow servos



# Set PWM frequency for arm



# min and max duty cycles


#FUNctions :)
#Saftey functions for duty and angle conversions
def safe_duty(servo, duty):
#Make sure the angle is within the range of 0 to 180 degrees
    if D_MIN <= duty <= D_MAX:
         servo.duty_u16(duty)
    else:
        return
#Make sure angle set safe
def safe_angle(servo, angle):
    if 0 <= angle <= 180:
        duty = translate(angle)
        safe_duty(servo, duty)

###############################
def inverse_kinematics(x_cord, y_cord):
   
    distance = 
    #make sure the targets in reach
    if  (distance > (L1 + L2) or distance < abs(L1 - L2)):
            return None, None
    else:
    #calculate elbow angle (theta2)
    
    #calculate shoulder angle (theta1)

        return (theta1), (theta2)
##########################################
def translate(angle: float) -> int:

################
def read_knobs():

    
    
     return x_value, y_value
################Set up pen control (up and down)

##########
def pen_control():

     last_pen_button_state = current_pen_button_state
######################################################33
def ITS_ALIVE():
    print("The robot arm is alive and ready to move!")
    #Gets the intial values of the knobs and converts them to x and y coordinates
    x_value, y_value = read_knobs()

    #mapping the values in the range (1, 300(total arm length)) 
    x_cord = (x_value / 65535) * (2 * (L1 + L2)) - (L1 + L2)
    y_cord = (y_value / 65535) * (2 * (L1 + L2)) - (L1 + L2)

    #Ugly math
    theta1, theta2 = inverse_kinematics(x_cord, y_cord)
    if theta1 is None or theta2 is None:
        return

    safe_angle()
    safe_angle()

    #PEN!
    pen_control()  # Set the initial pen state


def main():
    """Main entry point to run the robotic arm control."""


if __name__ == "__main__": #The things ai just kinda added this for me, but it works so I guess its fine.
    main()