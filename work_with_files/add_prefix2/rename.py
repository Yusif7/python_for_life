from pathlib import Path

root_dir = Path('files')
file_paths = root_dir.glob('**/*')

for path in file_paths:
    # Check if file inside of directory is folder
    if path.is_file():
        # Find the name of parent folder
        parent_folder = path.parts[1]
        new_filename = parent_folder + '-' + path.name
        new_filepath = path.with_name(new_filename)
        print(new_filepath)
        path.rename(new_filepath)
