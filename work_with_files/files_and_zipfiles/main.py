from pathlib import Path

root_dir = Path('files')
root_dir2 = Path('files2')
for i in range(1,11):
    filename = str(i) + '.txt'
    # Define path for new files files/new filename
    filepath = root_dir/Path(filename)
    # Method for creating
    filepath.touch()

for i in range(10,21):
    filename = str(i) + '.txt'
    # Define path for new files files/new filename
    filepath = root_dir2/Path(filename)
    # Method for creating
    filepath.touch()