import logging
from typing import Tuple

import paramiko

from load_config import load_config
from logging_config import setup_logger

logger = logging.getLogger("rasp_pi_connection")


def get_username_and_password() -> Tuple[str, str]:
    config_data = load_config()
    try:
        username = config_data["AUTHENTICATION"]["username"]
        password = config_data["AUTHENTICATION"]["password"]
    except KeyError as error:
        logger.exception(error)
        raise

    return username, password


class Picframe:
    def __init__(self):
        self.username, self.password = get_username_and_password()
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.connect()

    def connect(self):
        self.ssh.connect(
            hostname="picframe", username=self.username, password=self.password
        )

    def execute_command(self, command):
        stdin, stout, sterr = self.ssh.exec_command(command)

        errors = sterr.readlines()
        if errors:
            raise OSError(errors)

        output_arr = stout.readlines()

        return output_arr

    def get_directory_contents(self, directory=""):
        return self.execute_command(f"ls {directory}")

    def close(self):
        self.ssh.close()


if __name__ == "__main__":
    setup_logger()
    p = Picframe()
    try:
        o1 = p.get_directory_contents()
        print(f"user directory: {o1}")
        o2 = p.get_directory_contents("PySpace/photo_frame")
        print(f"PySpace/photo_frame: {o2}")
        # o3 = p.get_directory_contents("PySpace/photo_frames")
        p.close()
    except OSError as e:
        p.close()
        logger.exception(e)
    except Exception as e:
        logger.exception(e)
