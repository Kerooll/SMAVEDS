import can
import time

def setup_can_interface(channel='can0', bitrate=500000):
    """Initializes the CAN bus interface."""
    try:
        bus = can.interface.Bus(channel=channel, bustype='socketcan', bitrate=bitrate)
        print(f"[INFO] CAN interface {channel} initialized.")
        return bus
    except Exception as e:
        print(f"[ERROR] Failed to initialize CAN interface: {e}")
        return None

def filter_relevant_messages(message):
    "Filters relevant CAN messages based on known CAN IDs."
    # 0x180: Battery Voltage, 0x1F0: Engine Oil Level, 0x200: Tire Pressure
    relevant_ids = {
        0x180: "Battery Voltage",
        0x1F0: "Engine Oil Level",
        0x200: "Tire Pressure",
    }
    if message.arbitration_id in relevant_ids:
        return relevant_ids[message.arbitration_id], message.data
    return None, None

def read_can_messages(bus):
    """Reads and prints relevant CAN messages from the vehicle."""
    print("[INFO] Listening for relevant CAN messages...")
    try:
        while True:
            message = bus.recv()  # Receive a message
            if message:
                label, data = filter_relevant_messages(message)
                if label:
                    print(f"{label}: {data.hex()}")
            time.sleep(0.1)  # Adjust polling rate if necessary
    except KeyboardInterrupt:
        print("[INFO] Stopping CAN listener.")
    except Exception as e:
        print(f"[ERROR] Failed to read CAN messages: {e}")

if __name__ == "__main__":
    bus = setup_can_interface()
    if bus:
        read_can_messages(bus)



# Run the script to read CAN messages
# $ python obd_reader.py
