import pandas as pd
import numpy as np
from scipy.signal import butter, filtfilt, find_peaks
import matplotlib.pyplot as plt

def bandpass(signal, low, high, fs, order=4):
    nyq = 0.5 * fs
    b, a = butter(order, [low / nyq, high / nyq], btype='band')
    return filtfilt(b, a, signal)

def process_ecg(input_csv_path, plot_path):
    df = pd.read_csv("C:/Users/adity/Downloads/ecg/downloaded_ecg.csv")
    ecg = pd.to_numeric(df.iloc[:, -1], errors='coerce').dropna().values
    fs = 100  # Sampling rate from esp32 (samplingInterval = 10ms)

    # Filter ECG signal
    ecg_filt = bandpass(ecg - np.mean(ecg), 0.5, 40, fs)

    # R-peak detection
    min_distance = int(0.6 * fs)
    min_height = np.mean(ecg_filt) + 0.5 * np.std(ecg_filt)
    peaks, _ = find_peaks(ecg_filt, distance=min_distance, height=min_height)

    rpeak_times = peaks / fs
    rpeak_amplitudes = ecg_filt[peaks]

    # RR intervals and HR
    rr_intervals = np.diff(rpeak_times)
    heart_rates = 60 / rr_intervals

    features_df = pd.DataFrame({
        'R_peak_sample': peaks[1:],
        'R_peak_time_s': rpeak_times[1:],
        'R_peak_amplitude': rpeak_amplitudes[1:],
        'RR_interval_s': rr_intervals,
        'Heart_rate_bpm': heart_rates
    })

    features_df.to_csv('ecg_features_detailed.csv', index=False)

    # Save plot
    plt.figure(figsize=(12, 4))
    plt.plot(ecg_filt, label='Filtered ECG')
    plt.scatter(peaks, ecg_filt[peaks], color='red', label='R-peaks')
    plt.title('ECG with Detected R-peaks')
    plt.legend()
    plt.tight_layout()
    plt.savefig(plot_path)
    plt.close()

    return features_df
