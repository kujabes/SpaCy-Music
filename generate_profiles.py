from music21 import scale
import json

# The 12 unique pitch classes
# Note: Some notes have two names (ex. C# is the Same as D-). 
# to avoid duplicates and for the sake of consistency
# the choice was made to use the sharp representation
# for these notes
PITCH_CLASSES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

# Given a scale, create a key profile 
# representing that scale
def profile_generator(scale):
    profile = [0] * 12
    for i, note in enumerate(PITCH_CLASSES):
        if note in scale:
            profile[i] = 1
    
    return profile

def neg_bias_profile_generator(scale):
    profile = [-1] * 12
    for i, note in enumerate(PITCH_CLASSES):
        if note in scale:
            profile[i] = 1
    
    return profile

def root_bias_profile_generator(scale, root):
    profile = [0] * 12
    for i, note in enumerate(PITCH_CLASSES):
        if note in scale:
            if note == root:
                profile[i] = 2
            else:   
                profile[i] = 1
    
    return profile

def main():
    # Initializing the 8 modes, of which there are 12 scales
    # Note: not all 72 scales are unique. (Ex. Cmaj == Amin)
    major = dict(list())
    minor = dict(list())
    mixo = dict(list())
    dorian = dict(list())
    phrygian = dict(list())
    lydian = dict(list())
    locrian = dict(list())

    # Mapping to rename flat notes into their sharp equivalent
    flat_map = {
            "C-": "B",
            "D-": "C#",
            "E-": "D#",
            "F-": "E",
            "G-": "F#",
            "A-": "G#",
            "B-": "A#"
        }
    
    for pitch in PITCH_CLASSES:
        # grabbing the scales for each mode of a given pitch class / note
        maj_scale = [str(note)[:-1] for note in scale.MajorScale(pitch).getPitches()]
        min_scale = [str(note)[:-1] for note in scale.MinorScale(pitch).getPitches()]
        mixo_scale = [str(note)[:-1] for note in scale.MixolydianScale(pitch).getPitches()]
        dorian_scale = [str(note)[:-1] for note in scale.DorianScale(pitch).getPitches()]
        phrygian_scale = [str(note)[:-1] for note in scale.PhrygianScale(pitch).getPitches()]
        lydian_scale = [str(note)[:-1] for note in scale.LydianScale(pitch).getPitches()]
        locrian_scale = [str(note)[:-1] for note in scale.LocrianScale(pitch).getPitches()]

        scales = [
            maj_scale,
            min_scale,
            mixo_scale,
            dorian_scale,
            phrygian_scale,
            lydian_scale,
            locrian_scale
        ]

        # normalizing scales so that flats appear as sharps
        # note: relies on mutability of lists
        for s in scales:
            for i, note in enumerate(s):
                if note in flat_map:
                    s[i] = flat_map[note]


        # generating corresponding profiles
        minor_profile = root_bias_profile_generator(min_scale, pitch)
        major_profile = root_bias_profile_generator(maj_scale, pitch)
        mixo_profile = root_bias_profile_generator(mixo_scale, pitch)
        dorian_profile = root_bias_profile_generator(dorian_scale, pitch)
        phrygian_profile = root_bias_profile_generator(phrygian_scale, pitch)
        lydian_profile = root_bias_profile_generator(lydian_scale, pitch)
        locrian_profile = root_bias_profile_generator(locrian_scale, pitch)

        # creating a mapping for each profile
        major[pitch] = major_profile
        minor[pitch] = minor_profile
        mixo[pitch] = mixo_profile
        dorian[pitch] = dorian_profile
        phrygian[pitch] = phrygian_profile
        lydian[pitch] = lydian_profile
        locrian[pitch] = locrian_profile

    # dumping all the dictionaries into json files
    path = "root_bias_key_profiles"
    with open(f"{path}/major.json", "w") as f:
        json.dump(major, f)

    with open(f"{path}/minor.json", "w") as f:
        json.dump(minor, f)

    with open(f"{path}/mixolydian.json", "w") as f:
        json.dump(mixo, f)

    with open(f"{path}/dorian.json", 'w') as f:
        json.dump(dorian, f)

    with open(f"{path}/phrygian.json", 'w') as f:
        json.dump(phrygian, f)
    
    with open(f"{path}/lydian.json", 'w') as f:
        json.dump(lydian, f)
    
    with open(f"{path}/locrian.json", 'w') as f:
        json.dump(locrian, f)


if __name__ == '__main__':
    main()