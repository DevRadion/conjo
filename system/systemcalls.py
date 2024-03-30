import subprocess

from config import Config
from logger.level import Level
from logger.logger import Logger


class SystemCalls:
    def run(self, args, check, stdout=None, capture_output=False, text=None):
        Logger.log("Running command: " + " ".join(args), Level.VERBOSE)

        if Config.shared().wait_for_input:
            input("Press Enter to continue...")

        return subprocess.run(args, capture_output=capture_output, stdout=stdout, check=check, text=text)

    def run_cmd(self, args: [str]):
        try:
            command_str = " ".join(args)
            Logger.log("Running command: " + command_str, Level.VERBOSE)

            if Config.shared().wait_for_input:
                input("Press Enter to continue...")

            process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)

            if Config.shared().verbose:
                for line in process.stdout:
                    print(line, end='')

            return_code = process.wait()

            if return_code != 0:
                raise subprocess.CalledProcessError(return_code, args)

            return return_code

        except subprocess.CalledProcessError as e:
            Logger.log(f"Command {' '.join(args)} failed with return code {e.returncode}", Level.ERROR)
            raise e

        except Exception as e:
            Logger.log(f"An error occurred while executing {' '.join(args)}: {e}", Level.ERROR)
            raise e

    def get_os_name(self):
        try:
            with open("/etc/os-release", "r") as os_release_file:
                for line in os_release_file:
                    if line.startswith("NAME="):
                        os_name = line.split("=")[1].strip().strip('"')
                        return os_name.lower()
        except FileNotFoundError:
            return None
