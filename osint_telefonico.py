import time
import os
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import timezone
from phonenumbers import carrier
from pyfiglet import Figlet
import datetime
from tqdm import tqdm, trange
import winsound
from tqdm import tqdm, trange

while True:

    os.system('cls')

    LEG = Figlet(font='standard')
    print(LEG.renderText("IMPORTANTISIMO"))
    print("")
    
    print('''Hola!! bienvenido a esta herramienta de osint para numeros telefonicos,
    esta herramienta fue creada solamente para usos educativos y
    experimentativos, osea se
    que esta herramienta NUNCA debe ser utilizada con fines maliciosos,
    cosas como: cyberacoso, acoso,
    ataques informaticos, etc etc etc. NO DEBEN SER EJECUTADAS NUNCA,
    es totalmente ilegal en todos los paises del planeta
    *ME REFIERO A QUE NO DEBE SER EJECUTADA PARA CYBERACOSAR Y COSAS ASI,*,
    por esa razon, esta herramienta esta orientada
    a fines educativos y experimentativos, recuerden pedir
    permiso de la otra persona antes de probar a utilizar esta herramienta,
    ***por ejemplo
    yo estube todas las veces que la probe, con mi numero telefonico***,
    es la primera herramienta *de forma seria* que subo a esta plataforma
    asique me disculpo totalmente por cualquier fallo que tenga, me encantaria
    que me lo digais por alguna de mis redes sociales
    y ADEMAS,
    IMPORTANTE: NO ME HAGO RESPONSABLE DEL MAL USO QUE CUALQUIER OTRO USUARIO
    PUEDA HACER CON ESTA HERRAMIENTA,
    SOY EL AUTOR, PERO YO NO LA HE UTILIZADO DE MANERA ILICITA NI MALICIOSA,
    POR FAVOR, USTEDES TAMPOCO LO HAGAIS,
    NO ME HAGO RESPONSABLE DEL MAL USO QUE LE PODAIS DAR''')

    print("")
    print("")
    print("")
    print("y = si acepto, n = no acepto")
    print("")
    acuerdo = str(input("USTED ACEPTA ESTE ACUERDO DANDO A ENTENDER QUE NUNCA JAMAS UTILIZARAS ESTA HERRAMNIENTA DE MANERA MALICIOSA Y TAMBIEN ACEPTA QUE LA RESPONSABILIDAD DE QUE HAGA ALGO ILEGAL CON ESTA HERRAMIENTA QUEDARA SOLAMENTE PARA USTED, ES SU RESPONSABILIDAD LO QUE USTED HAGA CON ESTA HERRAMIENTA, *Y DE NINGUNA MANERA ES LA RESPONSABILIDAD DEL AUTOR LO QUE USTED HAGA CON ESTA HERRAMIENTA, YA QUE YO *el autor* LA CREE PARA LOS ENTUSIASTAS DE LA SEGURIDAD INFORMATICA DEFENSIVA Y EXPERIMENTATIVA*(y/n): "))

    if acuerdo == "n":
        print("")
        print("si no aceptas el acuerdo de ser una persona responsable y legal, no puedes utilizar mi herramienta ETICA, adios, no vuelvas")
        time.sleep(3)
        break
    elif acuerdo == "y":
        print("")
        print("perfecto!!, agradecemos que usted sea un hacker etico y te permitimos utilizar esta herramienta *ESPERE 10 SEGUNDOS, SI NO COMIENZA LA HERRAMIENTA, PULSE CTRL + Z Y VUELVELA A EJECUTAR*")
        print("")
        time.sleep(3)
        os.system('cls')

    comi = Figlet(font='standard')
    print(comi.renderText("INICIALIZANDO..."))
    duration = 200 # milliseconds
    freq = 2000  # Hz
    freq2 = 444 #Hz2
    freq3 = 1000 #Hz3
    freq4 = 600 #Hz4
    freq5 = 2000 #Hz5
    freq6 = 600 #Hz6
    freq7 = 2000 #Hz7
    freq8 = 999 #Hz8
    freq9 = 222 #Hz9
    freq10 = 5000 #Hz10
    freq11 = 700 #Hz11
    freq12 = 4000 #Hz12
    freq13 = 4000 #Hz13
    freq14 = 5000 #Hz14

    winsound.Beep(freq, duration)
    winsound.Beep(freq2, duration)
    winsound.Beep(freq3, duration)
    winsound.Beep(freq4, duration)
    winsound.Beep(freq5, duration)
    winsound.Beep(freq6, duration)
    winsound.Beep(freq7, duration)
    winsound.Beep(freq8, duration)
    winsound.Beep(freq9, duration)
    winsound.Beep(freq10, duration)
    winsound.Beep(freq11, duration)
    winsound.Beep(freq12, duration)
    winsound.Beep(freq13, duration)
    winsound.Beep(freq14, duration)

    texto = "i"
    for caracter in tqdm(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"]):
        texto = texto + caracter

    time.sleep(1)
    print("")
    os.system('cls')
    
    letras = Figlet(font='standard')
    nombre = Figlet (font='poison')
    print("")
    print(nombre.renderText("D3M0N1O GR1S"))
    print("")
    print("----------------------------------------------------------------------------")
    print("                                                                           |")
    print("Todo de mi                                                                 |")
    print("                                                                           |")
    print("----------------------------------------------------------------------------")
    print("                                                                           |")
    print("Autor: D3M0N10 GR1S                                                        |")
    print("                                                                           |")
    print("Redes sociales:                                                            |")
    print("                                                                           |")
    print("Instagram: pirat_ainformaticogris                                          |")
    print("                                                                           |")
    print("Canal de Youtube: https://www.youtube.com/channel/UCLxPhg5AuNe68hG8Z9NtdLg |")
    print("                                                                           |")
    print("----------------------------------------------------------------------------")
    print("")
    print(letras.renderText("OSINT - TELEFONICO"))

    print("vamos a hacer un doxxing de nuestro objetivo e intentar sacar informacion de ese numero, cosas como ¡ si existe o no ese numero")
    print("")
    print("Por favor el numero escribelo con el '+'  , el codigo del pais, y sin ningun espacio, ejemplo '+34111111111'")
    print("")
    print("POR EJEMPLO, si quieres doxear un numero de españa y el numero es: +34 123 34 45 56 pues tu lo que tendrias que escribir seria: +34123344556")
    time.sleep(2)

    n = False

    Q = str(input("numero de telefono para doxxear RECUERDA ESCRIBIR EL NUMERO SIN ESPACIOS, CON EL + Y CON EL CODIGO DEL PAIS, POR EJEMPLO +34111111111: "))

    numeroh = phonenumbers.parse(Q, "es")

    val = phonenumbers.is_valid_number(numeroh)
    
    if val == True:
        n = True
        
        print("")
        
        if n == True:
            print("")
            print("el numero existe:")
            print("")
            G = "YES"
            print(G)
            print("")
    elif Q == str:
        if n == False:
            print("")
            print("el numero no existe")
            print("")
            
    elif val == False:
        n = False
        if n == False:
            print("")
            print("El numero no existe")
            print("")
            break

    time.sleep(4)
    
    os.system('cls')

    print("COMIENZA EL DOXEO")
    
    time.sleep(4)

    os.system('cls')

    inf = Figlet(font='standard')

    print(inf.renderText("Recopilando informacion..."))

    time.sleep(4)

    os.system('cls')

    letras = Figlet(font='standard')
    nombre = Figlet (font='poison')
    print("")
    print(nombre.renderText("D3M0N1O GR1S"))
    print("")
    print(letras.renderText('''
    OSINT - TELEFONICO'''))

    print("OBJETIVO: " + Q)

    print("")

    print("¿EL NUMERO EXISTE?")

    print("")

    print(G)

    print("")

    hora = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    
    numero = phonenumbers.parse(Q, "es")
 
    zone = timezone.time_zones_for_number(numero)

    carr = phonenumbers.parse(Q)
    respuesta_carrier = carrier.name_for_number(carr, "es")

    geop = geocoder.description_for_number(numero, "es")

    region = geocoder.description_for_number(numero, 'es')

    time.sleep(3)

    print("")

    print("zona horaria de " + Q + ": ")

    print("")

    print(zone)

    print("")

    print("--------------------------------------------")

    print("informacion mas detallada de " + Q + " :")

    print("--------------------------------------------")

    print("")

    print(numero)

    print("")

    print("la isp de " + Q + " es: " + respuesta_carrier)

    print("")

    print("pais: " + geop)

    print("")

    print("ciudad/region: " + region)

    print("")

    print("HORA DEL DOXEO: " + hora)

    print("")

    LH = str(input("quieres guadar este doxing? y/n: "))

    if LH == "y":
        nombre_arch = str(input("nombre del archivo: "))
        
        time.sleep(2)
        file = open(nombre_arch + ".txt", "w")
        file.write("-------------------------------- \n")
        file.write("numero objetivo: " + Q + "\n")
        file.write("isp: " + respuesta_carrier + "\n")
        file.write("pais: " + geop + "\n")
        file.write("ciudad/region: " + region + "\n")
        file.write("--------------------------------- \n")
        file.write("HORA DEL DOXEO: " + hora + "\n")
        file.write("--------------------------------- \n")
        file.close()
        time.sleep(2)
        print("guardado con exito!!")
    elif LH == "n":
        time.sleep(1)

    print("")

    input("pulsa 'ENTER' para volver a iniciar un nuevo doxeo")

    print("")

    H = str(input("escriba 'n' para terminar o escriba 'y' para nuevo doxxeo: "))

    if H == "n":

        os.system('cls')

        letras = Figlet(font='standard')
        nombre = Figlet (font='poison')
        print("")
        print(nombre.renderText("D3M0N1O GR1S"))
        print("")
        print(letras.renderText('''
        OSINT - TELEFONICO'''))

        print("")

        print("muchas gracias por utilizar mi repositorio!! es la primera vez que utilizo github para subir un repositorio, y sinceramente, espero que si ahi algun fallo me informeis de ello, recordad que este repositorio fue creado de forma educativa y experimental!! no debeis utilizarlo de manera ilicita, recordad que yo no me hago responsable del mal uso que le deis, poco mas que decir! un abrazo, adios.")

        time.sleep(4)
                
        exit()
    elif H == "y":
        time.sleep(1)

    os.system('cls')
