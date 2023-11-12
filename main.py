import os
import argparse
import sys

from libs.service import Service

path_root = os.path.dirname(os.path.abspath(__file__))


class Main:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-ini', '--params', type=str, default='-v -s')

        self.cli_args = parser.parse_args(sys.argv[1:])
        self.main()

    def main(self):

        service = Service()
        service.install_requirements(os.path.join(path_root, 'requirements.txt'))

        # устанавливаем/обновляем playwright
        service.send_local('playwright install', force=True)

        params_ini = []
        if self.cli_args.params is not None:
            params_ini = [f'-{param}' for param in (' ' + ''.join(self.cli_args.params)).split(' -')[1:]]

        tests_group = []
        for tests_folder in os.listdir(os.path.join(path_root, f'tests/')):
            if os.path.isdir(os.path.join(path_root, f'tests/{tests_folder}')):
                tests_group.append(f'{path_root}/tests/{tests_folder}/index.py')

        import pytest
        pytest.main(tests_group + params_ini)


if __name__ == '__main__':
    main = Main()
