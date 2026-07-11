import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp, spectrogram
from scipy.io import wavfile

def generate_sweep_wav(filename="wav_outputs/sweep_100hz_to_10kHz.wav", duration=20.0, f0=100.0, f1=10000.0, sample_rate=48000, method='logarithmic'):
    """
    Generates a frequency sweep (chirp), saves it as a .wav file, and plots its spectrogram.
    
    Args:
        filename (str): Output filename.
        duration (float): Duration of the sweep in seconds.
        f0 (float): Starting frequency in Hz.
        f1 (float): Ending frequency in Hz.
        sample_rate (int): Sampling rate in Hz.
        method (str): Sweep method ('linear', 'quadratic', 'logarithmic', 'hyperbolic').
    """
    print(f"Generating a {duration}s {method} sweep from {f0} Hz to {f1} Hz...")
    
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # Generate time array
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    
    # Generate the frequency sweep
    sweep_signal = chirp(t, f0=f0, f1=f1, t1=duration, method=method)
    
    # Use 32-bit floating point format for highest precision (lossless, virtually no quantization noise)
    normalized_signal = np.float32(sweep_signal)
    
    # Write the signal to a WAV file
    wavfile.write(filename, sample_rate, normalized_signal)
    print(f"Saved generated sweep to {filename}")

    # Plot the ground truth spectrogram
    print("Generating ground truth spectrogram...")
    f, t_spec, Sxx = spectrogram(normalized_signal, sample_rate, nperseg=2048, noverlap=1024)
    
    plt.figure(figsize=(12, 6))
    # Add small epsilon to avoid log10(0) issues
    plt.pcolormesh(t_spec, f, 10 * np.log10(Sxx + 1e-10), shading='gouraud', cmap='viridis')
    plt.title(f"Ground Truth Spectrogram: {f0}Hz to {f1}Hz {method.capitalize()} Sweep")
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.ylim(0, min(sample_rate / 2, f1 + 2000)) # Focus on the relevant frequency range
    plt.colorbar(label='Power/Frequency (dB/Hz)')
    
    # Save the spectrogram plot
    plot_filename = filename.replace('.wav', '_spectrogram.png')
    plt.savefig(plot_filename, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved ground truth spectrogram to {plot_filename}")

if __name__ == "__main__":
    generate_sweep_wav()
