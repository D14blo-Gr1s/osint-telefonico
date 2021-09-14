import os
from os import system
import sys
from sys import platform

Z = (platform)

d = print(Z)
if d == "win32":
    os.system('cls')

    modulos = ["pyfiglet", "Figlet", "phonenumbers", "datetime", "time", "os", "tqdm"]
    pip_version = "pip3"

    for i in modulos:
        system("{} install {}".format(pip_version, i))

    print("")

    print("TODOS LOS REQUERIMIENTOS FUERON INSTALADOS CORRECTAMENTE")

    a = (platform)

    print("")

    print("usted esta utilizando el sistema operativo: {}".format (a))

    print("")

    os.system('dir')
elif d == "linux":
    os.system('clear')

    modulos = ["pyfiglet", "Figlet", "phonenumbers", "datetime", "time", "os", "tqdm"]
    pip_version = "pip3"

    for i in modulos:
        system("{} install {}".format(pip_version, i))

    print("")

    print("TODOS LOS REQUERIMIENTOS FUERON INSTALADOS CORRECTAMENTE")

    a = (platform)

    print("")

    print("usted esta utilizando el sistema operativo: {}".format (a))

    print("")    
