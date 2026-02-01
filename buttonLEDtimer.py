import time # For timing system
from gpiozero import LED, Button # For the general purpose input output pins to be assigned to LED and button.
led = LED(22) # To assign the LED to its specific GPIO pin (GPIO22)
button = Button(17) # To assign the button to its GPIO pin (GPIO17)

while True: # So the entire code is constantly looping
  
  if button.is_pressed: # For the timer to start as soon as button is pressed
    starttime = time.time() # Creates a variable for the time now
    time.sleep(0.01) # To try protect CPU from risk of overload
    while button.is_pressed: # The while loop running when the button is held down
      led.on() # Turns on the LED when button is held down
    
    led.off() # Turns off the LED as soon as button is released
    endtime = time.time() # Creates a variable for the time now
    elapsed = endtime - starttime # To calculate the time elapsed (time now - time earlier)
    print(elapsed) # Outputs the time elapsed
