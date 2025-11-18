import cv2
import numpy as np

# Carrega a imagem
imagem = cv2.imread('assets/13_frame_000001_t1.50s.jpg')

# Mostra a imagem na tela
cv2.imshow('Minha Imagem', imagem)

# RBG para HSV 
imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
cv2.imshow('Convertida (HSV)', imagem_hsv)


# Valores de azul
azul_minimo = np.array([100, 100, 50])
azul_maximo = np.array([140, 255, 255])

mascara = cv2.inRange(imagem_hsv, azul_minimo, azul_maximo)
cv2.imshow('Mascara', mascara)

# Deixa a janela aberta
cv2.waitKey(0)