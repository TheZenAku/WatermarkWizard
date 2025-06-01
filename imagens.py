from PIL import Image
import os

# Caminhos
pasta_origem = r"PASTA DE ORIGEM"
pasta_destino = os.path.join(pasta_origem, "com_disclaimer")
disclaimer_path = r"ARQUIVO DE IMAGEM DO DISCLAIMER"

# Garante que a pasta de saída exista
os.makedirs(pasta_destino, exist_ok=True)

# Abre o disclaimer original
disclaimer = Image.open(disclaimer_path)

# Percorre todos os arquivos .jpg na pasta
for nome_arquivo in os.listdir(pasta_origem):
    if nome_arquivo.lower().endswith(".jpg"):
        caminho_imagem = os.path.join(pasta_origem, nome_arquivo)
        imagem = Image.open(caminho_imagem)

        # Redimensiona o disclaimer para ter a mesma largura da imagem
        largura = imagem.width
        proporcao = largura / disclaimer.width
        altura_disclaimer = int(disclaimer.height * proporcao)
        disclaimer_redimensionado = disclaimer.resize((largura, altura_disclaimer))

        # Cria nova imagem maior para colocar o disclaimer + imagem original
        nova_altura = imagem.height + altura_disclaimer
        nova_imagem = Image.new("RGB", (largura, nova_altura), (255, 255, 255))

        # Cola o disclaimer no topo e depois a imagem
        nova_imagem.paste(disclaimer_redimensionado, (0, 0))
        nova_imagem.paste(imagem, (0, altura_disclaimer))

        # Salva a nova imagem na pasta de destino
        caminho_destino = os.path.join(pasta_destino, nome_arquivo)
        nova_imagem.save(caminho_destino)

print("✅ Todas as imagens foram processadas com sucesso!")
