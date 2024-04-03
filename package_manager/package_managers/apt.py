import os
import subprocess

from logger.level import Level
from logger.logger import Logger
from package_manager.return_code import ReturnCode
from system.systemcalls import SystemCalls


class AptPackageManager:
    system_calls = SystemCalls()

    def update_packages(self):
        Logger.log("Updating packages...")
        args = ["sudo", "apt-get", "update"]
        return self.system_calls.run_cmd(args)

    def upgrade_packages(self, accept_installation=True):
        Logger.log("Upgrading packages...")
        args = ["sudo", "apt-get", "upgrade"]
        if accept_installation:
            args.append("-y")

        return self.system_calls.run_cmd(args)

    def install_apt_package(self, packages: [str], accept_installation=True):
        packages_str = " ".join(packages)
        Logger.log("Installing " + packages_str)

        args = ["sudo", "apt-get", "install"]
        if accept_installation:
            args.append("-y")

        args += packages
        return_code = self.system_calls.run_cmd(args)

        return ReturnCode(return_code)

    def install_gpg_key(self, key_url: str, key_name: str):
        try:
            # Install necessary packages
            self.install_apt_package(["ca-certificates", "curl"])
            self.system_calls.run_cmd(["sudo", "install", "-m", "0755", "-d", "/etc/apt/keyrings"])

            key_file_path = f"/etc/apt/keyrings/{key_name}"
            self.system_calls.run_cmd(["sudo", "curl", "-fsSL", key_url, "-o", key_file_path])

            self.system_calls.run_cmd(["sudo", "chmod", "a+r", key_file_path])

            Logger.log(f"GPG key '{key_name}' installed successfully.")

        except subprocess.CalledProcessError as e:
            Logger.log(f"Failed to install GPG key '{key_name}'. Error: {e}", Level.ERROR)
        except Exception as e:
            Logger.log(f"An unexpected error occurred: {e}", Level.ERROR)

    def add_source(self, key_name: str, key_file_path: str, repo_url: str):
        try:
            with open(f"/etc/apt/sources.list.d/{key_name}.list", "w") as sources_file:
                codename = os.popen(". /etc/os-release && echo \"$VERSION_CODENAME\"").read().strip()

                arch = self.system_calls.run(["dpkg", "--print-architecture"], capture_output=True, check=True)
                deb_line = f"deb [arch={arch.stdout.decode().strip()} signed-by={key_file_path}] {repo_url} {codename} stable\n"

                output = self.system_calls.run(["echo", deb_line], capture_output=True, check=True)
                sources_file.write(output.stdout.decode())

            return True

        except subprocess.CalledProcessError as e:
            Logger.log(f"Error adding Docker repository: {e}", Level.ERROR)
            return False
