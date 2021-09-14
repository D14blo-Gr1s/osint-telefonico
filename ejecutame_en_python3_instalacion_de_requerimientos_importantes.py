import os
from os import system
import sys
from sys import platform

Z = (platform)

if Z == "win32":
    os.system('cls')

    modulos = ["pyfiglet", "Figlet", "phonenumbers", "datetime", "time", "os", "tqdm", "colorama"]
    pip_version = "pip3"

    for i in modulos:
        system("{} install {}".format(pip_version, i))

    print("")

    import colorama

    from colorama import Back, Fore, Style, init

    init()
    
    print(Fore.GREEN + Back.BLACK + "TODOS LOS REQUERIMIENTOS FUERON INSTALADOS CORRECTAMENTE")

    init(autoreset=True)
    
    a = (platform)

    print("")

    print("usted esta utilizando el sistema operativo: {} [windows] LO CUAL SIGNIFICA QUE USTED DEBE EJECUTAR EL ARCHIVO osint_telefonico_para_windows.py".format (a))

    print("")

    os.system('dir')
elif Z == "linux":
    os.system('clear')

    modulos = ["pyfiglet", "Figlet", "phonenumbers", "datetime", "time", "os", "tqdm", "colorama"]
    pip_version = "pip3"

    for i in modulos:
        system("{} install {}".format(pip_version, i))

    print("")

    import colorama

    from colorama import Back, Fore, Style, init

    init()
    
    print(Fore.GREEN + Back.BLACK + "TODOS LOS REQUERIMIENTOS FUERON INSTALADOS CORRECTAMENTE")

    init(autoreset=True)

    a = (platform)

    print("")

    print("usted esta utilizando el sistema operativo: {} [LINUX] LO CUAL SIGNIFICA QUE USTED DEBE EJECUTAR EL ARCHIVO osint_telefonico_LINUX.py".format (a))

    print("")    
