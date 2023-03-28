from command_runner.elevate import elevate
import ZIP
from pathlib import Path
import shutil
import os
from win32com.client import Dispatch
import subprocess

def create_autostartup(Thisfile: str):
    
    user_path = os.path.expanduser('~')
    

    if not os.path.exists(user_path+"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\PCInfoToExcel Client.lnk"):
        path = os.path.join(user_path + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup", "PCInfoToExcel Client.lnk")

        target = Thisfile
        
        Thisfile_name = os.path.basename(Thisfile)
        wDir   = Thisfile.replace('\\' + Thisfile_name, "")
        icon   = Thisfile

        shell    = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(path)

        shortcut.Targetpath       = target
        shortcut.WorkingDirectory = wDir
        shortcut.IconLocation     = icon

        shortcut.save()
    
        print(f'{Thisfile_name} добавлен в автозагрузку')  
    

            
def place_program(zipfile, dst, cfgfile):
    ZIP.unpack(zipfile + '.zip', dst)
    if CheckConfig(cfgfile):
        CopyConfig(cfgfile, dst + '\\' + zipfile + '\\' + cfgfile)

def CheckConfig(configfile):
    if Path('.\\' + configfile).is_file():
        return True
    else:
        return False
    
def CopyConfig(configfile, folder):
    shutil.copyfile('.\\' + configfile, folder)

def main():
    zipfile = 'Main'
    dst = 'C:\\Program Files\\ConfigNKU'
    cfgfile = 'client.cfg'
    place_program(zipfile, dst, cfgfile)
    create_autostartup(dst + '\\' + zipfile + '\\Main.exe')
    subprocess.run([dst + '\\' + zipfile + '\\Main.exe'])
 
if __name__ == "__main__":
    elevate(main)