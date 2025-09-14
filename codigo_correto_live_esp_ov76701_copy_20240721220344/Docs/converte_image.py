from PIL import Image

# Carrega a imagem original
image = Image.open('/home/rodrigo/Arduino/Octos/codigo_correto_live_esp_ov76701_copy_20240721220344/Imagens/imagem7.jpg')

# Redimensiona a imagem
resized_image = image.resize((320, 480))

# Salva a imagem redimensionada
resized_image.save('/home/rodrigo/Arduino/Octos/codigo_correto_live_esp_ov76701_copy_20240721220344/Imagens/imagem_redimensionada.jpg')
