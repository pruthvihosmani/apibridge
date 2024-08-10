import socket
from config.settings import HOST, PORT

def connect_to_apibridge():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        print("Connected to API Bridge")
        return s
    except Exception as e:
        print(f"Failed to connect to API Bridge: {e}")
        return None

def close_connection(socket_conn):
    try:
        socket_conn.close()
        print("Connection closed")
    except Exception as e:
        print(f"Failed to close connection: {e}")
