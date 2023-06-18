"""
tp2-tp3 transformée de fourier

La DFT permet de convertir un signal discret dans le domaine temporel en une représentation dans le domaine fréquentiel.
Plus précisément, la DFT prend un signal discret composé de N échantillons et calcule N coefficients de Fourier
correspondant aux différentes fréquences du signal.
Ces coefficients de Fourier représentent l'amplitude et la phase des composantes fréquentielles.
la base CN est une base d'un espace vectoriel complexe de dimension N,
utilisée dans le contexte de la DFT pour représenter les composantes fréquentielles d'un signal discret.
"""
import numpy as np
import wave
def w_k(k, n, N):
    """
    Calcule la valeur du k-ième vecteur de la base de l'espace vectoriel CN.
    """
    return np.exp(-2j * np.pi * (k-1) * n / N)
def dft(signal):
    """
    Calcule les coefficients de Fourier d'un signal donné en utilisant la transformée de Fourier discrète (DFT).
    """
    N = len(signal)
    dft_coeffs = np.zeros(N, dtype=np.complex128)
    for k in range(N):
        for n in range(N):
            dft_coeffs[k] += signal[n] * w_k(k+1, n, N)
    return dft_coeffs
def traitement_fichier_wav(file_path):
    """
    affiche les caracteristiques d un fichier son .wav
    """
    audio_file = wave.open(file_path, "rb")
    num_channels = audio_file.getnchannels()
    sample_width = audio_file.getsampwidth()
    frame_rate = audio_file.getframerate()
    num_frames = audio_file.getnframes()
    audio_frames = audio_file.readframes(num_frames)
    audio_data = np.frombuffer(audio_frames, dtype=np.int16)
    audio_data = audio_data / np.iinfo(np.int16).max
    audio_file.close()
    dft_coeffs = np.fft.fft(audio_data)
    return dft_coeffs
if __name__ == "__main__":
    signal = [1, 2, 3, 4]  # Signal d'entrée
    dft_coeffs = dft(signal)  # Calcul des coefficients de Fourier
    file_path = "1.wav"
    dft_result = process_wav_file(file_path)
    print(dft_result)
