# OBD-II CAN Sniffer Configuration

# CAN Interface Settings
CAN_CHANNEL = 'can0'  # Use 'can0' for Linux, 'COMx' for Windows (Replace x with port number)
BITRATE = 500000  # Standard CAN bus speed

# Relevant CAN IDs to Filter
RELEVANT_IDS = {
    0x180: "Battery Voltage",
    0x1F0: "Engine Oil Level",
    0x200: "Tire Pressure",
}

# Logging Options
ENABLE_LOGGING = True  # Set to False to disable logging
LOG_FILE = "obd_can_log.txt"  # Log file path
LOG_FORMAT = "%(asctime)s [%(levelname)s] %(message)s"  # Log format
LOG_LEVEL = "INFO"  # Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)



# End of config.py
