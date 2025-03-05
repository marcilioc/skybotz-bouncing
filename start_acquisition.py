import numpy as np
from detect_shapes import detectShapes
import cv2

cap = cv2.VideoCapture(0)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
    ret, frame = cap.read()

    # Aplica a detecção de formas geométricas na imagem recebida
    frame = detectShapes(frame)

    # Adicionar texto no canto superior esquerdo com fundo preto
    cv2.putText(frame, "Mission: Bouncing", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

    # Inscrição "Skybotz" no canto superior direito com fundo preto
    text = "Skybotz"
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    thickness = 2
    (text_width, text_height), baseline = cv2.getTextSize(text, font, font_scale, thickness)
    x = frame_width - text_width - 20
    y = 30
    padding = 5
    
    cv2.rectangle(frame, (x - padding, y - text_height - padding), (x + text_width + padding, y + baseline + padding), (0, 0, 0), -1)

    cv2.putText(frame, text, (x, y), font, font_scale, (255, 255, 0), thickness)

    # Mostra a imagem com o nome especificado na janela
    cv2.imshow('Geometric shapes', frame)
    
    # Sair ao pressionar 'q'
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
