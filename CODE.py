import time # For timing system
from gpiozero import LED, Button
led = LED(22) # To assign the LED to its specific GPIO pin
button = Button(17) # To assign the button to its GPIO pin

while True: # So the entire code is constantly looping
  
  if button.is_pressed:
    starttime = time.time()
    time.sleep(0.01) # To try protect CPU from risk of overload
    while button.is_pressed:
      led.on() # Turns on the LED when button is held down
    
    led.off() # Turns off the LED as soon as button is released
    endtime = time.time()
    elapsed = endtime - starttime # To calculate the time elapsed
    print(elapsed) # Prints the time elapsed
