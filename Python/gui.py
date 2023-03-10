from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import serial


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"PASTA DO PROJETO\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title('App NUTES SMS')
window.iconbitmap('icon.ico')

def conectar():
    global conectado
    try:
        conectado = serial.Serial("DEFINIR COM PORT", 9600, timeout=0.5)
        print("Conctado com a porta:", conectado.portstr)
    except serial.SerialExecption:
        print("Porta USB não detectada!")

conectar()
print(conectado.isOpen())


def enviaSMS():
    numero=entry_2.get()
    numero = numero + "$"
    mensagem=entry_1.get()

    mensagemSerial = numero + mensagem
    conectado.write(mensagemSerial.encode())
    print("SMS Enviado: ", numero, mensagem)
    print(mensagemSerial)

window.geometry("446x927")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 927,
    width = 446,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    223.0,
    464.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=enviaSMS,
    relief="flat"
)
button_1.place(
    x=104.0,
    y=605.0,
    width=243.0,
    height=67.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    224.0,
    510.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#094E6F",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=101.0,
    y=469.0,
    width=246.0,
    height=80.0
)

canvas.create_text(
    87.0,
    392.0,
    anchor="nw",
    text="Mensagem de Texto",
    fill="#FFFFFF",
    font=("UbuntuCondensed Regular", 36 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    224.0,
    334.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#094E6F",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=101.0,
    y=309.0,
    width=246.0,
    height=48.0
)

canvas.create_text(
    156.0,
    244.0,
    anchor="nw",
    text="Telefone",
    fill="#FFFFFF",
    font=("UbuntuCondensed Regular", 36 * -1)
)

canvas.create_text(
    125.0,
    163.0,
    anchor="nw",
    text="App Envia SMS",
    fill="#FFFFFF",
    font=("UbuntuCondensed Regular", 36 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    223.0,
    66.0,
    image=image_image_2
)
window.resizable(False, False)
window.mainloop()
