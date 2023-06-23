import os
import shutil
import tkinter as tk
from tkinter import filedialog

username=""
if os.name == 'nt':  # Windows
    username = os.environ['USERNAME']
else:  # Unix/Linux/Mac
    username = os.environ['USER']

cartella_origine = f'C:/Users/{username}/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets'
print(cartella_origine)
# Crea una finestra tkinter
root = tk.Tk()
root.withdraw()  # Nascondi la finestra principale

# Mostra il dialogo per la selezione della cartella
cartella_destinazione = filedialog.askdirectory()
print(cartella_destinazione)


file_da_copiare = os.listdir(cartella_origine)

# Copia i file uno per uno nella cartella di destinazione
for file in file_da_copiare:
    percorso_origine = os.path.join(cartella_origine, file)
    percorso_destinazione = os.path.join(cartella_destinazione, file)
    shutil.copy2(percorso_origine, percorso_destinazione)
    if os.path.isfile(percorso_destinazione):  # Verifica se è un file (esclude le cartelle)
        nuovo_nome = file + '.jpg'
        nuovo_percorso_destinazione = os.path.join(cartella_destinazione, nuovo_nome)
        os.rename(percorso_destinazione, nuovo_percorso_destinazione)


print(f"Immagini salvate nella cartella {cartella_destinazione} con successo")

