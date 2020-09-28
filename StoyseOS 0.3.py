import os
import subprocess
from datetime import datetime
import webbrowser

print("Stoyse | StoyseOS [Version 0.03]")
print("© 2020 Stoyse Corporation. All rights reserved.")
print("")

now = datetime.now()
current_time = now.strftime("%H:%M:%S")  # Realtime

__author__ = "Stoyse Corporation"
__version__ = "0.03"
__software__ = "StoyseOS"

user_name = input("user name : ")
password = input("password : ")
password_crypted = "****"
if user_name == "stoyse":
    if password == "julian":
        while True:
            path = "C:\stoyse\Julian >> "
            cmd = input(path)
            if cmd == "get login":
                print("pc login : " + str(os.getlogin()))
                print("user name : " + str(user_name))
                print("password : " + str(password_crypted))
            if cmd == "get full login":
                print("pc login : " + str(os.getlogin()))
                print("user name : " + str(user_name))
                print("password : " + str(password))
            if cmd == "cpu count":
                print("cpu count : " + str(os.cpu_count()))
            if cmd == "software info":
                print("Developer : " + __author__)
                print("Version : " + __version__)
                print("Software : " + __software__)
            if cmd == "windows Terminal":
                command = input("Windows command >> ")
                output = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = output.communicate()
                print(stdout, stderr)
            if cmd == "time":
                print("time >> " + current_time)
            if cmd == "help":
                webbrowser.open("https://julianfaitdugaming.wixsite.com/stoysecorp")
                webbrowser.open_new_tab("https://julianfaitdugaming.wixsite.com/stoysecorp/commands")
            if cmd == "info":
                print("get login")
                print("get full login")
                print("cpu count")
                print("software info")
                print("windows Terminal")
                print("time")
                print("help")
                print("for more info open https://julianfaitdugaming.wixsite.com/stoysecorp/")

            if cmd == "dev":
                print("developer mode ")
                if input("code for dev : ") == "root@stoyse":
                    print("full access accepted")
                    while True:
                        path = "C:\stoyse/root >> "
                        cmd = input(path)
                        if cmd == "break":
                            break
