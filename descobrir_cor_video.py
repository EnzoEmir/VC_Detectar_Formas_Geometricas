import cv2
import numpy as np

video = 'assets/video_desafio_1.mp4'
video = cv2.VideoCapture(video)

while True:
    key = cv2.waitKey(60) & 0xFF
    
    # Q para sair do loop
    if key == ord('q'):
        break

    # P para pausar e ir direto para seleção
    if key == ord('p'):
        ret, frame = video.read()
        if ret:
            cv2.destroyWindow("Video Original")
            bbox = cv2.selectROI("Selecione a Cor", frame, showCrosshair=True)
            cv2.destroyWindow("Selecione a Cor")
            
            # Verificar se algo foi selecionado
            if bbox[2] > 0 and bbox[3] > 0:
                x, y, w, h = bbox
                
                recorte = frame[y:y+h, x:x+w]
                
                recorte_hsv = cv2.cvtColor(recorte, cv2.COLOR_BGR2HSV)
                
                min_hsv = np.min(recorte_hsv, axis=(0,1))
                max_hsv = np.max(recorte_hsv, axis=(0,1))
                
                print(f"Minimo: np.array([{min_hsv[0]}, {min_hsv[1]}, {min_hsv[2]}])")
                print(f"Maximo: np.array([{max_hsv[0]}, {max_hsv[1]}, {max_hsv[2]}])")
                
                cv2.waitKey(0)
                break

    ret, frame = video.read()
    if not ret:
        # Reiniciar o vídeo quando acabar
        video.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    cv2.imshow('Video Original', frame)

video.release()
cv2.destroyAllWindows()
