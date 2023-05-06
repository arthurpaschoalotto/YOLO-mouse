import cv2
import torch
import datetime

# Carrega o modelo YOLOv5 treinado, só localiza o path com o arquivo de treino
model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')

# Define as classes de objetos que o modelo é capaz de detectar
classes = ['classe1']

# Inicializa a webcam
cap = cv2.VideoCapture(0)

while True:
    # Lê o frame mais recente da webcam
    ret, frame = cap.read()

    # Converte o frame para o formato de entrada do modelo (BGR -> RGB)
    input_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Executa a detecção de objetos no frame usando o modelo YOLOv5
    results = model(input_img)

    # Extrai as coordenadas e as classes dos objetos detectados
    detections = results.xyxy[0]
    detections = detections[detections[:, 4] > 0.5] # filtra detecções com confiança > 0.5
    boxes = detections[:, :4].cpu().numpy().astype(int)
    classes_detected = detections[:, 5].cpu().numpy().astype(int)

    # Desenha retângulos em volta dos objetos detectados
    for box, cls in zip(boxes, classes_detected):
        x1, y1, x2, y2 = box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
        cv2.putText(frame, classes[cls], (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
###############################################################
        # Captura uma imagem da webcam
        #ret, frame = cap.read()

        # Define o nome do arquivo de saída
        #filename = 'imagem_' + str(datetime.now().strftime("%Y%m%d_%H%M%S")) + '.jpg'

        # Posta o arquivo

        # Exibe uma mensagem de confirmação
        # print('Imagem salva como', filename)
###############################################################

    # Exibe o frame com as detecções na tela
    cv2.imshow('YOLOv5 Detection', frame)

    # Aguarda a tecla 'q' ser pressionada para encerrar o programa
    if cv2.waitKey(1) == ord('q'):
        break

# Libera os recursos utilizados pela webcam e fecha as janelas
cap.release()
cv2.destroyAllWindows()