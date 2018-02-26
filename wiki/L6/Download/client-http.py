import socket

# -- IP and the port of the server to connect
IP = "localhost"  # Localhost means "I": your local machine
PORT = 8002

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# And now let's connect to our own server
try:
    s.connect((IP, PORT))
except ConnectionRefusedError:
    print("Connection refused!")
    print("Not possible to connect to server: {} at PORT {}".format(IP, PORT))
    exit()
except OSError:
    print("Socket already used")
    # But first we need to disconnect
    s.close()
    exit()

print("")
print("Connected to server: {} at PORT {}!".format(IP, PORT))

# HTTP Protocol: Send the request message to the server
s.send(bytes("GET / HTTP/1.1\n", "utf8"))
s.send(bytes("Host: www\n", "utf8"))
s.send(bytes("\n", "utf8"))
print("Request message sent!\n")

# Read the message from the server
print("Message from the server:")
print("-------------------------")

while 1:

    # Read the received data
    data = s.recv(1024)

    # If there is no data, finish
    if not data:
        break

    # Print the received data as an utf-8 string
    print(data.decode("utf-8"))

print("-------------------------")
s.close()
