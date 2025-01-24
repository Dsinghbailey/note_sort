# Musical Merge Sort

A Python implementation of merge sort that plays musical notes during the sorting process. This creates an auditory representation of the sorting algorithm, where each comparison plays the notes being compared.

## Features

- Merge sort visualization through sound
- Multiple musical scale presets (Major, Minor, Pentatonic, Blues, etc.)
- Programmable tempo control
- Support for multiple octaves
- Pure tone generation using sine waves

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/musical-merge-sort.git
cd musical-merge-sort
```

2. Install the required dependencies:

```bash
pip install pygame numpy
```

## Usage

```python
from musical_merge_sort import *

# Create a scale across multiple octaves
extended_scale = add_octaves(C_PENTATONIC_MINOR_SCALE, 3, 5)

# Scramble the notes
scrambled_notes = scramble_notes(extended_scale)

# Sort them musically
tempo = 480  # BPM
sorted_notes = musical_merge_sort(scrambled_notes, tempo)
```

### Available Scales

- `C_MAJOR_SCALE`
- `C_NATURAL_MINOR_SCALE`
- `C_HARMONIC_MINOR_SCALE`
- `C_MELODIC_MINOR_SCALE`
- `C_PENTATONIC_MAJOR_SCALE`
- `C_PENTATONIC_MINOR_SCALE`
- `C_BLUES_SCALE`
- `C_DORIAN_SCALE`
- `C_MIXOLYDIAN_SCALE`

## Functions

### `musical_merge_sort(arr: List[str], tempo: int) -> List[str]`

Performs merge sort on an array of musical notes while playing each note during comparisons.

### `scramble_notes(notes: List[str]) -> List[str]`

Randomly shuffles the order of notes in an array.

### `add_octaves(notes: List[str], start_octave: int = 2, end_octave: int = 5) -> List[str]`

Creates a new array with the notes repeated across multiple octaves.

## License

MIT License

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
