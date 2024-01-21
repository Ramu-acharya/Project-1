import socket
import time
commands = ["F", "B", "L", "R"]  # List of commands to alternate

# Set the IP address and port on which the laptop server will listen
host = '0.0.0.0'  # Listen on all available interfaces
port = 5000 #change if not working.

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(1)
print(f"Server listening on {host}:{port}")

# Accept a connection
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address}")

while True:
    # Receive a response from the client
    data = client_socket.recv(1024)
    if not data:
        break
    print(f"Received from client: {data.decode()}")

    # Send "F" and then "B" alternatively every 1 second
    for command in commands:
        client_socket.sendall(command.encode())
        time.sleep(2)  # Adjust the sleep duration if needed
# Close the connection
client_socket.close()
server_socket.close()
