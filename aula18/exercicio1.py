import tkinter as tk

# Função para enviar os dados
def enviar():
    nome = entry_nome.get()
    idade = entry_idade.get()
    email = entry_email.get()
    endereco = entry_endereco.get()
    celular = entry_celular.get()
    cep = entry_cep.get()
    cidade = entry_cidade.get()
    cursos = entry_cursos.get()

    print("----- Dados do Cliente -----")
    print("Nome:", nome)
    print("Idade:", idade)
    print("E-mail:", email)
    print("Endereço:", endereco)
    print("Celular:", celular)
    print("CEP:", cep)
    print("Cidade:", cidade)
    print("Cursos:", cursos)

# Criando a janela
janela = tk.Tk()
janela.title("Cadastro de Clientes")
janela.geometry("1700x750")

# Campos do formulário
tk.Label(janela, text="Nome").pack()
entry_nome = tk.Entry(janela, width=50)
entry_nome.pack()

tk.Label(janela, text="Idade").pack()
entry_idade = tk.Entry(janela, width=50)
entry_idade.pack()

tk.Label(janela, text="E-mail").pack()
entry_email = tk.Entry(janela, width=50)
entry_email.pack()

tk.Label(janela, text="Endereço").pack()
entry_endereco = tk.Entry(janela, width=50)
entry_endereco.pack()

tk.Label(janela, text="Celular").pack()
entry_celular = tk.Entry(janela, width=50)
entry_celular.pack()

tk.Label(janela, text="CEP").pack()
entry_cep = tk.Entry(janela, width=50)
entry_cep.pack()

tk.Label(janela, text="Cidade").pack()
entry_cidade = tk.Entry(janela, width=50)
entry_cidade.pack()

tk.Label(janela, text="Cursos").pack()
entry_cursos = tk.Entry(janela, width=50)
entry_cursos.pack()

# Botão enviar
botao = tk.Button(janela, text="Enviar", command=enviar)
botao.pack(pady=20)

# Rodar o programa
janela.mainloop()
