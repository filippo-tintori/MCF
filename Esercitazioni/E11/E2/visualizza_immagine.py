from camera_module import read_camera
import matplotlib.pyplot as plt

try:
    image = read_camera()
    print("Immagine letta con successo!")
except RuntimeError as e:
    print(f"Errore: {e}")
    exit(1)

plt.imshow(image, cmap='gray')
plt.colorbar()
plt.title("Immagine dalla fotocamera")
plt.show()