import os
import time
from dbackerlib import RClone
from dbackerlib import MySQLDump

rclone = RClone.Wrapper()
mysqldump = MySQLDump.Wrapper()

def writeFile(content, name):
    with open(name, "w") as file:
        file.write(content)
        return file.name

def backupDB(database, remote):
    databasedata = mysqldump.databaseAsString(database)
    fname = writeFile( databasedata , f"{database}_{time.strftime('%H-%M-%j-%Y')}_BAK.sql")
    rclone.moveToRemote(fname, remote, "\DBacker")
    
if __name__ == "__main__":
    #rcCopyToRemote("backup.cmd", "ver2", "\\dbackup")
    backupDB("megabookstore", "ver2")
    
    