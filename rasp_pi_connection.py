import logging

import paramiko

from logging_config import setup_logger

logger = logging.getLogger("rasp_pi_connection")


class Picframe:
    def __init__(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.connect()

    def connect(self):
        self.ssh.connect(hostname="picframe", username="pi")

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
        o3 = p.get_directory_contents("PySpace/photo_framesdf")
        p.close()
    except OSError as e:
        p.close()
        logger.exception(e)
    except Exception as e:
        logger.exception(e)
