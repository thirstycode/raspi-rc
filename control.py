import bluetooth
import time
import RPi.GPIO as GPIO

left_gpio=16
right_gpio=18
forward_gpio=19
reverse_gpio=21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(left_gpio, GPIO.OUT)
GPIO.setup(right_gpio, GPIO.OUT)
GPIO.setup(forward_gpio, GPIO.OUT)
GPIO.setup(reverse_gpio, GPIO.OUT)
GPIO.output(left_gpio , 0)
GPIO.output(right_gpio , 0)
GPIO.output(forward_gpio, 0)
GPIO.output(reverse_gpio, 0)

server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM ) 
port = 1
server_socket.bind(("",port))
server_socket.listen(1)
 
client_socket,address = server_socket.accept()
print "Accepted connection from ",address

def left_side_forward():
    print "FORWARD LEFT"
    GPIO.output(forward_gpio , 1)
    GPIO.output(reverse_gpio , 0)
    time.sleep(.5)
    GPIO.output(left_gpio , 1)
    GPIO.output(right_gpio , 0)

def right_side_forward():
   print "FORWARD RIGHT"
   GPIO.output(forward_gpio , 1)
   GPIO.output(reverse_gpio , 0)
   time.sleep(.5)
   GPIO.output(left_gpio , 0)
   GPIO.output(right_gpio , 1)

def forward():
   print "FORWARD"
   GPIO.output(left_gpio , 0)
   GPIO.output(right_gpio , 0)
   GPIO.output(forward_gpio , 1)
   GPIO.output(reverse_gpio , 0)

def left_side_reverse():
   print "BACKWARD LEFT"
   GPIO.output(forward_gpio , 0)
   GPIO.output(reverse_gpio , 1)
   time.sleep(.5)
   GPIO.output(left_gpio , 1)
   GPIO.output(right_gpio , 0)

def right_side_reverse():
   print "BACKWARD RIGHT"

   GPIO.output(forward_gpio , 0)
   GPIO.output(reverse_gpio , 1)
   time.sleep(.5)
   GPIO.output(left_gpio , 0)
   GPIO.output(right_gpio , 1)

def reverse():
   print "BACKWARD"
   GPIO.output(left_gpio , 0)
   GPIO.output(right_gpio , 0)
   GPIO.output(forward_gpio , 0)
   GPIO.output(reverse_gpio , 1)

def stop():
   print "STOP"
   GPIO.output(left_gpio , 0)
   GPIO.output(right_gpio , 0)
   GPIO.output(forward_gpio , 0)
   GPIO.output(reverse_gpio , 0)
 
data=""
while 1:
         data= client_socket.recv(1024)
         print "Received: %s" % data
         if (data == "F"):    
            forward()
         elif (data == "L"):    
            left_side_forward()
         elif (data == "R"):    
            right_side_forward()
         elif (data == "B"):    
            reverse()
         elif (data == "A"):    
            left_side_reverse()
         elif (data == "P"):    
            right_side_reverse()
         elif data == "S":
            stop()
         elif (data == "Q"):
            print ("Quit")
            break
client_socket.close()
server_socket.close()