import socket
from calculatorObjServer import Calculator

HOST = '127.0.0.1'
PORT = 12834

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)

communication_socket, address = server.accept()
print(f"Connected to: {address[0]}")

while True:
    #communication_socket, address = server.accept()
    #print(f"Connected to: {address[0]}")
    sign = communication_socket.recv(1024).decode('utf-8')
    print(f"sign: {sign}")
    num1 = communication_socket.recv(1024).decode('utf-8')
    print(f"num1: {num1}")
    num2 = communication_socket.recv(1024).decode('utf-8')
    print(f"num2: {num2}")

    #print(address + " is trying to " + sign + " with " + num1 + " and " + num2)

    try:
        if str(sign) == "+":
            result = str(float(num1) + float(num2))
            communication_socket.send(result.encode('utf-8'))
            print("sent: " + result)
        elif str(sign) == "-":
            result = str(float(num1) - float(num2))
            communication_socket.send(result.encode('utf-8'))
            print("sent: " + result)
        elif str(sign) == "*":
            result = str(float(num1) * float(num2))
            communication_socket.send(result.encode('utf-8'))
            print("sent: " + result)
        elif str(sign) == "/":
            result = str(float(num1) / float(num2))
            communication_socket.send(result.encode('utf-8'))
            print("sent: " + result)
        else:
            communication_socket.send("Not Valid".encode('utf-8'))
            print("sent: Not Valid")
    except Exception as e:
        print(e)
        exit()
    #communication_socket.close()
    #print(f"Connection with {address[0]} ended")
    