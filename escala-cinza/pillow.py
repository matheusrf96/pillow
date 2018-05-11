#coding: utf-8

from PIL import Image
import os

# img = Image.open("migos.jpg")

# img = img.rotate(180)
# img.save("migos-ate-de-cabeca-para-baixo.jpg")

# img.show()

def novaImagem(nome):
    tamanho = (400, 400)

    imagem = Image.open(nome)
    nova = imagem.convert("L")
    nova = nova.resize(tamanho)

    nova.save("NOVA-"+nome)

    nova.show()

directory = "/var/www/html/img/escala-cinza/"

for filename in os.listdir(directory):
    if filename.endswith(".jpg"): 
        #print(os.path.join(directory, filename))     
        print(os.path.join(filename))     
        novaImagem(os.path.join(filename))