from PIL import Image
from sys import argv
import os

orig = argv[1]
dest = argv[2]

try:
    os.mkdir(dest)
except FileExistsError as err:
    pass

for fileName in os.listdir(orig):
    img = Image.open(f'./{orig}/{fileName}')
    img.save(f"./{dest}/{os.path.splitext(fileName)[0]}.png", "png")
    print("image saved")
    # lo de splitext() lo vi en el video, separa en el punto, y devuelve tuple de ambas aprtes
    # yo habia puesto {fileName[0:-3]}, pero era fijo para extension de 3 caracteres

print("END")
