from scripts.socket_connection import connect_to_apibridge, close_connection
from scripts.send_order import send_order

def main():
    # Connect to APIBridge
    socket_conn = connect_to_apibridge()
    if socket_conn is None:
        print("Exiting...")
        return

    # Define your order details here (replace with actual values)
    order_details = "b'8,LE,SBIN,M,1,180,1,EQ,STG11'"

    # Send the order
    send_order(socket_conn, order_details)

    # Close the connection
    close_connection(socket_conn)

if __name__ == "__main__":
    main()
