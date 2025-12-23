class ShutdownProtocol:
    def execute(self):
        return {
            "status": "SYSTEM HALTED",
            "reason": "Manual or ethical shutdown triggered"
        }
