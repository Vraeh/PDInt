import cv2
from facial_emotion_recognition import EmotionRecognition

# Inicializar el detector de emociones
emotion_recognition = EmotionRecognition(device='cpu')

# Inicializar la cámara (puedes ajustar el número según la cámara que estés utilizando)
cap = cv2.VideoCapture(0)

while True:
    # Capturar un frame
    ret, frame = cap.read()

    # Convertir el frame a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar caras en el frame
    faces = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml').detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Para cada cara detectada
    for (x, y, w, h) in faces:
        # Extraer la región de interés (ROI) para la detección de emociones
        roi = gray[y:y + h, x:x + w]

        # Detectar la emoción en la ROI
        emotion, confidence = emotion_recognition.recognize_emotion(roi)

        # Mostrar la emoción detectada en la consola
        print(f'Emoción: {emotion} - Confianza: {confidence}')

        # Si la emoción detectada es "feliz"
        if emotion == 'happy' and confidence > 0.5:
            pass  # Add your code here

    # Mostrar el frame con las caras marcadas
    cv2.imshow('PiCar-X Emotion Detection', frame)

    # Romper el bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar los recursos
cap.release()
cv2.destroyAllWindows()