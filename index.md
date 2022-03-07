# Welcome to PyFileSorter

Most likely, many people had a bunch of different installers, archives and other files in their downloads folder. It's much easier to find what you're looking for when the folders are sorted in the same style. So I thought, why not write a file extension sorter script in Python?

## Customizing the program to suit your needs
As you can already understand, the program is quite flexible, and you can customize it for yourself. To do this, you just need to change the extensions dictionary.

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

## Conclusion 
Take it, change it for yourself, use it for your health. I will be glad to any feedback.
