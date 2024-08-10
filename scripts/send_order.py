def send_order(socket_conn, order_details):
    try:
        socket_conn.sendall(order_details.encode('utf-8'))
        data = socket_conn.recv(1024)
        print("Order Response:", repr(data))
    except Exception as e:
        print(f"Failed to send order: {e}")
