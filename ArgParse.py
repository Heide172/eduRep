import argparse
import sys

def decode_Caesar_cipher(s, n):
    alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
    s = s.strip()
    text = ''
    for c in s:
        text += alpha[(alpha.index(c) + n) % len(alpha)]
    print('Decoded text: "' + text + '"')

def open_Enode_File(_args):
    filename = _args.file
    opened_file = open(filename)
    _encoded_text = opened_file.read()  # read the file into a string
    opened_file.close()  # always close the files you've opened
    return(_encoded_text)


args = sys.argv
parser = argparse.ArgumentParser()
parser.add_argument("--file")
args = parser.parse_args()

encoded_text = open_Enode_File(args)
for _i in range (1, 100):
    print(_i)
    decode_Caesar_cipher(encoded_text, -_i)

