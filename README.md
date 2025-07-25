# 🧠 Détecteur Alphabet – Application de reconnaissance faciale pour l’accessibilité

## 📌 Description

Cette application Python permet aux **personnes en situation de handicap** ayant des difficultés d’élocution ou d’expression verbale de **composer des mots grâce aux mouvements de leur tête**.

### 🔍 Fonctionnement

1. L’application affiche l’alphabet en défilement automatique.
2. L’utilisateur **hoche la tête** pour sélectionner la lettre affichée.
3. Les lettres choisies sont ajoutées pour former un mot.
4. Le mot est lu à haute voix grâce à un moteur de synthèse vocale.

---
## fonctionnement 
1. telecharge le script
2. Autorise l’accès à la webcam.
3. Suis les instructions affichées :
    L’alphabet défile automatiquement (1 lettre par seconde).
    Hoche la tête pour sélectionner la lettre affichée.
    Appuie sur “v” pour valider le mot complet et l’entendre.
    Appuie sur “q” pour quitter l’application.

---
## ⚙️ Technologies utilisées

- [Python](https://www.python.org/)  
- [OpenCV](https://opencv.org/) – capture vidéo en temps réel  
- [MediaPipe](https://google.github.io/mediapipe/) – détection du visage et suivi du nez  
- [pyttsx3](https://pypi.org/project/pyttsx3/) – synthèse vocale hors ligne

---
 ## Dependances 
- pip install opencv-python mediapipe pyttsx3

---

 ## 🛠️ Contribuer
 Les contributions sont les bienvenues !

---
## 🚀 Installation

1. **Clone le projet :**

```bash
git clone https://github.com/mrbaores/detecteur_alphabet.git
cd detecteur_alphabet

---
## 📄 Licence

Ce projet est sous licence MIT

