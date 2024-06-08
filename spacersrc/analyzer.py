# spacersrc/analyzer.py
import os

def get_directory_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if os.path.exists(file_path):
                total_size += os.path.getsize(file_path)
    return total_size

def scan_directory(path):
    data = {}
    for dirpath, dirnames, filenames in os.walk(path):
        for dirname in dirnames:
            dir_full_path = os.path.join(dirpath, dirname)
            data[dir_full_path] = get_directory_size(dir_full_path)
    return data
