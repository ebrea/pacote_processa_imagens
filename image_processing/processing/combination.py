import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity

def find_difference(image1, image2):        # verifica se as imagens são iguais
    assert image1.shape == image2.shape, "Specify 2 images with de same shape."   # compara as imagens. Se for diferente, dá a mensagem
    gray_image1 = rgb2gray(image1)      # converte a imagem 1 para preto-e-branco (biblioteca rgb2gray do pacote skimage.color)
    gray_image2 = rgb2gray(image2)      # converte a imagem 2 para preto-e-branco
    (score, difference_image) = structural_similarity(gray_image1, gray_image2, full=True)  # achando o score (valor de 0 a 1) das imagens (pacote skimage.metrics)
    print("Similarity of the images:", score)
    normalized_difference_image = (difference_image-np.min(difference_image))/(np.max(difference_image)-np.min(difference_image))
    return normalized_difference_image

def transfer_histogram(image1, image2):  # Ajusta os tons de uma imagem para parecer com a outra.
    matched_image = match_histograms(image1, image2, multichannel=True)
    return matched_image


'''
1. Função find_difference(image1, image2) = Comparar duas imagens e mostrar as diferenças.
assert image1.shape == image2.shape
Garante que as imagens têm o mesmo tamanho e número de canais (ex: 512x512x3).
Se não for, gera erro.
structural_similarity(gray_image1, gray_image2, full=True)
Calcula a similaridade estrutural (SSIM), que retorna:

score = verifica o quanto as imagens são semelhantes
    um valor entre -1 e 1 (na prática, entre 0 e 1). 1.0 = imagens idênticas  0.0 = completamente diferentes

difference_image → uma imagem que destaca as diferenças entre as duas.
Isso ajusta os valores da imagem de diferença para variar de 0 a 1, facilitando a visualização.
Retorno: imagem normalizada que mostra onde há diferenças (para melhor plotagem)

2. Função transfer_histogram(image1, image2)
Objetivo: Ajustar os tons de uma imagem para parecer com a outra.

match_histograms(image1, image2, multichannel=True)
Ajusta a distribuição de cores da image1 para que se pareça com a de image2.
Isso é útil, por exemplo, quando duas imagens têm iluminação diferente.
Retorno: uma nova imagem (matched_image) com os histogramas de cor ajustados.

Em resumo:
find_difference → diz o quanto duas imagens são parecidas e gera uma imagem destacando diferenças.
transfer_histogram → faz uma correção de cores para que a primeira imagem tenha o mesmo estilo de 
iluminação/tons da segunda.

'''