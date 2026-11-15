Real quick GitHub was not acting nice so the most recent version was pushed to master instead of main. I am not sure what I am doing wrong but its something.







Okay so just to go over it, first we main function that runs. In main it will run ITS_ALIVE with a while loop. In keep alive function it gets x/y value from the knobs which is then translated into x/y coordinates with (PercentRead/MaxDuty)*((2*max arm length)-(max arm length)=x/ycord Then using x/y cord we run inverse kinematics where they get translated into theta 1 and theta 2 (we will include a function to return them as none if the angles are bad.) After that we will use set_safe_angle for both thetas. In set_safe_angle the angles are checked to be in allowed range then, then inside safe angle translate runs (we may put an extra redundancy in that) then after translate set_safe_duty will run where it checks the duty cycles are in range before finally setting them to the appropriate pwm pins. After those are updated pen control runs which checks if the button is pressed. Assuming everything works there will be virtually no delay between pressing then pen button and changing the pen. 




SKELTON CODE:
from machine import PWM, Pin, ADC
import math
import time

#Arm length


#Set up the pins for the knobs to control the arm
x_axis =
Defined as x_axis. It will be whatever pin we use to read where the point the arm is going to try to get to using one of the potentiometers. 
y_axis =
Defined as y_axis. It will be whatever pin we use to read where the point the arm is going to try to get to using one of the potentiometers.



#PWM for shoulder and elbow servos
We will use PWM for everything so we can update everything on the fly. A pwm signal will run through the potentiometers and later take the limited value converted back into useable number for finding the point on the paper we will try too move the arm too.


# Set PWM frequency for arm
More maintenance stuff. We will probably set it to 50, thats just what most people do.


# min and max duty cycles
We will define multiple items to have max and min. Each arm will have one and we will use it to limit the angle the servo will try to move to.


#FUNctions :)



#Safety functions for duty and angle conversions
def safe_duty(servo, duty):
#Make sure the angle is within the range of 0 to 180 degrees
    if D_MIN <= duty <= D_MAX:
         servo.duty_u16(duty)
    else:
        Return
Okay so this is just basic code. Basically this makes sure that the max and min distance are being respected. If they are, the duty is set, if not, it returns and does not implement the change. 




#Make sure angle set safe
def safe_angle(servo, angle):
    if 0 <= angle <= 180:
        duty = translate(angle)
        safe_duty(servo, duty)
This one makes sure the angle is not above or below 0 and 180 respectively. If it works the translate function runs and translates the 



###############################
def inverse_kinematics(x_cord, y_cord):
   
    distance = 
    #make sure the targets in reach
    if  (distance > (L1 + L2) or distance < abs(L1 - L2)):
            return None, None
	Make sure that the point we are trying to reach is not greater then the arm at full extension or the distance the arm can reach when fully bent.
    else:
    #calculate elbow angle (theta2)
    Use inverse Kin to find the right elbow angle. More work will need to be done. This could also be allocated to ai and we simply test and verify it. 

    #calculate shoulder angle (theta1)
Use inverse Kin to find the right shoulder angle 
        return (theta1), (theta2)
Return the right value



##########################################
def translate(angle: float) -> int:
This one is going to be longer but a bit less challenging. It should be roughly the same as the translate function we made in a lab. Essentially we need to take the angles we got from inverse kin and make those into a duty cycle to later use.

################
def read_knobs():
Just some basic code. X_value, y_value = the reduced value from the potentiometers. I believe there are ADC pins we can use.


    
    
     return x_value, y_value



################Set up pen control (up and down)
In here we will define what the pen needs to work, aka a button, a pull down, a way to make sure the button gets chcked




##########
def pen_control():
Make the pen go up and down. If the button got turned on and was previously on switch to the “down”/”up” duty cycle. 




######################################################33
def ITS_ALIVE():
    print("The robot arm is alive and ready to move!")
I just like knowing its working.
    #Gets the initial values of the knobs and converts them to x and y coordinates
    x_value, y_value = read_knobs()


Actually gets the value we will use for mapping used the reader function.

    #mapping the values in the range (1,(total arm length)) 
    x_cord = (x_value / 65535) * (2 * (L1 + L2)) - (L1 + L2)
    y_cord = (y_value / 65535) * (2 * (L1 + L2)) - (L1 + L2)

    #Ugly math
    theta1, theta2 = inverse_kinematics(x_cord, y_cord)
    if theta1 is None or theta2 is None:
        return
I forgot to mention if theta 1 or 2 is not allowed it will out as none. Literally none, not no value.
    safe_angle()
    safe_angle()


Using the safe angle to make sure its good. This also sets the duty cycle because set safe duty is ran inside safe angle,
    #PEN!
    pen_control() Just make the damn pen go. 

def main():
    Main entry point to run the robotic arm control.


if __name__ == "__main__": #The things ai just kinda added this for me, but it works so I guess its fine.
    main()
As you can see in the comment, it kinda just added but I like how it looks and it works so why not use it? Also it just kinda runs main constantly so that's great.





Everything is in and assigned. I am waiting on one person to accept the invite to the new repository (last one wouldn’t let me upload to it.) So whatever is not assigned is being worked on by the last member of our group.
