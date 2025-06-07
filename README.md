# Breast Cancer Detection with CNNs

Dieses Repository enthält Code und Notebooks zur Erkennung von Brustkrebs mithilfe von Convolutional Neural Networks (CNNs).

## Projektstruktur

```
.
├── .gitignore
├── cnn_breastcancer_pytorch.ipynb
├── CNN_model_pytorch_weights.pth
├── LICENSE
├── README.md
├── keras/
│   ├── Breast_Cancer_Detection_using_CNN.ipynb
│   └── CNN_model.h5
├── misc/
│   ├── 8th-sem-major-project.ipynb
│   ├── breast-cancer-imageclassification.ipynb
│   ├── breast-histopathology-images.py
│   └── cbis-ddsm-breast-cancer-image-dataset-training.ipynb
└── urls/
    ├── url-breast-histopathology-images.txt
    ├── url-cancer-cnn.txt
    ├── url-cbis-ddsm-breast-cancer-image-dataset.txt
    └── url-miniddsm2.txt
```

## Jupyter Notebooks

### `cnn_breastcancer_pytorch.ipynb`

Dieses Notebook implementiert ein Convolutional Neural Network (CNN) mit PyTorch zur Klassifizierung von Brustkrebsbildern. Es behandelt wahrscheinlich die folgenden Schritte:

*   **Datenvorbereitung:** Laden und Vorverarbeiten der Bilddaten. Dies kann das Augmentieren von Daten, Normalisieren und Aufteilen in Trainings-, Validierungs- und Testdatensätze umfassen.
*   **Modellarchitektur:** Definition der CNN-Architektur, einschließlich Convolutional Layers, Pooling Layers, Fully Connected Layers und Aktivierungsfunktionen.
*   **Training:** Trainieren des Modells mit den vorbereiteten Daten. Dies beinhaltet die Definition einer Verlustfunktion und eines Optimierers sowie die Durchführung von Trainingsiterationen.
*   **Evaluierung:** Bewertung der Leistung des trainierten Modells anhand von Metriken wie Genauigkeit, Präzision, Recall und F1-Score.
*   **Vorhersage:** Verwendung des trainierten Modells zur Vorhersage bei neuen Bildern.

Die trainierten Gewichte für dieses Modell könnten in `CNN_model_pytorch_weights.pth` gespeichert sein.

### Weitere Notebooks

*   **[`keras/Breast_Cancer_Detection_using_CNN.ipynb`](keras/Breast_Cancer_Detection_using_CNN.ipynb):** Ein ähnliches Notebook, das Keras anstelle von PyTorch für die CNN-Implementierung verwendet. Die zugehörigen Gewichte könnten in [`keras/CNN_model.h5`](keras/CNN_model.h5) gespeichert sein.
*   **[`misc/8th-sem-major-project.ipynb`](misc/8th-sem-major-project.ipynb):** Ein Notebook, das wahrscheinlich im Rahmen eines Studienprojekts erstellt wurde.
*   **[`misc/breast-cancer-imageclassification.ipynb`](misc/breast-cancer-imageclassification.ipynb):** Ein weiteres Notebook zur Bildklassifizierung von Brustkrebs.
*   **[`misc/cbis-ddsm-breast-cancer-image-dataset-training.ipynb`](misc/cbis-ddsm-breast-cancer-image-dataset-training.ipynb):** Ein Notebook, das sich speziell auf das Training mit dem CBIS-DDSM-Datensatz konzentriert.

## Datensätze

Das Skript [`misc/breast-histopathology-images.py`](misc/breast-histopathology-images.py) scheint mit den folgenden Datensätzen zu arbeiten, um Bilder zu zählen und zu verwalten:

1.  **`breast-histopathology-images`**: Enthält histopathologische Bilder im PNG-Format. (Siehe [`urls/url-breast-histopathology-images.txt`](urls/url-breast-histopathology-images.txt))
2.  **`MINI-DDSM-Complete-PNG-16`**: Enthält Mammographiebilder im PNG-Format, unterteilt in "Benign" und "Cancer". (Siehe [`urls/url-miniddsm2.txt`](urls/url-miniddsm2.txt))
3.  **`cbis-ddsm-breast-cancer-image-dataset`**: Enthält Mammographiebilder im JPEG-Format. (Siehe [`urls/url-cbis-ddsm-breast-cancer-image-dataset.txt`](urls/url-cbis-ddsm-breast-cancer-image-dataset.txt))

Das Skript [`misc/breast-histopathology-images.py`](misc/breast-histopathology-images.py) enthält die Funktion [`_count_dataset_images`](misc/breast-histopathology-images.py), um die Anzahl der Bilder in diesen Datensätzen zu ermitteln.

## Hilfsskripte

*   **[`misc/breast-histopathology-images.py`](misc/breast-histopathology-images.py):** Ein Python-Skript zum Zählen und potenziell Verwalten von Bildern aus verschiedenen Brustkrebs-Datensätzen. Es kann sowohl lokal als auch in einer Google Drive-Umgebung ausgeführt werden.

## URLs

Der Ordner `urls/` enthält Textdateien mit Links zu den verwendeten Datensätzen und möglicherweise zu relevanten Kaggle-Notebooks oder Ressourcen:

*   [`urls/url-breast-histopathology-images.txt`](urls/url-breast-histopathology-images.txt)
*   [`urls/url-cancer-cnn.txt`](urls/url-cancer-cnn.txt)
*   [`urls/url-cbis-ddsm-breast-cancer-image-dataset.txt`](urls/url-cbis-ddsm-breast-cancer-image-dataset.txt)
*   [`urls/url-miniddsm2.txt`](urls/url-miniddsm2.txt)

## Lizenz

Siehe die Datei `LICENSE` für Lizenzinformationen.