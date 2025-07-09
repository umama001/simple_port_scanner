# Importing necessary modules
import socket   # For creating network connections (IP + Port)
import sys      # For handling command-line arguments and exiting

# Function to scan a specific port on a target host
def scan_port(target_host, target_port):
    try:
        # Create a TCP socket using IPv4
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # Set timeout to 1 second (don’t wait forever)

        # Try to connect to the target host and port
        result = s.connect_ex((target_host, target_port))

        # If result is 0, connection successful → port is open
        if result == 0:
            print(f"Port {target_port}: Open")
        else:
            # Any other result means port is closed or filtered (e.g., by firewall)
            print(f"Port {target_port}: Closed or Filtered")

        s.close()  # Close the socket after checking

    # If the hostname (IP or domain) is invalid
    except socket.gaierror:
        print(f"Hostname could not be resolved: {target_host}")
        sys.exit()

    # If there’s a general error in connecting to the server
    except socket.error:
        print("Could not connect to server.")
        sys.exit()

# Main function: entry point of the script
def main():
    # Check if exactly 2 arguments were provided (host and port)
    if len(sys.argv) != 3:
        print("Usage: python3 port_scanner.py <target_host> <target_port>")
        sys.exit()

    # Get the first argument from the command line → target host/IP
    target_host = sys.argv[1]

    try:
        # Try converting second argument to integer → target port
        target_port = int(sys.argv[2])
    except ValueError:
        # If port is not a number, show error
        print("Invalid port number.")
        sys.exit()

    # Call the scanning function with the host and port
    scan_port(target_host, target_port)

# Run the main function only if this script is executed directly
if __name__ == "__main__":
    main()

