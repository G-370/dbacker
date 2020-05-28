from os import popen, remove

class Wrapper:
    rclone_path = ""
    config_path = ""
    version = ""
    
    def __init__(self, rclone_path="rclone", config_path="rclone.conf"):
        self.version = popen(f"{rclone_path} --version")
        self.rclone_path = rclone_path
        self.config_path = config_path
    
    def callThis(self, invocation):
        out = popen(f"{self.rclone_path} {invocation} --config {self.config_path}")
        return out.read()
    
    def moveToRemote(self, what, remote, remote_folder):
        print(self.callThis(f"copy {what} {remote}:{remote_folder}"))