#Coded by Yashraj Singh Chouhan
import socket, threading
import winsound

nickname = input("Choose your nickname: ")
ip_address = input("Add IP Address")
port_address = int(input("Add Port Number"))
duration = 1000  
freq = 140
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip_address, port_address))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICKNAME':
                client.send(nickname.encode('ascii'))
                winsound.Beep(freq, duration)
            else:
                print(message)
                winsound.Beep(freq, duration)
        except:
            print("An error occured!")
            client.close()
            break
def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))
        winsound.Beep(freq, duration)

receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)                   
write_thread.start()