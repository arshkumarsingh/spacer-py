import os

def get_directory_size(path):
    """Calculate the total size of a directory, including all subdirectories and files."""
    try:
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                if os.path.exists(file_path):
                    total_size += os.path.getsize(file_path)
        return total_size
    except Exception as e:
        print(f"An error occurred while getting directory size for {path}: {e}")
        return 0

def scan_directory(path):
    """Scan a directory and return a dictionary with the sizes of its subdirectories and files."""
    try:
        if not os.path.exists(path):
            raise ValueError("The specified path does not exist.")
        
        data = {}
        for dirpath, dirnames, filenames in os.walk(path):
            # Include files at the top level of the selected directory
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                data[file_path] = get_directory_size(file_path)
            
            # Include sizes of subdirectories
            for dirname in dirnames:
                dir_full_path = os.path.join(dirpath, dirname)
                data[dir_full_path] = get_directory_size(dir_full_path)
        return data
    except ValueError as ve:
        print(f"ValueError: {ve}")
        return {}
    except Exception as e:
        print(f"An unexpected error occurred while scanning directory: {e}")
        return {}

def format_size(size):
    """Format size in bytes to a more readable format (e.g., KB, MB, GB)."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0
    return f"{size:.2f} PB"

def scan_and_format_directory(path):
    """Scan a directory and return a dictionary with the formatted sizes of its subdirectories and files."""
    data = scan_directory(path)
    formatted_data = {key: format_size(value) for key, value in data.items()}
    return formatted_data

# Example usage:
if __name__ == "__main__":
    path = input("Enter the directory path to scan: ")
    data = scan_and_format_directory(path)
    for item, size in data.items():
        print(f"{item}: {size}")
