import tkinter as tk

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.setup_ui() # Call a method to set up initial UI or screens

    def setup_ui(self):
        # Example: a button to call the cadastro method
        cadastro_button = tk.Button(self.root, text="Abrir Cadastro", command=self.cadastro)
        cadastro_button.pack()

    def cadastro(self):
        # This method should define and display the registration UI elements
        # For example, creating a new Toplevel window for registration
        cadastro_window = tk.Toplevel(self.root)
        cadastro_window.title("Cadastro")
        cadastro_window.geometry("300x200")

        tk.Label(cadastro_window, text="Nome:").pack()
        tk.Entry(cadastro_window).pack()
        tk.Button(cadastro_window, text="Salvar").pack()

    def run(self):
        self.root.mainloop() # Call mainloop once to start the application

app = App()
app.run()