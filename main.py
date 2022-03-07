import os
from colorama import init, Fore
from colorama import Back
from colorama import Style
from extensions import *
from console_picture import *

init(autoreset=True)

console_picture()

print('Write main path:')
main_path = input()


def create_folders_from_list(folder_path, folder_names):
    for folder in folder_names:
        if not os.path.exists(f'{folder_path}\\{folder}'):
            os.mkdir(f'{folder_path}\\{folder}')


def get_subfolder_paths(folder_path) -> list:
    subfolder_paths = [f.path for f in os.scandir(folder_path) if f.is_dir()]

    return subfolder_paths


def get_file_paths(folder_path) -> list:
    file_paths = [f.path for f in os.scandir(folder_path) if not f.is_dir()]

    return file_paths


def sort_files(folder_path):
    file_paths = get_file_paths(folder_path)
    ext_list = list(extensions.items())

    for file_path in file_paths:
        extension = file_path.split('.')[-1]
        file_name = file_path.split('\\')[-1]

        for dict_key_int in range(len(ext_list)):
            if extension in ext_list[dict_key_int][1]:
                print(
                    Fore.GREEN + f'Moving {file_name} in {ext_list[dict_key_int][0]} folder\n')
                os.rename(
                    file_path, f'{main_path}\\{ext_list[dict_key_int][0]}\\{file_name}')


def remove_empty_folders(folder_path):
    subfolder_paths = get_subfolder_paths(folder_path)

    for p in subfolder_paths:
        if not os.listdir(p):
            print(Fore.WHITE + Back.RED + 'Deleting empty folder:',
                  p.split('\\')[-1], '\n')
            os.rmdir(p)


if __name__ == "__main__":
    create_folders_from_list(main_path, extensions)
    sort_files(main_path)
    remove_empty_folders(main_path)

input("Press Enter to continue...")
