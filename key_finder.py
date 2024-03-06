import scipy.io.wavfile as wav
from scipy.fft import fft, fftfreq
from scipy.signal import find_peaks
from librosa import hz_to_note
from librosa.feature import chroma_stft
from pprint import pprint

def notes_played(song):
    sample_rate, audio_data = wav.read(song)

    # if we have stereo input
    if len(audio_data.shape) == 2:
        # pick out only one channel
        audio_data = audio_data[:, 0]

    
    # Perform Fourier Transform
    # Note: Contains complex numbers representing the frequency components
    fft_result = fft(audio_data)

    # Calculate Frequencies
    fft_freq = fftfreq(len(audio_data), d=1/sample_rate)

    # Isolating positive frequencies
    # Note: only first half of values are unique/positive
    n = len(fft_freq) - 1
    abs_fft_result = abs(fft_result)**2
    pos_fft_freq = fft_freq[:n // 2]
    pos_fft_result = abs_fft_result[:n // 2]

    # Note: Distance between note frequencies becomes smaller in the lower ranges
    # https://mixbutton.com/mixing-articles/music-note-to-frequency-chart/
    peaks, _ = find_peaks(pos_fft_result, prominence=5e13, distance=30)
    note_frequencies = pos_fft_freq[peaks]
    
    # Converting frequencies to notes
    notes = hz_to_note(note_frequencies)

    return notes

def musical_key(notes):
    # use chromograms and short time fourier transform
    ...



def main():
    # song path
    song = "wav_songs/re-plus - Pulse.wav"
    chord = 'chords/CMajMelody1.wav'
    notes = notes_played(chord)
    print(notes)

    chromagram = chroma_stft(notes)
    pprint(chromagram)



if __name__ == '__main__':
    main()

