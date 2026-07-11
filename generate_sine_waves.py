import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram
from scipy.io import wavfile

def generate_sine_wave(frequency, duration=20.0, sample_rate=48000, output_dir="wav_outputs"):
    """
    Generates a pure sine wave and saves it as a 32-bit float .wav file, along with its spectrogram.
    
    Args:
        frequency (float): Frequency of the sine wave in Hz.
        duration (float): Duration of the audio in seconds.
        sample_rate (int): Sampling rate in Hz.
        output_dir (str): Directory to save the outputs.
    """
    print(f"Generating a {duration}s {frequency} Hz sine wave...")
    
    os.makedirs(output_dir, exist_ok=True)
    filename = os.path.join(output_dir, f"sine_{frequency}Hz.wav")
    
    # Generate time array
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    
    from scipy.signal.windows import tukey
    
    # Generate the sine wave
    sine_signal = np.sin(2 * np.pi * frequency * t)
    
    # Apply a Tukey window (fade-in/fade-out) to prevent spectral splatter (clicks) at the boundaries
    # alpha=0.05 on 20s means a 0.5s smooth fade-in and 0.5s fade-out, keeping the tone pure.
    window = tukey(len(sine_signal), alpha=0.05)
    sine_signal = sine_signal * window
    
    # Use 32-bit floating point format for highest precision (lossless)
    normalized_signal = np.float32(sine_signal)
    
    # Write the signal to a WAV file
    wavfile.write(filename, sample_rate, normalized_signal)
    print(f"Saved generated sine wave to {filename}")

    # Plot the ground truth spectrogram
    print(f"Generating ground truth spectrogram for {frequency} Hz...")
    f, t_spec, Sxx = spectrogram(normalized_signal, sample_rate, nperseg=2048, noverlap=1024)
    
    plt.figure(figsize=(12, 6))
    plt.pcolormesh(t_spec, f, 10 * np.log10(Sxx + 1e-10), shading='gouraud', cmap='viridis')
    plt.title(f"Ground Truth Spectrogram: {frequency}Hz Pure Sine Wave")
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    
    # Dynamically set y-axis limit based on frequency to make the tone visible
    ymax = min(sample_rate / 2, max(frequency * 1.5, 2000))
    plt.ylim(0, ymax)
    plt.colorbar(label='Power/Frequency (dB/Hz)')
    
    # Save the spectrogram plot
    plot_filename = filename.replace('.wav', '_spectrogram.png')
    plt.savefig(plot_filename, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved ground truth spectrogram to {plot_filename}\n")

if __name__ == "__main__":
    frequencies = [200, 500, 750, 1000, 1500, 2500, 8000]
    print(f"Generating sine waves for frequencies: {frequencies} Hz\n")
    for freq in frequencies:
        generate_sine_wave(freq)
