# Add prefix in files directory
from pathlib import Path

# Define the root folder
root_dir = Path('files')
# Create a generator files
file_paths = root_dir.iterdir()
# List of files -> list(file_paths

for path in file_paths:
    new_filename = 'new-' + path.stem + path.suffix
    # new_filepath = Path(new_filename) -> when we use whis format we rename names of files and move them inside of
    # files directory
    # When we use this way we change names of files name inside of files directory
    new_filepath = path.with_name(new_filename)
    path.rename(new_filepath)
