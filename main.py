import os

if __name__ == '__main__':
    for file_name in os.listdir():
        if file_name[0] in ('.', '_') or file_name == 'main.py':
            continue
        with open(file_name) as f:
            print(file_name, ": ", f.readline(), end=' ')
