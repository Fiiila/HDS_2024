import re
from pathlib import Path

# import custom modules
from SP1 import rules


class PhoneticTranscriptor(object):
    def __init__(self, input, output):
        self.input = Path(input)
        self.input_data = None
        self.input_data_tokens = []
        self.output = Path(output)
        self.result = None

    def load_input(self):
        if self.input.exists():
            with open(self.input, 'r', encoding='utf-8') as file:
                self.input_data = file.readlines()
            print("Input data loaded")
        else:
            print(f"Input file does not exists. Please check the given path: {self.input.__str__()}")

    def save_output(self):
        # check if output file and directory exists and create it if not
        if not self.output.exists():
            self.output.parent.mkdir(parents=True, exist_ok=True)

        # write the result into output file
        with open(self.output, 'w', encoding='utf-8') as file:
            file.writelines(self.result)
        print("Output file saved.")

    def preprocess_input_data(self):
        # read individual sentences and preprocess them individually
        for line in self.input_data:
            temp = re.split(r'(\W+)', string=line.strip().lower())
            self.input_data_tokens.append(temp)

    def apply_basic_rules(self):
        result = []
        temp = None
        for sentence in self.input_data_tokens:
            temp = "|$|" + '|'.join(sentence)
            for p in rules.BASIC_RULES:
                # print(f"{p} - {rules.BASIC_RULES[p]}")
                temp = re.sub(pattern=p, repl=rules.BASIC_RULES[p], string=temp)
            result.append(temp + "\n")
        print(result)
        self.result = result

    def print_input_data(self):
        print(*self.input_data)

    def print_output_data(self):
        pass

if __name__ == '__main__':
    # define transcriptor
    PT = PhoneticTranscriptor(Path("./input/ukazka_HDS.ortho.txt"), Path("./output/ukazka_HDS.trancribed.txt"))

    # load input
    PT.load_input()
    PT.print_input_data()

    # preprocess input
    PT.preprocess_input_data()
    print(PT.input_data_tokens)

    PT.apply_basic_rules()

    PT.save_output()