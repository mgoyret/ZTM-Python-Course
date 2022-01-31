import hashlib
from urllib import request, response
import requests  # pide cosas de paginas web
import hashlib
from sys import argv, exit

"""
url = "https://api.pwnedpasswords.com/range/" + "password123"
res = requests.get(url)

en realidad, a la api no se le manda la contraseña. Hay que encriptarla, hashearla, con el
protocolo SH1, que es el protocolo que usa esta API. Para esto, ponemos nuestra contrasena en esta pagina:
https://passwordsgenerator.net/sha1-hash-generator/
damos en generate, y en realidad, igual es peligroso porq mandamos nuestro hash por internet, y se podria
revertir a la contrasena usando el protocolo. Entonces, solo mandamos los primeros 5 caracteres del hash, que es
larguisimo, y la pagina nos devuelve todas las contrasenas cuyo hash empieza con esos 5, y nosotros localmente
verificamos cada una. Asi, si alguien nos intercepta, solo ve esos 5 digitos, y hay miles de contraseñas cuyo
hash empieza con esos 5, seria muy dificil que le peguen justo a la mia.
"""

# psw = password123
# hash = CBFDAC6008F9CAB4083784CBD1874F76618D2A97


# funcion para enviar los 5 primeros caracteres de la contraseña hasheada, y obtener toda la lista de hashes que arrancan con esos 5 caracteres
def requestApiData(querychar):
    url = "https://api.pwnedpasswords.com/range/" + querychar
    #esta pagina, entramos con los 5 primeros dig y nos devuelve solo el tail, los restantes
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f"Error fetching: {res.status_code}, check the API and try again")
    return res


def readResponse(response):
    print(response.text)

def passwordLeaksCount(hashes, hashToCheck):
    hashes = ( line.split(":") for  line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hashToCheck:
            return count
    return 0


# funcion para comparar mi contraseña, con todas las obtenidas, revirtiendo el SHA1
def pwnedApiCheck(password):
    # sha1() recibe un string en unicode, y crea el hash.
    # tomamos la password, la codificamos a utf-8. hexdigest para tomar el objeto
    # q nos da hash y obtener el numero en exa, y upper porque necesitamos en mayus
    sha1Psw = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5char, tail = sha1Psw[:5], sha1Psw[5:]
    # response es la lista de contrasenas con esos 5 car. y la cantidad de veces que fue filtrada
    response = requestApiData(first5char)
    return passwordLeaksCount(response, tail)


def main(args):
    for password in args:
        count = pwnedApiCheck(password)
        if count:
            print(f"\"{password}\" was found {count} times, it is unsecure")
        else:
            print(f"\"{password}\" was not leaked, it is a safe password")
    return "done"

if __name__ == "__main__":
    exit(main(argv[1:]))
