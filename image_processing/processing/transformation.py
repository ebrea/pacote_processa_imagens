# redimencionando as imagens

from skimage.transform import resize

def resize_image(image, proportion):
    assert 0 <= proportion <= 1, "Specify a valid proportion between 0 and 1."
    height = round(image.shape[0] * proportion)
    width = round(image.shape[1] * proportion)
    image_resized = resize(image, (height, width), anti_aliasing=True)
    return image_resized


'''
Função resize_image(image, proportion)
Entrada:
image: a imagem original (matriz NumPy, geralmente 2D para PB ou 3D para RGB).
proportion: um valor entre 0 e 1 que indica o fator de redução. 
    1.0 → mantém o tamanho original
    0.5 → reduz para metade da altura e da largura
    0.25 → reduz para ¼ do tamanho
    
Resumo:
Essa função pega uma imagem e reduz seu tamanho proporcionalmente, preservando a proporção da altura e largura.
É útil, por exemplo, para diminuir imagens antes de comparar (find_difference) ou antes de treinar um modelo 
de visão computacional.


'''