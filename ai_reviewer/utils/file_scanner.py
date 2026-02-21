import os


def scan_python_files(directory, exclude=None):
    if exclude is None:
        exclude = []

    python_files = []

    for root, dirs, files in os.walk(directory):
        # Remove excluded directories
        dirs[:] = [d for d in dirs if d not in exclude]

        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))

    return python_files


if __name__ == "__main__":
    files = scan_python_files(".", exclude=["venv"])
    for f in files:
        print(f)