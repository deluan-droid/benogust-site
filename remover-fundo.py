from PIL import Image
import os

# Carregar a imagem
img_path = r"C:\BENOGUST\Site BenoGust\Midia\Whatsup PNG Liza.jpg"
img = Image.open(img_path)

# Converter para RGBA para suportar transparência
img = img.convert("RGBA")

# Obter os pixels
pixels = img.load()

# Cor branca (ou quase branca) a ser removida
white_threshold = 240

# Substituir branco por transparente
for y in range(img.height):
    for x in range(img.width):
        r, g, b, a = pixels[x, y]
        # Se o pixel é branco ou muito claro, tornar transparente
        if r > white_threshold and g > white_threshold and b > white_threshold:
            pixels[x, y] = (r, g, b, 0)

# Salvar como PNG com transparência
output_path = r"C:\BENOGUST\Site BenoGust\Midia\whatsapp-icon.png"
img.save(output_path, "PNG")

print("Imagem salva sem fundo em: " + output_path)
