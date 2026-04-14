import json

def parse_obd_data(raw_data):
    """Parses raw OBD-II CAN data into structured format."""
    try:
        parsed_data = {
            "Battery Voltage": f"{int(raw_data.get(0x180, 0)) / 10}V",
            "Engine Oil Level": "Normal" if raw_data.get(0x1F0, 1) == 1 else "Low",
        }
        return parsed_data
    except Exception as e:
        print(f"[ERROR] Failed to parse OBD data: {e}")
        return {}

def parse_tpms_data(raw_binary):
    """Parses raw TPMS binary data into structured format."""
    try:
        parsed_data = {
            "Tire Pressure": f"{int(raw_binary[:8], 2) / 10} PSI",
            "Temperature": f"{int(raw_binary[8:16], 2)}°C",
        }
        return parsed_data
    except Exception as e:
        print(f"[ERROR] Failed to parse TPMS data: {e}")
        return {}

def format_for_bluetooth(obd_data, tpms_data):
    """Formats parsed data into JSON for Bluetooth transmission."""
    try:
        combined_data = {**obd_data, **tpms_data}
        return json.dumps(combined_data)
    except Exception as e:
        print(f"[ERROR] Failed to format data for Bluetooth: {e}")
        return "{}"

if __name__ == "__main__":
    mock_obd = {0x180: 124, 0x1F0: 1}
    mock_tpms = "1100001100100001"
    
    parsed_obd = parse_obd_data(mock_obd)
    parsed_tpms = parse_tpms_data(mock_tpms)
    formatted_data = format_for_bluetooth(parsed_obd, parsed_tpms)
    
    print(f"Formatted Data: {formatted_data}")



# Run the script to parse and format data
# $ python data_parser.py"
