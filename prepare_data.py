from pathlib import Path
from shutil import copyfileobj
from tempfile import TemporaryDirectory
from zipfile import ZipFile


def main():
    root = Path(__file__).resolve().parent
    paths = ('data/json_tres_potable.db', 'static/images/logo.png')
    with ZipFile(root / 'site-HubEau.zip') as archive:
        for relative_path in paths:
            target = root / relative_path
            if target.is_file():
                continue

            target.parent.mkdir(parents=True, exist_ok=True)
            with TemporaryDirectory(dir=target.parent) as directory:
                temporary_file = Path(directory) / target.name
                with archive.open(f'appli/{relative_path}') as source, temporary_file.open('wb') as output:
                    copyfileobj(source, output)
                temporary_file.replace(target)

    print('Base SQLite et logo disponibles.')


if __name__ == '__main__':
    main()
