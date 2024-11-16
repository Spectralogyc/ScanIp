import socket

def scan_ip(ip_address):
    try:
        socket.inet_aton(ip_address)
        return True
    except socket.error:
        return False

def main():
    start_ip = input("Enter the starting IP address: ")
    end_ip = input("Enter the ending IP address: ")

    for ip_address in range(int(start_ip), int(end_ip) + 1):
        if scan_ip(str(ip_address)):
            print(ip_address)

if __name__ == "__main__":
    main()
