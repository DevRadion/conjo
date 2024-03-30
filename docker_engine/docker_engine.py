from logger.logger import Logger
from package_manager.package_manager import PackageManager
from system.systemcalls import SystemCalls
from system.systemctl import SystemCtl


class DockerEngine:
    package_manager = PackageManager()
    system_calls = SystemCalls()
    systemctl = SystemCtl()

    def install_docker_engine(self):
        Logger.log("Installing Docker Engine...")

        self.package_manager.update_packages()
        self.package_manager.upgrade_packages()

        os_name = self.system_calls.get_os_name()
        docker_os_url = f"https://download.docker.com/linux/{os_name}"
        self.package_manager.install_gpg_key(f"{docker_os_url}/gpg", "docker.asc")

        self.package_manager.add_source("docker", "/etc/apt/keyrings/docker.asc", docker_os_url)

        self.package_manager.update_packages()
        self.package_manager.upgrade_packages()

        self.package_manager.install_package(
            ["docker-ce", "docker-ce-cli", "containerd.io", "docker-buildx-plugin", "docker-compose-plugin"])
        self.systemctl.start("docker")

        self.package_manager.install_package(["docker-compose"])

        Logger.log("Docker Engine installed!")
