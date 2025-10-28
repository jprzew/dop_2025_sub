import os
from pathlib import Path


def get_repo_path():
    path = Path(os.path.abspath('.'))  # Take the current directory

    # Find .git folder in superdirectory
    while not os.path.exists(path / '.git'):
        path = path.parent
        if path == Path('/'):
            raise FileNotFoundError('Probably not inside git repository.')

    return path
