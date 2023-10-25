import socket
import threading
from os import error
import string
import webbrowser

HOST = '127.0.0.1'
PORT = 8080
FORMAT = "utf8"

LOGIN = "login"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((HOST, PORT))

    print("SERVER SIDE")
    print('* Running on http://{HOST}:{PORT}')
    print("server:", HOST, PORT)
    print("Waiting for Client!!!")

except socket.error as e:
    print('socket error: {e}')
    print('socket error: %s' %(e)) 





def handleClient(conn, addr):
    while True:
        data = conn.recv(1024).decode()
        print(data)
        if not data: break
        request_line = data.split('\r\r')[0]
        print('1 ', request_line)
        request_method = request_line.split(' ')[0]
        print('2 ', request_method)
        request_url = (request_line.split(' ')[1]).strip('/')    
        print('3 ', request_method, request_url)
        length = len(request_line.split('\n'))
        print(length)
        x = request_line.split('\r\n')[length - 1]
        
        data = read_request(request_method, request_url)
        conn.send(data)
        conn.close()   
        break


def read_request(request_method,request_url):
    type = request_url.split('.')[1]
    print(type)
    if request_method == 'GET':
        
        Content_type = 'text/html' 
        data= read_file(request_url, Content_type)
        return data
        
def read_file(filename, Content_type):
    f = open(filename, 'rb')
    fdata = reponse_header(Content_type)
    fdata += f.read()
    return fdata

def reponse_header(Content_type):
    mess_head = 'HTTP/1.1 200 \n'
    mess_head += f'Content-type: {Content_type}'
    mess_head += '\r\n\r\n'
    mess_head = mess_head.encode()
    return mess_head
    
    
def serverLogin(conn):
    client_account = conn.recv()

    
if __name__ == '__main__':
    s.listen()
    while True:
        try:
            conn, addr = s.accept()
            thread = threading.Thread(target=handleClient, args=(conn, addr))
            thread.start()
        except:
            print('Error')
    # conn, addr = s.accept()
    # handleClient(conn, addr)      
    # conn.close() 
    # s.close()
    # server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # server.bind((HOST, 80))
    # server.listen()
    # connect, add = server.accept()
    # data = connect.recv(1024).decode()
    # data1 = data.split('\r\r')[0]
    # data2 = data1.split(' ')[0]
    # print("--hgfhgfhgfhgf-", data2,'--fgfghfghhgffhg--')
    # if(data2 == 'Username=admin&Password=123456'):
    #     dat = read_file('images.html', 'text/html')
    #     connect.send(dat)
    # connect.close()
    # server.close()
