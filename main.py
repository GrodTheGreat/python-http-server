import socket

HOST = '127.0.0.1'  # localhost
PORT = 6969

response: bytes = b'HTTP/1.1 200 OK\r\nConnection: close\r\n\r\nHello, World!\r\n\r\n'
print('Response:')
print(response)

print('Starting HTTP server...')

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
        print('Connected by', address)
        # Receive only a small portion of the request
        data: bytes = connection.recv(1024)
        print("Request received:")
        request_data: bytes = data
        request: str = request_data.decode()

        request_items = request.split(sep='\r\n')
        start_line = request_items.pop(0)
        print(start_line)
        for item in request_items:
            print(item)

        print('Reading start line...')
        start_line_items: list[str] = start_line.split(sep=' ')
        method: str = start_line_items[0]
        request_target: str = start_line_items[1]
        protocol: str = start_line_items[2]
        print(f'Method: {method}, Target: {request_target}, Protocol: {protocol}')

        # Send the response
        connection.sendall(data=response)
        print('Response sent, closing connection...')

    print('Socket closed...')

print('Server shutting down...')
