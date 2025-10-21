# 🧠 Tracker Face & Fingers

Este proyecto combina **reconocimiento facial** con **detección de manos y conteo de dedos** en tiempo real usando la cámara del dispositivo.  
Integra tecnologías como **OpenCV**, **MediaPipe**, **face_recognition** y una interfaz gráfica simple con **Tkinter**.

---

## 🚀 Funcionalidades principales

- 🔍 Reconoce rostros previamente registrados en una carpeta local (`faces_db/`).
- ✋ Detecta manos y cuenta los dedos levantados usando MediaPipe.
- 🧰 Interfaz visual creada con Tkinter para mostrar video en tiempo real.
- ⚡ Procesamiento optimizado en frames reducidos (para mejor rendimiento).

---

## 🧩 Tecnologías usadas

- [OpenCV](https://opencv.org/) – procesamiento de imágenes y video.  
- [MediaPipe](https://developers.google.com/mediapipe) – detección de manos.  
- [face_recognition](https://github.com/ageitgey/face_recognition) – reconocimiento facial basado en `dlib`.  
- [Pillow](https://python-pillow.org/) – manipulación de imágenes para Tkinter.  
- [Tkinter](https://docs.python.org/3/library/tkinter.html) – interfaz gráfica simple.  
- [NumPy](https://numpy.org/) – operaciones matemáticas.

---

## 🎬 Video demostrativo

¿Quieres ver cómo funciona en acción?  
👉 **Mira el video en YouTube:**  
[![Ver en YouTube](https://img.shields.io/badge/YouTube%20-%20Ver%20demo%20🔴-ff0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/watch?v=HK5SWp8QyBU&authuser=1)

También puedes hacer clic directamente en el enlace:  
🔗 [https://www.youtube.com/watch?v=HK5SWp8QyBU&authuser=1](https://www.youtube.com/watch?v=HK5SWp8QyBU&authuser=1)


## 🧱 Instalación

### 1️⃣ Clonar el repositorio

Abre tu terminal (o Git Bash) y ejecuta:

```bash
git clone https://github.com/FernandoReyes04/Tracker_Face_Fingers.git
cd Tracker_Face_Fingers
```

---

## Crear carpeta 📁
Para que el proyecto almacene rostros de forma efectiva, se debe crear un folder con el nombre "faces_db" donde se almacenaran las caras que quiera almacenar en formato png/jpg.
