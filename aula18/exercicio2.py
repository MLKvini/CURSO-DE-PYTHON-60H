import tkinter as tk
from PIL import Image, ImageTk


janela = tk.Tk()
janela.title("Atendimento Hospital")
janela.geometry("1500x1500")

frame_principal = tk.Frame(janela, padx=20, pady=20)
frame_principal.pack()


try:
    img = Image.open("j2.png")   
    img = img.resize((200, 200), Image.LANCZOS)
    tk_img = ImageTk.PhotoImage(img)

    label_imagem = tk.Label(frame_principal, image=tk_img)
    label_imagem.image = tk_img
    label_imagem.pack(pady=10)

except FileNotFoundError:
    print("Erro: O arquivo 'j2.png' não foi encontrado.")



tk.Label(frame_principal, text="Nome").pack()
entry_nome = tk.Entry(frame_principal, width=40)
entry_nome.pack(pady=5)

tk.Label(frame_principal, text="Email").pack()
entry_email = tk.Entry(frame_principal, width=40)
entry_email.pack(pady=5)

tk.Label(frame_principal, text="Telefone").pack()
entry_telefone = tk.Entry(frame_principal, width=40)
entry_telefone.pack(pady=5)

tk.Label(frame_principal, text="Especialidade").pack()
entry_especialidade = tk.Entry(frame_principal, width=40)
entry_especialidade.pack(pady=5)


def enviar():
    print("Nome:", entry_nome.get())
    print("Email:", entry_email.get())
    print("Telefone:", entry_telefone.get())
    print("Especialidade:", entry_especialidade.get())


botao = tk.Button(frame_principal, text="Enviar", command=enviar)
botao.pack(pady=20)

janela.mainloop()
