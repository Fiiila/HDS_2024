import os
from pathlib import Path
from phonetic_transcriptor import PhoneticTranscriptor


if __name__ == '__main__':
    # define transcriptor
    PT = PhoneticTranscriptor(Path("./input/vety_HDS.ortho.txt"), Path("./output/vety_HDS.phntrn.txt"))

    # load input
    PT.load_input()
    # PT.print_input_data()

    # preprocess input
    PT.preprocess_input_data()

    # apply transcription rules
    PT.apply_basic_rules()

    # save output into predefined file
    PT.save_output()