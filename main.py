import cv2
import numpy as np
import face_recognition
import os
import mediapipe as mp
from PIL import Image, ImageTk
import tkinter as tk

# ------------------------------
# Función para contar dedos levantados
def contar_dedos(hand_landmarks):
    dedos = []

    # Pulgar: se compara x (por ser horizontal)
    if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
        dedos.append(1)
    else:
        dedos.append(0)

    # Índice, medio, anular, meñique: se compara y
    tips_ids = [8, 12, 16, 20]
    for tip in tips_ids:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            dedos.append(1)
        else:
            dedos.append(0)

    return sum(dedos)
# ------------------------------

# Cargar rostros conocidos
def load_face_db(path='faces_db'):
    encodings = []
    names = []
    for file in os.listdir(path):
        img_path = os.path.join(path, file)
        img = face_recognition.load_image_file(img_path)
        encoding = face_recognition.face_encodings(img)
        if encoding:
            encodings.append(encoding[0])
            names.append(os.path.splitext(file)[0])
    print("Rostros cargados:", names)
    return encodings, names

known_encodings, known_names = load_face_db()

# Inicializar MediaPipe Hands
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.7)

cap = cv2.VideoCapture(0)

# Procesamiento del frame
def video_loop():
    ret, frame = cap.read()
    if not ret:
        return

    frame = cv2.flip(frame, 1)

    # Redimensionar para procesamiento rápido
    small = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convertir a RGB
    rgb_small = cv2.cvtColor(small, cv2.COLOR_BGR2RGB)

    # Detectar rostros
    locations = face_recognition.face_locations(rgb_small)
    encodings = face_recognition.face_encodings(rgb_small, locations) if locations else []

    for (top, right, bottom, left), encoding in zip(locations, encodings):
        name = "Desconocido"
        matches = face_recognition.compare_faces(known_encodings, encoding)
        distances = face_recognition.face_distance(known_encodings, encoding)
        if len(distances) > 0:
            best = np.argmin(distances)
            if matches[best]:
                name = known_names[best]

        # Escalar coordenadas
        top, right, bottom, left = [i * 4 for i in (top, right, bottom, left)]

        # Dibujar rectángulo y etiqueta
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Detección de manos
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result_hands = hands.process(rgb_frame)

    if result_hands.multi_hand_landmarks and result_hands.multi_handedness:
        for hand_landmarks, handedness in zip(result_hands.multi_hand_landmarks, result_hands.multi_handedness):
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Contar dedos levantados
            dedos_levantados = contar_dedos(hand_landmarks)

            # Obtener si es mano izquierda o derecha
            label = handedness.classification[0].label  # 'Left' o 'Right'

            # Mostrar información en pantalla
            x = int(hand_landmarks.landmark[0].x * frame.shape[1])
            y = int(hand_landmarks.landmark[0].y * frame.shape[0])
            cv2.putText(frame, f"{label} - Dedos: {dedos_levantados}", (x, y - 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Mostrar en Tkinter
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(frame_rgb)
    imgtk = ImageTk.PhotoImage(image=img)
    panel.imgtk = imgtk
    panel.config(image=imgtk)
    panel.after(10, video_loop)

# Interfaz gráfica
root = tk.Tk()
root.title("Identificación Facial y Detección de Dedos")

panel = tk.Label(root)
panel.pack()

def salir():
    cap.release()
    root.destroy()

btn_salir = tk.Button(root, text="Salir", command=salir, bg='red', fg='white')
btn_salir.pack(pady=10)

video_loop()
root.mainloop()
