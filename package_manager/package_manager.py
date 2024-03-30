from package_manager.package_managers.apt import AptPackageManager


class PackageManager:
    def install_package(self, packages: [str], accept_installation=True):
        # TODO: - Check OS -
        if True:
            apt_package = AptPackageManager()
            return apt_package.install_apt_package(packages, accept_installation)

    def install_gpg_key(self, key_url: str, key_name: str):
        # TODO: - Check OS -
        if True:
            apt_package = AptPackageManager()
            return apt_package.install_gpg_key(key_url, key_name)

    def update_packages(self):
        # TODO: - Check OS -
        if True:
            apt_package = AptPackageManager()
            return apt_package.update_packages()

    def upgrade_packages(self, accept_installation=True):
        # TODO: - Check OS -
        if True:
            apt_package = AptPackageManager()
            return apt_package.upgrade_packages(accept_installation)

    def add_source(self, key_name: str, key_file_path: str, repo_url: str):
        # TODO: - Check OS -
        if True:
            apt_package = AptPackageManager()
            apt_package.add_source(key_name, key_file_path, repo_url)
