import cv2

# Carrega a imagem
imagem = cv2.imread('assets/13_frame_000001_t1.50s.jpg')

# Mostra a imagem na tela
cv2.imshow('Minha Imagem', imagem)

# RBG para HSV 
imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
cv2.imshow('Convertida (HSV)', imagem_hsv)

# Deixa a janela aberta
cv2.waitKey(0)