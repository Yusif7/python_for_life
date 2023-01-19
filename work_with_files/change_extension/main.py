from pathlib import Path

root_dir = Path('files')
file_path = root_dir.glob('**/*')

for file in file_path:
    if file.is_file():
        # Change suffix of file
        new_filename = file.with_suffix('.csv')
        file.rename(new_filename)
