from pathlib import Path

def write_file(file_name, file_content):
    file_name = Path(file_name)
    if file_name.suffix != ".txt":
        file_name = file_name.with_suffix(".txt")
    with open(file_name, "w") as f:
        f.write(file_content)

def append_file(file_name, file_content):
    file_name = Path(file_name)
    if file_name.suffix != ".txt":
        file_name = file_name.with_suffix(".txt")
    with open(file_name, "a") as f:
        f.write(file_content)

def read_file(file_name):
    file_name = Path(file_name)
    if file_name.suffix != ".txt":
        file_name = file_name.with_suffix(".txt")
    with open(file_name, "r") as f:
        return f.read()
