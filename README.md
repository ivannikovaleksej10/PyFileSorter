# PyFileSorter

![GitHub last commit](https://img.shields.io/github/last-commit/moblamobla/PyFileSorter)
![GitHub repo size](https://img.shields.io/github/size/moblamobla/PyFileSorter/main.py)

Python script for sorting files into folders with flexible configuration

## Quick start
Open **extensions.py**

Set up a dictionary for your sorting method.

**Key** - folder name, **value** - list of file extensions for this folder.
```python
# key names will be folder names!
extensions = {

    'video': ['mp4', 'mov', 'avi', 'mkv'],

    'audio': ['mp3', 'wav', 'ogg'],

    'image': ['jpg', 'png', 'bmp', 'ai', 'psd', 'ico', 'jpeg', 'svg'],

    'archive': ['zip', 'rar', '7z', 'z', 'gz'],

    # 'folder-name': ['extension-name', 'another-extension']
}
```

Open **main.py** 
