from os import popen

class Wrapper:
    mysqldump_path = ""
    version = ""
    host = "" #TO DO: HOST-CASES
    user = ""
    password = ""
    
    def __init__(self, mysqldump_path="mysqldump", user="root", password=" ", host=""):
        self.mysqldump_path = mysqldump_path
        self.user = user
        self.password = password
        self.host = host
        
    def callThis(self, invocation):
        out = popen(f"{self.mysqldump_path} {invocation}")
        return out.read()
        
    def databaseAsString(self, database):
        return self.callThis(f"{database} --user={self.user} --password={self.password}")