from machine import PWM, Pin, ADC
import math
import time

#Arm length
L1 =
L2 =

#Set up the pins for the knobs to controll the arm
x_axis =
y_axis =



#PWM for shoulder and elbow servos
shoulder_pwm = 
elbow_pwm = 

# Set PWM frequency for arm



# min and max duty cycles
D_MIN =
D_MAX =
PEN_UP =
PEN_DOWN =



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
   
    distance = math.sqrt(x_cord**2 + y_cord**2)
    #make sure the targets in reach
    if  (distance > (L1 + L2) or distance < abs(L1 - L2)):
            return None, None #that can be used later in Its_Alive. If the distance is out of reach the arms wont update
    else:

    #calculate elbow angle (theta2)
            theta2 = math.acos((distance**2 - L1**2 - L2**2) / (2 * L1 * L2))
#Law of Cosines!
    #calculate shoulder angle (theta1)
            theta1 = math.atan2(y_cord, x_cord) - math.acos((L2**2 + distance**2 - L1**2) / (2 * L2 * distance))
            return math.degrees(theta1), math.degrees(theta2)
##########################################
def translate(angle: float) -> int:

################
def read_knobs():

    
    
     return x_value, y_value
################Set up pen control (up and down)

##########
pen_switch = Pin(12, Pin.IN, Pin.PULL_DOWN) 
pen_pwm = PWM(Pin(2))
pen_pwm.freq(50)  # Standard servo frequency 50 Hz
pen_write = False # False = up, True = down
last_pen_button_state = 0 #We need to have a defined value 
##########
def pen_control():
     global pen_write, last_pen_button_state
     current_pen_button_state = pen_switch.value()
     if current_pen_button_state == 1 and last_pen_button_state == 0: #have it like this to actaully see its pressed!
            pen_write = not pen_write  #toggle the pen state
            print(f"Pen state changed: {'Ready!' if pen_write else 'Waiting!'}")
            pen_state = PEN_DOWN if pen_write else PEN_UP
            safe_duty(pen_pwm, pen_state)
    
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

    safe_angle(shoulder_pwm, theta1)
    safe_angle(elbow_pwm, theta2)

    #PEN!
    pen_control()  # Set the initial pen state


def main():
    """Main entry point to run the robotic arm control."""


if __name__ == "__main__": #The things ai just kinda added this for me, but it works so I guess its fine.
    main()