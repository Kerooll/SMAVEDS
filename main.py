import threading
import time
from obd_sniffer.obd_reader import setup_can_interface, read_can_messages
from rtl_sdr.rtl_reader import setup_rtl_sdr, capture_rf_data
from utils.bluetooth_transmitter import setup_bluetooth_server, send_data
from utils.data_parser import parse_obd_data, parse_tpms_data, format_for_bluetooth

def start_obd_sniffing(bus, data_store):
    """Thread function to read OBD-II CAN messages."""
    while True:
        message = bus.recv()
        if message:
            data_store[message.arbitration_id] = message.data[0]  # Simplified storage
        time.sleep(0.1)

def start_tpms_sniffing(sdr, data_store):
    """Thread function to capture TPMS data from RTL-SDR."""
    while True:
        raw_binary = capture_rf_data(sdr)
        if raw_binary:
            data_store["TPMS"] = raw_binary[:16]  # Store relevant bits
        time.sleep(5)

def main():
    """Main function to initialize and run all modules."""
    print("[INFO] Initializing System...")
    
    # Initialize CAN Bus
    bus = setup_can_interface()
    if not bus:
        print("[ERROR] OBD-II interface failed to initialize.")
        return
    
    # Initialize RTL-SDR
    sdr = setup_rtl_sdr()
    if not sdr:
        print("[ERROR] RTL-SDR interface failed to initialize.")
        return
    
    # Initialize Bluetooth Server
    bt_server = setup_bluetooth_server()
    if not bt_server:
        print("[ERROR] Bluetooth server failed to start.")
        return
    
    # Data Store
    data_store = {}
    
    # Start Threads
    threading.Thread(target=start_obd_sniffing, args=(bus, data_store), daemon=True).start()
    threading.Thread(target=start_tpms_sniffing, args=(sdr, data_store), daemon=True).start()
    
    print("[INFO] System Running. Waiting for Bluetooth connections...")
    
    while True:
        obd_data = parse_obd_data(data_store)
        tpms_data = parse_tpms_data(data_store.get("TPMS", ""))
        formatted_data = format_for_bluetooth(obd_data, tpms_data)
        send_data(bt_server, formatted_data)
        time.sleep(5)

if __name__ == "__main__":
    main()



# Run the main script to start the system
# $ python main.py