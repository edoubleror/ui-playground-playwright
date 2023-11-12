# file must contain built-in imports only
import subprocess
import logging
import os


class Service:

    def __init__(self):
        self.log = logging.getLogger()

    def install_requirements(self, path_to_requirements):
        """
        Метод устанавливает обязательные модули для запуска и работы автоматизированных тестов
        """

        if not os.path.exists(path_to_requirements):
            raise self.log.error('File has been stolen or disappeared somewhere! (i mean requirements.txt)')

        cmd = f'pip3 install -q -r "{path_to_requirements}"'
        result = self.send_local(cmd)

        # error , no matching distribution found
        if 'rror' in result or 'o matching distribution found' in result or 'не найдена' in result:
            self.log.info(result)
            return False
        return True

    @staticmethod
    def send_local(cmd: str, force: bool = False) -> str:
        """
        Метод запускает команду в консоли операционной системы

        :param cmd: - непосредственно команда для консоли
        :param force: - это элемент "для последующего расширения" или на всякий случай. Когда мы не сможем выполнить команду
        средствами питона, мы можем её запустить исключительно в шелле, не управляемо и без вывода. Но запустим
        :return: Возвращаем вывод из консоли
        """

        if force:
            os.system(cmd)  # принудительный запуск команды - без результата вывода и не контролируемо...
        else:
            result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0 and len(result.stdout.decode()) > 0:
                return result.stdout.decode()
            return result.stderr.decode()
