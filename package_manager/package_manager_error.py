from package_manager import ReturnCode


class PackageManagerError(Exception):
    error_code = None

    def __init__(self, error_code: ReturnCode):
        self.error_code = error_code
        super(PackageManagerError, self)

    def __str__(self):
        return self.error_code.name
