import socket

HOST = '127.0.0.1'  # localhost
PORT = 80  # HTTP

print('Starting http server...')

with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as soc:
    print('Socket created...')

    soc.bind((HOST, PORT))
    print('Socket successfully bound...')

    soc.listen(1)  # Only one connection at a time?
    print('Now accepting connections...')

    # This is blocking, the script will not progress until a connection
    # is found
    connection, address = soc.accept()

    with connection:
        print('Connect by', address)
        while True:
            data = connection.recv(1024)
            print(data)
            if not data:
                break
            connection.sendall(data)

    print('Socket closed...')

print('Server shutting down...')
