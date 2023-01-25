# Add filter
from pathlib import Path

root_dir = Path('files')
filepath = root_dir.glob('**/*')
num = int(input('Enter the character: '))
for file in filepath:
    if file.is_file():
        new_file = file.parts[1].split('.')[0]
        if str(num) in new_file:
            print(file.absolute())







