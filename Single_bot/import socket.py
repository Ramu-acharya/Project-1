import socket  # Import the socket module for network communication
import time  # Import the time module for time-related functions

def calculate_commands(coordinates):
    movement_commands = []  # Use a different variable name to avoid conflicts
    current_position = (0, 0)  # Initialize the current position of the robot

    for coord in coordinates:  # Loop through each set of coordinates
        x, y = coord

        # Calculate the distance to move along the x-axis
        x_distance = x - current_position[0]

        # Calculate the distance to move along the y-axis
        y_distance = y - current_position[1]

        # Move forward
        if x_distance > 0:
            movement_commands.extend(["F"] * (x_distance // 200))  # Add forward commands
            time.sleep(2 * (x_distance // 200))  # Sleep to simulate movement time

        # Turn right or left
        if y_distance > 0:
            movement_commands.extend(["R"] * (y_distance // 200))  # Add right turn commands
            time.sleep(4 * (y_distance // 200))  # Sleep to simulate turn time
        elif y_distance < 0:
            movement_commands.extend(["L"] * (-y_distance // 200))  # Add left turn commands
            time.sleep(4 * (-y_distance // 200))  # Sleep to simulate turn time

        # Update the current position
        current_position = (x, y)

    # Stop the robotic car
    movement_commands.append("S")  # Add stop command

    return movement_commands

# Given coordinates
coordinates = [(200, 300), (400, 300), (600, 300), (800, 300), (800, 500), (800, 700), (800, 900)]

# Set the IP address and port on which the laptop server will listen
host = '0.0.0.0'  # Listen on all available interfaces
port = 5000  # Change if not working.

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

    received_data = data.decode()
    print(f"Received from client: {received_data}")

    # Check if the trigger message is received
    if received_data.strip() == "Hello Server!":
        # Calculate commands and send them to the client
        movement_commands = calculate_commands(coordinates)
        for command in movement_commands:
            client_socket.sendall(command.encode())  # Send the encoded command
            time.sleep(2)  # Adjust the sleep duration if needed

# Close the connection
client_socket.close()
server_socket.close()
