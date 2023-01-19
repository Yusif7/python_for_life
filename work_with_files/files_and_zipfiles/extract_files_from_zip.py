from pathlib import Path
import zipfile

# Our zipfiles is in the same directory as our python file, dot means main directory
root_dir = Path('.')
zip_path = root_dir.glob('*.zip')
# The directory where we import files from zip
extract_path = Path('zip_files')

for path in zip_path:
    # If we extract files we need to use 'r'
    with zipfile.ZipFile(path, 'r') as zip_file:
        # If you want to add all files inside .zip files then do not use final_path use direct extractall method
        final_path = extract_path / Path(path.stem)
        zip_file.extractall(path=final_path)



