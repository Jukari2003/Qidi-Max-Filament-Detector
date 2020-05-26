import RPi.GPIO as GPIO
import time
print('Running....')
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)    #System Switch
GPIO.setup(3,GPIO.OUT)                              #System LED
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)    #Filament Switch
GPIO.setup(17,GPIO.OUT)                             #Filament LED
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)


count = 0
while True:
    time.sleep(.1)
    ###Power Switch
    input_state = GPIO.input(2)  
    if input_state == False:
        #print('System On')
        GPIO.output(3,GPIO.HIGH)    #Turn System Light On

        
        ###Roller Switch
        input_state = GPIO.input(4)  
        if input_state == False:
            count = count + 1
            GPIO.output(17,GPIO.LOW) #Turn Filament LED Off 
            if count >= 100: #Wait 10 seconds before power system off
                GPIO.output(26, GPIO.HIGH) #Turn Socket Off
                GPIO.output(17,GPIO.LOW) #Turn Filament LED Off
                if (count % 2) == 0:
                    time.sleep(1)
                    GPIO.output(3,GPIO.LOW) #Turn System Light Off
                else:
                    time.sleep(1)
                    GPIO.output(3,GPIO.HIGH)#Turn System Light On
                
            elif (count % 2) == 0:
                GPIO.output(17,GPIO.HIGH) #Turn Filament LED On 
            else:
                GPIO.output(17,GPIO.LOW) #Turn Filament LED Off 
            
        
        else:
            count = 0;
            #print('Filament Full')
            GPIO.output(26, GPIO.LOW) #Turn Socket On
            GPIO.output(17,GPIO.HIGH) #Turn Filament LED On
            GPIO.output(3,GPIO.HIGH)  #Turn System Light On
        
        
        
        
        
    else:
        count = 0;
        #print('System Off')
        GPIO.output(26, GPIO.LOW) #Turn Socket On
        GPIO.output(3,GPIO.LOW) #Turn System Light Off
        GPIO.output(17,GPIO.LOW) #Turn Filament LED Off 
