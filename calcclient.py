import socket, json
import time
from calculatorObject import Calculator

HOST = "127.0.0.1"
PORT = 12834

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

calc = Calculator()
while calc.loop:
    #client.connect((HOST, PORT))
    calc.set_sign()
    client.send(calc.sign.encode('utf-8'))
    calc.set_nums()
    nums = {"num1": calc.num1, "num2": calc.num2}
    client.send(json.dumps(nums).encode('utf-8'))
    #client.send(str(calc.num2).encode('utf-8'))
    print("awaiting server...")
    print(f"Result: {client.recv(1024).decode('utf-8')}")
    #client.close()
    #time.sleep(1)