import bluetooth
import time

def setup_bluetooth_server(port=1):
    """Initializes a Bluetooth RFCOMM server."""
    try:
        server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        server_sock.bind(("", port))
        server_sock.listen(1)
        print(f"[INFO] Bluetooth server started on port {port}, waiting for connections...")
        return server_sock
    except Exception as e:
        print(f"[ERROR] Failed to initialize Bluetooth: {e}")
        return None

def send_data(sock, data):
    """Sends diagnostic data over Bluetooth to a connected client."""
    try:
        client_sock, address = sock.accept()
        print(f"[INFO] Connected to {address}")
        client_sock.send(data)
        print(f"[INFO] Sent data: {data}")
        client_sock.close()
    except Exception as e:
        print(f"[ERROR] Failed to send data: {e}")

if __name__ == "__main__":
    server = setup_bluetooth_server()
    if server:
        while True:
            mock_data = "Battery: 12.4V, Oil: Normal, TPMS: 29 PSI"
            send_data(server, mock_data)
            time.sleep(5)  # Send updates every 5 seconds



# Run the script to start the Bluetooth server
# $ python bluetooth_transmitter.py

