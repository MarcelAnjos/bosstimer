from tkinter import *
import time
import threading
from PIL import Image, ImageTk, ImageDraw
import pygame

# Inicializar o mixer do pygame para tocar o áudio
pygame.mixer.init()

def play_alarm():
    """Função para tocar o alarme duas vezes seguidas."""
    for _ in range(1):  # Toca o alarme duas vezes
        pygame.mixer.music.load('alarme.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(1)

def create_timer_button(parent, image, row, column, duration=900):
    var = IntVar()
    stop_event = threading.Event()

    def display():
        if var.get() == 0:
            stop_event.set()  # Para o temporizador
            check_button.config(text="00:00")
        else:
            stop_event.clear()  # Reinicia o evento para permitir que o temporizador continue

            def run_timer():
                for x in range(duration, -1, -1):
                    if stop_event.is_set():  # Verifica se o temporizador foi parado
                        break
                    seconds = x % 60
                    minutes = int(x / 60) % 60
                    check_button.config(text=f"{minutes:02}:{seconds:02}")
                    parent.update()
                    time.sleep(1)

                if not stop_event.is_set():  # Tocar o alarme se o temporizador não foi parado
                    play_alarm()
                    check_button.config(text="00:00")
                    var.set(0)

            # Inicia um novo temporizador em uma thread separada
            timer_thread = threading.Thread(target=run_timer)
            timer_thread.start()

    check_button = Checkbutton(parent,
                               text="00:00",
                               variable=var,
                               onvalue=1,
                               offvalue=0,
                               command=display,
                               font=('Arial', 14),
                               fg='#00FF00',
                               activeforeground='#00FF00',
                               padx=15,
                               pady=5,
                               image=image,
                               compound='top',
                               bg='black',
                               activebackground='black',
                               highlightthickness=0,
                               relief='flat',
                               borderwidth=0)
    check_button.grid(row=row, column=column, padx=5, pady=5)

def create_image_label(parent, image, row, column):
    label = Label(parent, image=image, bg='black')
    label.grid(row=row, column=column, padx=5, pady=5)

window = Tk()
window.title("BOSS TIMER METACENE")

# Define o tamanho fixo da janela
window.geometry("800x800")
window.resizable(False, False)

# Configurações de grid para centralizar os widgets
for i in range(8):
    window.columnconfigure(i, weight=1)
for i in range(8):
    window.rowconfigure(i, weight=1)

# Carregar a imagem de fundo
try:
    background_image = Image.open('CAPA.PNG')
    background_image = background_image.resize((800, 800), Image.LANCZOS)
    background_photo = ImageTk.PhotoImage(background_image)
except Exception as e:
    print(f"Erro ao carregar a imagem de fundo: {e}")
    background_photo = None

if background_photo:
    background_label = Label(window, image=background_photo)
    background_label.place(relwidth=1, relheight=1)
else:
    window.configure(bg='black')

# Função para processar a imagem
def process_image(image_path, size=(80, 80), border_size=0, rounded=True):
    try:
        image = Image.open(image_path).convert("RGBA")
        if rounded:
            mask = Image.new('L', size, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0) + size, fill=255)
            image = image.resize(size, Image.LANCZOS)
            image.putalpha(mask)
            border_image = Image.new("RGBA", (size[0] + border_size*2, size[1] + border_size*2), (255, 255, 255, 0))
            border_mask = Image.new('L', (size[0] + border_size*2, size[1] + border_size*2), 0)
            border_draw = ImageDraw.Draw(border_mask)
            border_draw.ellipse((border_size, border_size, size[0] + border_size, size[1] + border_size), fill=255)
            border_image.putalpha(border_mask)
            border_image.paste(image, (border_size, border_size), image)
            return ImageTk.PhotoImage(border_image)
        else:
            image = image.resize(size, Image.LANCZOS)
            return ImageTk.PhotoImage(image)
    except Exception as e:
        print(f"Erro ao processar a imagem {image_path}: {e}")
        return None

# Carregar as imagens
images = []
for i in range(1, 33):
    image_path = f'foto{i}.png'
    rounded = (i <= 21)
    size = (100, 100) if i == 23 else (120, 120)
    processed_image = process_image(image_path, size=size, rounded=rounded)
    if processed_image:
        images.append(processed_image)
    else:
        print(f"Erro ao carregar a imagem: {image_path}")

# Definir o ícone da janela
try:
    icon_image = process_image('foto25.png', size=(32, 32), rounded=True)
    if icon_image:
        window.iconphoto(False, icon_image)
except Exception as e:
    print(f"Erro ao definir o ícone da janela: {e}")

# Criar os Checkbuttons e Labels
if len(images) == 32:
    index = 0
    for i in range(5):
        for j in range(5):
            if index < len(images):
                if index == 4 or index == 18 or index == 19:  # Checkbox 5, 19, e 20 com 1800 segundos (30 minutos)
                    create_timer_button(window, images[index], i, j, duration=1800)
                elif index < 21:
                    create_timer_button(window, images[index], i, j)
                else:
                    create_image_label(window, images[index], i, j)
            index += 1
else:
    print("Erro: Nem todas as imagens foram carregadas corretamente.")

window.mainloop()
