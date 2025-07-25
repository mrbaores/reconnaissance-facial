import cv2
import mediapipe as mp
import time
import pyttsx3  

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

cap = cv2.VideoCapture(0)

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
index = 0
last_switch = time.time()

nose_y_positions = []
current_word = ""  

cooldown = 0  

engine = pyttsx3.init()  # Initialisation du moteur de voix

def detect_nod(y_positions):
    if len(y_positions) < 5:
        return False
    delta = y_positions[-1] - y_positions[0]
    if delta > 20:  # Ajuste si besoin
        return True
    return False

while True:
    success, img = cap.read()
    if not success:
        break

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(img_rgb)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:

            mp.solutions.drawing_utils.draw_landmarks(
                img, face_landmarks, mp_face_mesh.FACEMESH_CONTOURS)

            nose_landmark = face_landmarks.landmark[1]
            h, w, _ = img.shape
            nose_y = int(nose_landmark.y * h)
            nose_y_positions.append(nose_y)

            if len(nose_y_positions) > 10:
                nose_y_positions.pop(0)

            current_time = time.time()
            if detect_nod(nose_y_positions) and current_time > cooldown:

                current_word += alphabet[index]
                print(f"Lettre ajoutée : {alphabet[index]} ➔ Mot actuel : {current_word}")
                nose_y_positions.clear()  # Reset après détection

                cooldown = current_time + 1.5

    if time.time() - last_switch >= 1:
        index = (index + 1) % len(alphabet)
        last_switch = time.time()

    cv2.putText(img, f'Lettre: {alphabet[index]}', (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.putText(img, f'Mot: {current_word}', (50, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.putText(img, "Appuie 'v' pour valider le mot", (50, 150),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.putText(img,"Pour supprimer la lettre 'z'",(60,200),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8,(0,0,155),2)

    cv2.imshow('Alphabet Selector', img)


    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('v'):
        print(f"Mot final valide : {current_word}")
        engine.say(current_word)
        engine.runAndWait()  
        current_word = ""  
cap.release()
cv2.destroyAllWindows()
