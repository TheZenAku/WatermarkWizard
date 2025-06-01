# WatermarkWizard

## Sobre o projeto
WatermarkWizard é um script em Python projetado para adicionar uma imagem de disclaimer no topo de arquivos JPG armazenados em um diretório do Windows. Isso pode ser útil para inserir marcas d'água, avisos legais ou outras sobreposições informativas.

O script digitaliza a pasta de origem, redimensiona o disclaimer para corresponder à largura das imagens e combina os dois em uma nova imagem processada.

## Requisitos
- Python 3.x
- Biblioteca `Pillow`

## Instalação
Clone o repositório e instale as dependências necessárias:

```bash
git clone https://github.com/TheZenAku/WatermarkWizard.git
cd WatermarkWizard
pip install -r requirements.txt