import pygame
import time
from typing import List
import numpy as np
import random

# Musical Scales in C
C_MAJOR_SCALE = ["c4", "d4", "e4", "f4", "g4", "a4", "b4", "c5"]
C_NATURAL_MINOR_SCALE = [
    "c4",
    "d4",
    "d#4",
    "f4",
    "g4",
    "g#4",
    "a#4",
    "c5",
]  # Also known as Aeolian
C_HARMONIC_MINOR_SCALE = ["c4", "d4", "d#4", "f4", "g4", "g#4", "b4", "c5"]
C_MELODIC_MINOR_SCALE = [
    "c4",
    "d4",
    "d#4",
    "f4",
    "g4",
    "a4",
    "b4",
    "c5",
]  # Ascending form
C_PENTATONIC_MAJOR_SCALE = ["c4", "d4", "e4", "g4", "a4", "c5"]
C_PENTATONIC_MINOR_SCALE = ["c4", "d#4", "f4", "g4", "a#4", "c5"]
C_BLUES_SCALE = ["c4", "d#4", "f4", "f#4", "g4", "a#4", "c5"]
C_DORIAN_SCALE = ["c4", "d4", "d#4", "f4", "g4", "a4", "a#4", "c5"]
C_MIXOLYDIAN_SCALE = ["c4", "d4", "e4", "f4", "g4", "a4", "a#4", "c5"]


def init_pygame_mixer():
    """Initialize pygame mixer for playing sounds"""
    pygame.mixer.init()
    pygame.init()


def get_frequency(note: str) -> float:
    """
    Convert a note string to its frequency in Hz
    Note format should be like 'c1', 'b4', 'd#3'
    """
    # Define base frequencies for notes (A4 = 440 Hz)
    base_notes = {
        "c": -9,
        "c#": -8,
        "d": -7,
        "d#": -6,
        "e": -5,
        "f": -4,
        "f#": -3,
        "g": -2,
        "g#": -1,
        "a": 0,
        "a#": 1,
        "b": 2,
    }

    # Parse the note and octave
    note = note.lower()
    note_name = "".join(c for c in note if not c.isdigit())
    octave = int("".join(c for c in note if c.isdigit()))

    # Calculate the number of half steps from A4
    half_steps = base_notes[note_name] + (octave - 4) * 12

    # Calculate frequency using the equation: f = 440 * (2^(n/12))
    # where n is the number of half steps from A4
    frequency = 440 * (2 ** (half_steps / 12))
    return frequency


def play_note(note: str):
    """
    Play a musical note using pygame
    Note format should be like 'c1', 'b4', 'd#3'
    """
    try:
        # Sound parameters
        sample_rate = 44100  # samples per second
        duration = 0.2  # seconds
        amplitude = 0.3  # volume (0.0 to 1.0)

        # Generate time array
        t = np.linspace(0, duration, int(sample_rate * duration), False)

        # Generate sine wave
        frequency = get_frequency(note)
        sine_wave = amplitude * np.sin(2 * np.pi * frequency * t)

        # Apply fade out to avoid clicking
        fade_out = np.linspace(1.0, 0.0, int(sample_rate * duration))
        sine_wave = sine_wave * fade_out

        # Convert to 16-bit integer samples
        audio_samples = (sine_wave * 32767).astype(np.int16)

        # Create stereo audio by duplicating the mono channel
        stereo_samples = np.column_stack((audio_samples, audio_samples))

        # Create pygame sound object
        sound = pygame.sndarray.make_sound(stereo_samples)
        sound.play()

    except Exception as e:
        print(f"Could not play note {note}: {e}")


def get_note_value(note: str) -> float:
    """
    Convert a note to a numeric value for comparison
    Note format should be like 'c1', 'b4', 'd#3', 'eb3'
    """
    # Parse the note and octave
    note = note.lower()
    note_name = "".join(c for c in note if not c.isdigit())
    octave = int("".join(c for c in note if c.isdigit()))

    # Define base values for notes, including both sharp and flat notations
    base_notes = {
        "c": 0,
        "c#": 1,
        "db": 1,
        "d": 2,
        "d#": 3,
        "eb": 3,
        "e": 4,
        "f": 5,
        "f#": 6,
        "gb": 6,
        "g": 7,
        "g#": 8,
        "ab": 8,
        "a": 9,
        "a#": 10,
        "bb": 10,
        "b": 11,
        "cb": 11,
    }

    # Calculate total value: (octave * 12) + note_value
    return (octave * 12) + base_notes[note_name]


def musical_merge_sort(arr: List[str], tempo: int, ascending: bool = True) -> List[str]:
    """
    Perform merge sort on an array of musical notes while playing each note

    Args:
        arr: List of note strings to sort
        tempo: beats per minute
        ascending: If True, sort from lowest to highest pitch. If False, sort from highest to lowest.

    Returns:
        Sorted list of notes
    """
    # Calculate delay between notes based on tempo
    delay = 60 / tempo  # Convert BPM to seconds

    def merge(left: List[str], right: List[str]) -> List[str]:
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            # Play the notes being compared
            play_note(left[i])
            time.sleep(delay)
            play_note(right[j])
            time.sleep(delay)

            # Compare notes by their musical value, considering sort direction
            left_val = get_note_value(left[i])
            right_val = get_note_value(right[j])

            if ascending:
                should_take_left = left_val <= right_val
            else:
                should_take_left = left_val >= right_val

            if should_take_left:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # Add remaining elements
        while i < len(left):
            play_note(left[i])
            time.sleep(delay)
            result.append(left[i])
            i += 1

        while j < len(right):
            play_note(right[j])
            time.sleep(delay)
            result.append(right[j])
            j += 1

        return result

    def sort(arr: List[str]) -> List[str]:
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = sort(arr[:mid])
        right = sort(arr[mid:])

        return merge(left, right)

    # Initialize pygame mixer before sorting
    init_pygame_mixer()

    # Perform the musical merge sort
    sorted_arr = sort(arr)

    # Clean up pygame
    pygame.quit()

    return sorted_arr


def scramble_notes(notes: List[str]) -> List[str]:
    """
    Randomly shuffle the order of notes in an array

    Args:
        notes: List of note strings

    Returns:
        A new list with the notes in random order
    """
    shuffled = notes.copy()  # Create a copy to avoid modifying the original
    random.shuffle(shuffled)
    return shuffled


def add_octaves(
    notes: List[str], start_octave: int = 2, end_octave: int = 5
) -> List[str]:
    """
    Create a new array with the notes repeated across multiple octaves

    Args:
        notes: List of note strings
        start_octave: Starting octave number (inclusive)
        end_octave: Ending octave number (inclusive)

    Returns:
        A new list with notes across specified octaves
    """
    result = []

    # Extract base notes without octave numbers
    base_notes = []
    for note in notes:
        note_name = "".join(c for c in note if not c.isdigit())
        if note_name not in base_notes:
            base_notes.append(note_name)

    # Add each note in each octave
    for octave in range(start_octave, end_octave + 1):
        for note_name in base_notes:
            result.append(f"{note_name}{octave}")

    return result


# Example usage
if __name__ == "__main__":
    # Create a scale across multiple octaves
    extended_scale = add_octaves(C_PENTATONIC_MAJOR_SCALE, 3, 5)

    # Scramble the notes
    scrambled_notes = scramble_notes(extended_scale)

    print("Scrambled notes:", scrambled_notes)
    # Sort them musically
    tempo = 480  # 120 BPM
    sorted_notes = musical_merge_sort(scrambled_notes, tempo, ascending=False)
    print("Sorted notes:", sorted_notes)
