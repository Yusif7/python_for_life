from pathlib import Path
from datetime import datetime, date

root_dir = Path('files')
file_paths = root_dir.glob('**/*')


for path in file_paths:
    if path.is_file():
        # stat func => All information about the file
        stats = path.stat()
        # Second created time
        second_created = stats.st_mtime
        # Convert to real date
        date_created = datetime.fromtimestamp(second_created)
        # Define the format of date
        date_created_str = date_created.strftime('%Y-%m-%d')
        new_filename = date_created_str + '-' + path.name
        new_filepath = path.with_name(new_filename)
        path.rename(new_filepath)

