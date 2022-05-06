import sys
import bz2
import random
import time
import sys
import pandas as pd


def read_complete_comment(file):

    while file.read(3) != b"}\n{":
        pass


    output = b"{"
    while 1:
        byte = file.read(3)
        if byte == b"}\n{":
            return output + b"}\n"
        output += byte


if __name__ == '__main__':
    NO_SAMPLES = int(sys.argv[1])
    random.seed(time.time())
    bytes = [random.randint(0, 500000000) for _ in range(NO_SAMPLES)]
    bytes.sort()
    output = b""
    with bz2.BZ2File("RC_2015-01.bz2", mode="rb") as input_file:
        for i in range(NO_SAMPLES):
            print(i)
            input_file.seek(bytes[i])
            output += read_complete_comment(input_file)
    with open("sample.json", "wb") as output_file:
        output_file.write(output)
    df = pd.read_json("sample.json", lines=True)
    df.to_csv(sys.argv[2], index=False)
