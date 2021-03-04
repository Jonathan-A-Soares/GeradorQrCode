import qrcode

data = input("text:")
print(".png")
filename = input("Nome do arquivo:")
img = qrcode.make(data)
img.save(filename)
