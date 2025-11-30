import cv2
import numpy as np

video = 'assets/video_desafio_1.mp4'
video = cv2.VideoCapture(video)

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

is_paused = False
frame = None

# Loop que atualiza os valores dos trackbars
while True:
    key = cv2.waitKey(60) & 0xFF
    
    # Q para sair do loop
    if key == ord('q'):
        break

    # P para pausar/despausar
    if key == ord('p'):
        is_paused = not is_paused

    if not is_paused:
        ret, current_frame = video.read()
        if not ret:
            # Reiniciar o vídeo quando acabar
            video.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue
        frame = current_frame

    if frame is None:
        continue

    h_min = cv2.getTrackbarPos('H Minimo', 'Meus Ajustes')
    h_max = cv2.getTrackbarPos('H Maximo', 'Meus Ajustes')

    s_min = cv2.getTrackbarPos('S Minimo', 'Meus Ajustes')
    s_max = cv2.getTrackbarPos('S Maximo', 'Meus Ajustes')

    v_min = cv2.getTrackbarPos('V Minimo', 'Meus Ajustes')
    v_max = cv2.getTrackbarPos('V Maximo', 'Meus Ajustes')

    minimo = np.array([h_min, s_min, v_min])
    maximo = np.array([h_max, s_max, v_max])

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    mascara = cv2.inRange(hsv, minimo, maximo)

    cv2.imshow('Video Original', frame)
    cv2.imshow('Mascara', mascara)

video.release()
cv2.destroyAllWindows()
 