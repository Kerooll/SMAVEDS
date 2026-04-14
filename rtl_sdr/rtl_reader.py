from rtlsdr import RtlSdr
import numpy as np
import time
import scipy.signal as signal

def setup_rtl_sdr(center_freq=433000000, sample_rate=2.048e6, gain=40):
    """Initializes the RTL-SDR device with given parameters."""
    try:
        sdr = RtlSdr()
        sdr.sample_rate = sample_rate  # Sample rate in Hz
        sdr.center_freq = center_freq  # Frequency in Hz (433 MHz for TPMS)
        sdr.gain = gain  # Gain level
        print(f"[INFO] RTL-SDR initialized at {center_freq/1e6} MHz with gain {gain}.")
        return sdr
    except Exception as e:
        print(f"[ERROR] Failed to initialize RTL-SDR: {e}")
        return None 

def capture_rf_data(sdr, duration=5):
    """Captures RF data for a given duration and processes it."""
    print("[INFO] Capturing RF data...")
    try:
        samples = sdr.read_samples(duration * int(sdr.sample_rate))
        print("[INFO] Raw RF data captured.")
        
        # Apply Bandpass Filter (for better TPMS signal isolation)
        sos = signal.butter(4, [0.1, 0.9], btype='bandpass', output='sos', fs=sdr.sample_rate)
        filtered_samples = signal.sosfilt(sos, samples)
        
        # Perform FFT to analyze frequency domain
        magnitude = np.abs(np.fft.fft(filtered_samples))
        freq_axis = np.fft.fftfreq(len(magnitude), d=1/sdr.sample_rate)
        
        # Extract Peak Frequencies
        peak_freqs = freq_axis[np.argsort(magnitude)[-5:]]  # Top 5 frequencies
        print(f"[INFO] Peak Frequencies Detected: {peak_freqs}")
        
        # Convert RF signal to binary data (Basic Demodulation)
        binary_data = np.where(filtered_samples > np.mean(filtered_samples), 1, 0)
        print(f"[INFO] Demodulated Data: {binary_data[:50]}...")  # Print first 50 bits
        
        return binary_data
    except Exception as e:
        print(f"[ERROR] Failed to capture RF data: {e}")
        return None

if __name__ == "__main__":
    sdr = setup_rtl_sdr()
    if sdr:
        capture_rf_data(sdr)
        sdr.close() # Close the RTL-SDR device



# Run the script to capture RF data 
# $ python rtl_reader.py 

