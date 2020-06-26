import socket
import select
import errno
import json
from tkinter import *


# HEADER_LENGTH = 10

# IP = "127.0.0.1"
# PORT = 1234
# my_username = input("Username: ")

# # Create a socket
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Connect to a given ip and port
# client_socket.connect((IP, PORT))

# # Set connection to non-blocking state, so .recv() call won;t block, just return some exception we'll handle
# client_socket.setblocking(False)

# # Prepare username and header and send them
# # We need to encode username to bytes, then count number of bytes and prepare header of fixed size, that we encode to bytes as well
# username = my_username.encode('utf-8')
# username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
# client_socket.send(username_header + username)


def send_message():

    message = input(f'{my_username} > ')

    # If message is not empty - send it
    if message:

        # Encode message to bytes, prepare header and convert to bytes, like for username above, then send
        message = message.encode('utf-8')
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        client_socket.send(message_header + message)

    try:
        # Now we want to loop over received messages (there might be more than one) and print them
        while True:

            # Receive our "header" containing username length, it's size is defined and constant
            username_header = client_socket.recv(HEADER_LENGTH)

            # If we received no data, server gracefully closed a connection, for example using socket.close() or socket.shutdown(socket.SHUT_RDWR)
            if not len(username_header):
                print('Connection closed by the server')
                sys.exit()

            # Convert header to int value
            username_length = int(username_header.decode('utf-8').strip())

            # Receive and decode username
            username = client_socket.recv(username_length).decode('utf-8')

            # Now do the same for message (as we received username, we received whole message, there's no need to check if it has any length)
            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')

            # Print message
            print(f'{username} > {message}')

    except IOError as e:
        # This is normal on non blocking connections - when there are no incoming data error is going to be raised
        # Some operating systems will indicate that using AGAIN, and some using WOULDBLOCK error code
        # We are going to check for both - if one of them - that's expected, means no incoming data, continue as normal
        # If we got different error code - something happened
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error: {}'.format(str(e)))
            sys.exit()

        # We just did not receive anything
        #continue

    except Exception as e:
        # Any other exception - something happened, exit
        print('Reading error: '.format(str(e)))
        sys.exit()


def setDefaultDispenserAmount(n):
    with open('settings.json', 'r') as f:
        data = json.load(f)
        data["defaultSettings"]["dispenserAmount"]=n

    with open('settings.json', 'w') as f:
        json.dump(data, f)

def getDefaultDispenserAmount():
    with open('settings.json', 'r') as f:
        data = json.load(f)
        return data["defaultSettings"]["dispenserAmount"]

def setDefaultDispenserName(n):
    with open('settings.json', 'r') as f:
        data = json.load(f)
        data["defaultSettings"]["name"]=n
        
    with open('settings.json', 'w') as f:
        json.dump(data, f)

def getDefaultDispenserName():
    with open('settings.json', 'r') as f:
        data = json.load(f)
        return data["defaultSettings"]["name"]

def setCustomDispenserAmount(n):
    with open('settings.json', 'r') as f:
        data = json.load(f)
        data["customSettings"]["dispenserAmount"]=n
        
    with open('settings.json', 'w') as f:
        json.dump(data, f)

def getCustomDispenserAmount():
    with open('settings.json', 'r') as f:
        data = json.load(f)
        return data["customSettings"]["dispenserAmount"]

def setCustomDispenserName(n):
    with open('settings.json', 'r') as f:
        data = json.load(f)
        data["customSettings"]["name"]=n
        
    with open('settings.json', 'w') as f:
        json.dump(data, f)

def getCustomDispenserName():
    with open('settings.json', 'r') as f:
        data = json.load(f)
        return data["customSettings"]["name"]



with open('settings.json', 'r') as f:
        data = json.load(f)

dispenserAmount = getCustomDispenserAmount()
disensperName = getCustomDispenserName()

if dispenserAmount == "None" and disensperName == "None":
    dispenserAmount = getDefaultDispenserAmount()
    disensperName = getDefaultDispenserName()

root = Tk()

customDispenserAmount = Entry(root, width=50)
customDispenserName = Entry(root, width=50)
myLabel1= Label(root, text='Name: ' + disensperName)
myLabel2= Label(root, text='Amount: ' + str(dispenserAmount))
confirmDispenserAmount= Button(root,text='Confirm', command=setCustomDispenserAmount(customDispenserAmount.get()))
confirmDispenserName= Button(root,text='Confirm', command=setCustomDispenserAmount(customDispenserName.get()))
setCustomDispenserAmount(100)
myLabel1.grid(row=1, column=0)
myLabel2.grid(row=0, column=0)
customDispenserAmount.grid(row=3,column=0)
confirmDispenserAmount.grid(row=4,column=0)
customDispenserName.grid(row=5,column=0)
confirmDispenserName.grid(row=6,column=0)
root.mainloop()