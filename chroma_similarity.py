from scipy.spatial.distance import cosine
import librosa

# Find the cosine similarity between two matrices
# i.e. cos(theta)
def cosine_similarity(m1, m2):
    # reshape matrices in the case they do not
    # have the same shape
    if m1.shape != m2.shape:
        min_val = min(m1.shape[1], m2.shape[1])
        m1 = m1[:, :min_val]
        m2 = m2[:, :min_val]
    
    flat1 = m1.flatten()
    flat2 = m2.flatten()
    return 1 - cosine(flat1, flat2)


def chroma_similarity(path1, path2):
    '''
    path1 - path to first .wav file
    path2 - path to second .wav file
    '''

    y1, sr1 = librosa.load(path1)
    y2, sr2 = librosa.load(path2)

    # duration will be used to create a ratio to ensure
    # both matrices have the same shape
    chroma1_duration = librosa.core.audio.get_duration(y=y1, sr=sr1)
    chroma2_duration = librosa.core.audio.get_duration(y=y2, sr=sr2)
    hop_length = int(512 * (chroma2_duration/chroma1_duration))
    
    # hop_length determines the "step size" for each stft, we are making
    # it such that we have the same number of frames in the two chromagrams
    chroma1 = librosa.feature.chroma_stft(y=y1, sr=sr1)
    chroma2 = librosa.feature.chroma_stft(y=y2, sr=sr2, hop_length=hop_length) 

    return cosine_similarity(chroma1, chroma2)


def main():
    songs = {
        'The Sound of Silence' : 'wav_songs/The Sound of Silence.wav',
        'What a Wonderful World' : 'wav_songs/What A Wonderful World (Official Video).wav',
        'Mad World' : 'wav_songs/Mad World.wav',
        'Blue Skies' : 'wav_songs/Blue Skies.wav'
    }

    vocal = {
        'The Sound of Silence' : 'wav_songs/separated/htdemucs/The Sound of Silence/vocals.wav',
        'What a Wonderful World' : 'wav_songs/separated/htdemucs/What A Wonderful World (Official Video)/vocals.wav',
        'Mad World' : 'wav_songs/separated/htdemucs/Mad World/vocals.wav',
        'Blue Skies' : 'wav_songs/separated/htdemucs/Blue Skies/vocals.wav'
    }

    bass = {
        'The Sound of Silence' : 'wav_songs/separated/htdemucs/The Sound of Silence/bass.wav',
        'What a Wonderful World' : 'wav_songs/separated/htdemucs/What A Wonderful World (Official Video)/bass.wav',
        'Mad World' : 'wav_songs/separated/htdemucs/Mad World/bass.wav',
        'Blue Skies' : 'wav_songs/separated/htdemucs/Blue Skies/bass.wav'
    }

    other = {
        'The Sound of Silence' : 'wav_songs/separated/htdemucs/The Sound of Silence/other.wav',
        'What a Wonderful World' : 'wav_songs/separated/htdemucs/What A Wonderful World (Official Video)/other.wav',
        'Mad World' : 'wav_songs/separated/htdemucs/Mad World/other.wav',
        'Blue Skies' : 'wav_songs/separated/htdemucs/Blue Skies/other.wav'
    }

    drums = {
        'The Sound of Silence' : 'wav_songs/separated/htdemucs/The Sound of Silence/drums.wav',
        'What a Wonderful World' : 'wav_songs/separated/htdemucs/What A Wonderful World (Official Video)/drums.wav',
        'Mad World' : 'wav_songs/separated/htdemucs/Mad World/drums.wav',
        'Blue Skies' : 'wav_songs/separated/htdemucs/Blue Skies/drums.wav'
    }

    # for song1 in vocal:
    #     for song2 in vocal:
    #         song_pair = f'{song1} <-> {song2}'
    #         sim = chroma_similarity(vocal[song1], vocal[song2])
    #         print(f'{song_pair: ^50} | similarity: {round(sim, 3)}')

    # tears = 'wav_songs/Mad World.wav'
    # gary = 'wav_songs/Mad World - Gary Jules (Lyrics).wav'
    # sim = chroma_similarity(tears, tears)
    # print(f'Mad World (Tears for Fears) <-> Mad World (Gary Jules) | similarity: {round(sim, 3)}')

    lamp = 'wav_songs/lamp.wav'
    dance = 'wav_songs/dance.wav'
    sim = chroma_similarity(lamp, dance)
    print(sim)

if __name__ == '__main__':
    main()