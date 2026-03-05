from pathlib import Path

current_dir = Path.cwd()
current_file = Path(__file__).name # __file__ is a special Python variable for current file

print(f"Files in {current_dir}:")

for filepath in current_dir.iterdir(): # iterdir() returns all files and folders in that directory
    if filepath.name == current_file:
        continue

    print(f"  - {filepath.name}")

    if filepath.is_file():
        content = filepath.read_text(encoding='utf-8')
        print(f"    Content: {content}")