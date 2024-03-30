from system.systemcalls import SystemCalls


class SystemCtl:
    system_calls = SystemCalls()

    def restart(self, service):
        self.system_calls.run_cmd(["sudo", "systemctl", "restart", service])

    def start(self, service):
        self.system_calls.run_cmd(["sudo", "systemctl", "start", service])

    def stop(self, service):
        self.system_calls.run_cmd(["sudo", "systemctl", "stop", service])
