# -*- coding: utf-8 -*-
import json
import random
import sys
import tty

wtf8 = json.loads(open('wtf8.json').read())

def translate(char):
    if wtf8.get(char) != None and wtf8[char]:
        return random.choice(wtf8[char])
    return char

def input_handler(key):
    if key == '\x1b':
        sys.stdout.write('\r\n')
        sys.exit(0)
    elif key == '\x7f':
        sys.stdout.write('\b \b')
    elif key == '\n':
        sys.stdout.write('\r\n')
    elif key == ' ':
        sys.stdout.write(key)
    elif key in list(wtf8.keys()):
        sys.stdout.write(translate(key))
    else:
        sys.stdout.write(key)
    sys.stdout.flush()

if __name__ == "__main__":
    data = ""
    if len(sys.argv) >= 2:
        data = open(sys.argv[2]).read() if sys.argv[1] == '-f' else sys.argv[1]
        for c in data:
            input_handler(c)

        sys.stdout.write('\r\n')
        sys.exit(0)

    tty.setraw(sys.stdin)
    while True:
        key = sys.stdin.read(1)[0]
        input_handler(key)
    
