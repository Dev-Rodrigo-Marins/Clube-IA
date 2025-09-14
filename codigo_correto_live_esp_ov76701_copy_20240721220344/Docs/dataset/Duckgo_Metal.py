# encoding: utf-8

from bing_image_downloader import downloader

#query_string definer como a imagem a ser buscada
query_string = 'lixo'

#limit é a quantidade imagem para download.
#output_dir é a pasta que vai ser criada para salvar os arquivos.
#adult_filter filtra os conteudos adultos
#force_replace força a criação da pasta se ja existir alguma ele apaga e cria uma nova
#timeout tempo de espera por download
#verbose mostra tudo o que esta acontecendo enquanto o codigo esta sendo executado.

downloader.download(query_string, limit=500,  output_dir='lixo', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)
