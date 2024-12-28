import os

def count_class_lines(start_dir, file_types=[".cpp", ".h"]):
    total_lines = 0
    for subdir, dirs, files in os.walk(start_dir):
        # Exclude Intermediate and Binaries directories
        if 'Intermediate' in subdir or 'Binaries' in subdir:
            continue
        for file in files:
            # Only count lines in .cpp and .h files
            if any(file.endswith(ext) for ext in file_types):
                with open(os.path.join(subdir, file), 'r', encoding='utf-8', errors='ignore') as f:
                    total_lines += sum(1 for line in f)
                    print(f"Reading file {file}")
    return total_lines

project_dir = input("Enter you source directory: ")
lines = count_class_lines(project_dir)
print(f"Total lines of class scripts: {lines}")
