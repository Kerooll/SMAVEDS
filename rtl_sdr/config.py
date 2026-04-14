# RTL-SDR Configuration File

# RTL-SDR Device Settings
CENTER_FREQUENCY = 433000000  # Frequency in Hz (433 MHz for TPMS)
SAMPLE_RATE = 2.048e6  # Sampling rate in Hz
GAIN = 40  # Gain level (adjust based on signal strength)

# Signal Processing Settings
BANDPASS_LOW = 0.1  # Lower cutoff frequency (normalized)
BANDPASS_HIGH = 0.9  # Upper cutoff frequency (normalized)
FILTER_ORDER = 4  # Order of the bandpass filter

# Data Capture Settings
CAPTURE_DURATION = 5  # Duration in seconds to capture RF data
PEAK_FREQUENCY_COUNT = 5  # Number of top peak frequencies to extract
DEMODULATION_THRESHOLD = 0.5  # Threshold for demodulating binary data



# End of rtl_config.py