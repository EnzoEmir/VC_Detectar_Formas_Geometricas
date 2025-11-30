import cv2
import numpy as np

# Carrega a imagem
imagem = cv2.imread('assets/13_frame_000001_t1.50s.jpg')
#imagem = cv2.imread('assets/13_frame_000004_t6.00s.jpg')

cv2.namedWindow('Meus Ajustes')

def nada(x):
    pass

# Barras para o H (Matiz - Cor)
cv2.createTrackbar('H Minimo', 'Meus Ajustes', 0, 179, nada) 
cv2.createTrackbar('H Maximo', 'Meus Ajustes', 179, 179, nada)

# Barras para o S (Saturação - Pureza da cor)
cv2.createTrackbar('S Minimo', 'Meus Ajustes', 0, 255, nada) 
cv2.createTrackbar('S Maximo', 'Meus Ajustes', 255, 255, nada)

# Barras para o V (Valor - Brilho/Luz)
cv2.createTrackbar('V Minimo', 'Meus Ajustes', 0, 255, nada)
cv2.createTrackbar('V Maximo', 'Meus Ajustes', 255, 255, nada)

# Loop que atualiza os valores dos trackbars
while True:
    h_min = cv2.getTrackbarPos('H Minimo', 'Meus Ajustes')
    h_max = cv2.getTrackbarPos('H Maximo', 'Meus Ajustes')
    s_min = cv2.getTrackbarPos('S Minimo', 'Meus Ajustes')
    s_max = cv2.getTrackbarPos('S Maximo', 'Meus Ajustes')
    v_min = cv2.getTrackbarPos('V Minimo', 'Meus Ajustes')
    v_max = cv2.getTrackbarPos('V Maximo', 'Meus Ajustes')

    minimo = np.array([h_min, s_min, v_min])
    maximo = np.array([h_max, s_max, v_max])

    hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
    
    mascara = cv2.inRange(hsv, minimo, maximo)

    cv2.imshow('Mascara', mascara)

    # Q para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

