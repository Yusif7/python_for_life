from pathlib import Path
import zipfile

root_dir = Path('files')
file_path = root_dir.glob('**/*')

root_dir2 = Path('files2')
file_path2 = root_dir.glob('**/*')
# If you want to create zip file inside of files directory write only root_dir / Path('archive.zip')
archive_dir = Path('archive.zip')
archive_dir2 = Path('archive2.zip')

# If you want to create use 'w'
with zipfile.ZipFile(archive_dir, 'w') as archive:
    for path in file_path:
        archive.write(path)

# If you want to create use 'w'
with zipfile.ZipFile(archive_dir2, 'w') as archive:
    for path in file_path2:
        archive.write(path)
