from tkinter import *
from tkinter.scrolledtext import *
import time
import socket
import threading
import select
import timeit
import time

#at home Asus is 192.168.55.209, HP is 192.168.55.214
hpip = "192.168.55.214"
asusip = "192.168.55.209"

waittime = 2
ip = "192.168.55.214"
receiveip = socket.gethostbyname(socket.gethostname())
port = 8888
message = "Hello, World!"
connected = False
Sendmode = True

def command1(key):
    try:
        message = txtSearch.get()
    except:
        print("Problem getting message")
    if message != "":
        #print("message = " + message)
        if not commands(message):
            if connected or checkconnection():
                sock.sendto(bytes(message, 'UTF-8'), (ip, port))
                time.sleep(0.1)
                print1("Message sent")
    txtSearch.delete(0, 'end')


root = Tk()
frame2 = Frame(root, width=200, height=200, bg="#DDFFEE")
txtSearch = Entry(frame2, width=20)
txtSearch.bind('<Return>', command1)
txtSearch.grid(row=0, column=0)

results = ScrolledText(root, width=60, height=30, bg="#DDEEFF")
frame2.grid(row=1, column=0, sticky="NS")
results.grid(row=1, column=1)
results.insert(END, "Welcome to Connor's networked chat. Type 'help' to see commands. Once you are connected to another computer any text you enter that is not a command will be sent as a message.\n")

def print1(x):
    results.insert(END, "\n"+str(x))

def newsocket():
    global sock
    try:
        sock.close()
    except:
        print1("No send socket to close")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(waittime)
    print1("New send socket created")


def newrsocket():
    global rsock
    try:
        rsock.close()
    except:
        print1("No rsock to close down.")
        
    rsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #rsock.settimeout(waittime)
    print1("New rsocket created")
    #print1(receiveip)
    #print1(port)
    if receiveip != None and port != None:
        try:
            rsock.bind((receiveip, port))
            print1("New rsocket bound")
        except:
            print1("New rsocket failed bind.")
            raise


def checkconnection():
    global connected
    if ip == None:
        print1("You have not set the sending IP. Type 'connect_HP', 'connect_Asus', or 'set_send_ip'.")
        return False
    t1 = timeit.default_timer()
    sock.sendto(bytes("ping", 'UTF-8'), (ip, port))
    print1("Waiting for reply")
    try:
        data, addr = sock.recvfrom(1024)
        print1("Received pong")
        t2 = timeit.default_timer()
        myping = t2 - t1
        connected = True
        return True, myping
    except:
        print1("Timeout error. Maybe the server isn't functioning correctly?")
        newsocket()
        return False, 100
    
newsocket()
newrsocket()

mycommands = ["help", "ping", "connect_hp", "connect_asus", "my_ip", "set_receive_ip", "change_mode"]
messages = []
def commands(message):
    global ip
    global receiveip
    global Sendmode
    message = message.lower()
    

    if message in mycommands:
        print1("")
        print1("You entered the recognized command: " + message)
    else:
        return False
    
    if message == "help":
        for i,v in enumerate(mycommands):
            print1("Command #" + str(i) + " is " + v)
        print1("Type 'ping' to see connection info")
        print1("Type 'connect_HP' to connect to the HP with IP " + hpip)
        print1("Type 'connect_Asus' to connect to the Asus with IP " + asusip)
        print1("Type 'my_ip' to see what python thinks your local IP is.")
        print1("Type 'set_receive_ip' to set the receiving IP of this computer")
        print1("Type 'change_mode' to change to listening mode, though this change is not reversable")
        print1("")
        return True
    elif message == "ping":
        connected, ping = checkconnection()
        if connected:
            print1("You are connected to " + ip + ".")
            print1("Your ping is " + str(ping) + " seconds")
    elif message == "connect_hp":
        ip = hpip
        print1("Set to send messages to the HP on home network.")
        return True
    elif message == "connect_asus":
        ip = asusip
        print1("Set to send messages to the Asus on home network.")
        return True
    elif message == "set_send_ip":
        new_ip = input("Type in the IP address you would like to send messages to: ")
        ip = new_ip
        print1("Successfully set sending IP to " + ip)
        return True
    elif message == "my_ip":
        print1("Your local IP is " + socket.gethostbyname(socket.gethostname()))
        return True
    elif message == "set_receive_ip":
        new_rip = input("If you would like to have python set the receiving IP to your local IP, then press Enter. Else type 'No' and then press Enter.")
        if new_rip == "":
            receiveip = socket.gethostbyname(socket.gethostname())
            print("The receiving IP of this computer was set to: " + receiveip)
            try:
                newrsocket()
                print1("Rsocket bound seccessfully to " + receiveip)
            except:
                print1("Error binding receiving rsocket to IP " + receiveip + ", Port " + str(port))
                raise
        else:
            receiveip = input("Input the receiving IP for this computer: ")
            try:
                newrsocket()
                print1("Rsocket bound seccessfully to " + receiveip)
            except:
                print1("Error binding receiving socket to IP " + receiveip + ", Port " + str(port))
                newrsocket()
        return True
    elif message == "change_mode":
        Sendmode = False
        return True
    elif message == "show_messages":
        print1(len(messages))
        for i in messages:
            print1(i)
    return True


def Thread2():
    while True:
        ready = select.select([rsock], [], [], 1)
        if ready[0]:
            data, addr = rsock.recvfrom(1024)
            messages.append(data.decode('UTF-8'))
            #print(ip)
            #print(port)
            if data.decode('UTF-8').lower() == "ping":
                print("pinged by IP " + addr[0] + ":" + str(addr[1]))
                rsock.sendto(bytes("pong", 'UTF-8'), (addr[0], addr[1]))
            elif data.decode('UTF-8') == "received":
                print("confirmed received")
            else:
                rsock.sendto(bytes("received", 'UTF-8'), (ip, port))
                print1("Message: " + data.decode('UTF-8'))

t = threading.Thread(target=Thread2)
t.daemon = True
t.start() 

root.mainloop()
