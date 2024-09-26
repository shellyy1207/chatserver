import socket
import threading

# 設定伺服器的 IP 和 Port
HOST = '127.0.0.1'
PORT = 12345

# 儲存所有連接的客戶端
clients = []

def broadcast(message, client_socket):
    """
    將訊息廣播給所有連接的客戶端
    """
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)

def handle_client(client_socket):
    """
    處理客戶端的訊息
    """
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(f"收到訊息: {message.decode('utf-8')}")
                broadcast(message, client_socket)
            else:
                client_socket.close()
                clients.remove(client_socket)
                break
        except:
            client_socket.close()
            clients.remove(client_socket)
            break

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"伺服器啟動，正在 {HOST}:{PORT} 等待連接...")

    while True:
        client_socket, client_address = server.accept()
        print(f"客戶端 {client_address} 已連接")
        clients.append(client_socket)
        threading.Thread(target=handle_client, args=(client_socket,)).start()

if __name__ == "__main__":
    main()