# encoding=utf-8
import os

if __name__ == '__main__':
    ls = os.listdir()
    for file_name in ls:
        if file_name[0] in ('.', '_') or file_name == 'main.py':
            continue
        with open(file_name, encoding='utf-8') as f:
            print(file_name, ": ", f.readline(), end=' ')
