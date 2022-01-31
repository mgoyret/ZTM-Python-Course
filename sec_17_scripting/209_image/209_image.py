from PIL import Image, ImageFilter

img = Image.open('./raw/pikachu.jpg')

# probando filtros
filteredImg = img.filter(ImageFilter.BLUR)
filteredImg.save("blur.png", "png")

sharpenedImg = img.filter(ImageFilter.SHARPEN)
sharpenedImg.save("sharpened.png", "png")

# probando conversion, esl modo blanco y negro es "L"
convertedImg = img.convert("L")
convertedImg.save("grey.png", "png")

rotatedImg = img.rotate(90)
rotatedImg.save("rotated.png", "png")

# comprimir imagen
compressedImg = img.copy()
"""
a thumbnail() le damos un tuple con los valores maximos
de dimensiones, y hara lo mayor posible, sin romper relacion
"""
compressedImg.thumbnail((400, 200))
print(compressedImg.size)
compressedImg.save("thumbnail.png", "png")