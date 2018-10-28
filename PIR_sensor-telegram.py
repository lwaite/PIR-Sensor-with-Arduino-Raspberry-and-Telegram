import serial
import telegram
import time

myID = ID
bot = telegram.Bot(token=Token)
ser = serial.Serial('/dev/ttyACM0',9600)

def sendMessage():
    try:
        bot.sendMessage(myID, 'Presença detectada')
        time.sleep(3)
    except:
        pass

def waitPresence():
    while True:
        read = ser.readline()
        message = read.decode("utf-8")
        print(message)
        if message != '' :
            sendMessage()
        time.sleep(0.5)    

def main():
    waitPresence()

if __name__ == '__main__':
    main()
