""" Setup Files file for Python MVC Shell Framework Package """
import os
import glob
import shutil

from pathlib import Path
from importlib.resources import files


class SetupFiles():
    """ Class for PMVCS Setup Files """

    def __init__(self, setup: object) -> None:
        """
        Init the PMVCS Setup Files requirements
        """
        self.setup = setup

    def copy_files(self, subfolder: str, app_folder_name: str) -> None:
        """
        Copys all files and folders to another path
        """
        file_folder_orig = files('pmvcs').joinpath(f'setup/{subfolder}/')
        file_folder_dest = f'{self.setup.home_path}/{app_folder_name}/'

        shutil.copytree(file_folder_orig, file_folder_dest, dirs_exist_ok=True)

        if subfolder == 'defaults':
            shutil.copy(files('pmvcs').joinpath('setup/app.py'),
                        f'{self.setup.home_path}/app.py')
            self.rename_file(f'{self.setup.home_path}/',
                             'app.py', f'{app_folder_name}.py')

    def copy_file(self, subfolder: str, path: Path,
                  app_folder_name='') -> None:
        """
        Copys a file to another path
        """
        if subfolder:
            subfolder = f'{subfolder}/'

        if app_folder_name:
            app_folder_name = f'{app_folder_name}/'

        try:
            file_folder_orig = files('pmvcs').joinpath(f'setup/{subfolder}{path}')
            file_folder_dest = Path(f'{self.setup.home_path}/{app_folder_name}{path}')

            if file_folder_orig.is_file():
                shutil.copy(file_folder_orig, file_folder_dest)
                print(f'>>> {self.setup.lang_setup.sprintf("SETUP_COPYING", file_folder_dest)}')
        except FileNotFoundError as error:
            print(self.setup.lang_setup.sprintf(
                "SETUP_ERROR_COPYING_TO_APP", subfolder,
                path, file_folder_dest, error))

    def rename_file(self, current_path: Path,
                    old_file: str, new_file: str) -> None:
        """
        Renames a file in selected path
        """
        old_path = Path(current_path + old_file)
        new_path = Path(current_path + new_file)

        try:
            if old_path.is_file():
                shutil.move(old_path, new_path)
                print(f'>>> {self.setup.lang_setup.sprintf("SETUP_MOVING", current_path, new_file)}')
        except FileNotFoundError as error:
            print(self.setup.lang_setup.sprintf("SETUP_ERROR_MOVING_TO_APP",
                  current_path, old_file, current_path, new_file, error))

    def edit_files(self, path: str, search: str, replace: str) -> None:
        """
        Edits all files content of selected path
        """
        files_list = self._search_files(path)
        for file in files_list:
            self.edit_file(file, search, replace)

    def edit_file(self, path: str, search: str, replace: str) -> None:
        """
        Edits file content
        """
        if Path(path).suffix == '.py':
            try:
                #print(f'>>> Reading path: {path}')  #Debug
                with open(path, 'r', encoding='utf-8') as file:
                    data = file.read()

                data = data.replace(search, replace)

                #print(f'>>> Writing path: {path}')  #Debug
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(data)
            except FileNotFoundError as error:
                print(error)

    def to_camelcase(self, module_name: str, space=False) -> str:
        """
        Returns module class name in CamelCase
        """
        splited = module_name.replace("_", " ").split()

        if len(module_name) == 0:
            return module_name

        if space:
            return ' '.join(i.capitalize() for i in splited[0:])

        return ''.join(i.capitalize() for i in splited[0:])

    def _search_files(self, path: str) -> list:
        """
        Searchs files inside selected path
        """
        files_list = []
        filess = glob.glob(f'{path}**', recursive=True)

        for file in filess:
            if not os.path.isdir(file):
                files_list.append(str(file))

        return list(files_list)
