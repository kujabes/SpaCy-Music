from music21 import scale
import json

CENTERS = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def profile_generator(scale):
    profile = [0] * 12
    for i, note in enumerate(CENTERS):
        if note in scale:
            profile[i] = 1
    
    return profile


def main():
    major = dict(list())
    minor = dict(list())
    mixo = dict(list())
    dorian = dict(list())
    phrygian = dict(list())
    lydian = dict(list())
    locrian = dict(list())

    for center in CENTERS:
        # scales
        maj_scale = [str(note)[:-1] for note in scale.MajorScale(center).getPitches()]
        min_scale = [str(note)[:-1] for note in scale.MinorScale(center).getPitches()]
        mixo_scale = [str(note)[:-1] for note in scale.MixolydianScale(center).getPitches()]
        dorian_scale = [str(note)[:-1] for note in scale.DorianScale(center).getPitches()]
        phrygian_scale = [str(note)[:-1] for note in scale.PhrygianScale(center).getPitches()]
        lydian_scale = [str(note)[:-1] for note in scale.LydianScale(center).getPitches()]
        locrian_scale = [str(note)[:-1] for note in scale.LocrianScale(center).getPitches()]

        # generating corresponding profiles
        major_profile = profile_generator(maj_scale)
        minor_profile = profile_generator(min_scale)
        mixo_profile = profile_generator(mixo_scale)
        dorian_profile = profile_generator(dorian_scale)
        phrygian_profile = profile_generator(phrygian_scale)
        lydian_profile = profile_generator(lydian_scale)
        locrian_profile = profile_generator(locrian_scale)

        # creating dictionary for each profile
        major[center] = major_profile
        minor[center] = minor_profile
        mixo[center] = mixo_profile
        dorian[center] = dorian_profile
        phrygian[center] = phrygian_profile
        lydian[center] = lydian_profile
        locrian[center] = locrian_profile

    # dumping all the dictionaries into json files
    with open("key_profiles/major.json", "w") as f:
        json.dump(major, f)

    with open("key_profiles/minor.json", "w") as f:
        json.dump(minor, f)

    with open("key_profiles/mixolydian.json", "w") as f:
        json.dump(mixo, f)

    with open("key_profiles/dorian.json", 'w') as f:
        json.dump(dorian, f)

    with open("key_profiles/phrygian.json", 'w') as f:
        json.dump(phrygian, f)
    
    with open("key_profiles/lydian.json", 'w') as f:
        json.dump(lydian, f)
    
    with open("key_profiles/locrian.json", 'w') as f:
        json.dump(locrian, f)


if __name__ == '__main__':
    main()