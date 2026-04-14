#SmaVeDS (Smart Vehicle Diagnostic System)

**Project Overview**
SmaVeDS is a modular vehicle diagnostic system that supports **both OBD-II CAN bus sniffing and RTL-SDR-based TPMS (Tire Pressure Monitoring System) decoding**. The software runs on a laptop, captures real-time vehicle data, and transmits it via **Bluetooth** to a mobile application for user-friendly diagnostics. 

**Key Features**
- **OBD-II Sniffing**: Reads engine oil level, battery voltage, and other vehicle parameters.
- **RTL-SDR TPMS Sniffing**: Captures RF signals from tire pressure sensors (315 MHz / 433 MHz).
- **Bluetooth Transmission**: Sends decoded vehicle diagnostics to a smartphone app.
- **Cross-Compatible Codebase**: Written in Python, compatible with Linux and Windows.
- **Scalable for Future Development**: Designed to transition from a laptop-based prototype to an embedded USB hardware device.

---

**Project Structure**

📂 **SmaVeDS/** _(Project Root)_  
├── 📄 `README.md` _(This file - Project Documentation)_  
├── 📄 `main.py` _(Main script to initialize and run OBD-II & RTL-SDR sniffing)_  
├── 📂 `obd_sniffer/` _(Handles OBD-II diagnostics)_  
│ ├── 📄 `obd_reader.py` _(Reads and parses OBD-II CAN messages)_  
│ ├── 📄 `config.py` _(Contains configurable OBD-II settings)_  
├── 📂 `rtl_sdr/` _(Handles RTL-SDR TPMS sniffing)_  
│ ├── 📄 `rtl_reader.py` _(Captures and decodes RF signals from TPMS sensors)_  
│ ├── 📄 `config.py` _(Contains RTL-SDR frequency and decoding settings)_  
├── 📂 `utils/` _(Utility functions for data processing)_  
│ ├── 📄 `bluetooth_transmitter.py` _(Handles Bluetooth communication with the phone app)_  
│ ├── 📄 `data_parser.py` _(Formats and processes CAN & TPMS data)_  
└── 📄 `requirements.txt` _(List of required dependencies)_  

---

**Installation Instructions**

1. Install Dependencies
Ensure you have Python 3.8+ installed. 
Then, install the required libraries:

pip install -r requirements.txt
