import tkinter as tk
import re

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("400x300")
        self.master.title("Cadastro de Cliente")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.name_label = tk.Label(self, text="Nome completo:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        self.age_label = tk.Label(self, text="Idade:")
        self.age_label.pack()
        self.age_entry = tk.Entry(self)
        self.age_entry.pack()

        self.marital_status_label = tk.Label(self, text="Estado civil:")
        self.marital_status_label.pack()
        self.marital_status_var = tk.StringVar(self)
        self.marital_status_var.set("Solteiro(a)")
        self.marital_status_menu = tk.OptionMenu(self, self.marital_status_var, "Solteiro(a)", "Casado(a)", "Divorciado(a)", "Viúvo(a)")
        self.marital_status_menu.pack()

        self.gender_label = tk.Label(self, text="Gênero:")
        self.gender_label.pack()
        self.gender_var = tk.StringVar(self)
        self.gender_var.set("Masculino")
        self.gender_menu = tk.OptionMenu(self, self.gender_var, "Masculino", "Feminino", "Não binário")
        self.gender_menu.pack()

        self.cpf_label = tk.Label(self, text="CPF:")
        self.cpf_label.pack()
        self.cpf_entry = tk.Entry(self)
        self.cpf_entry.pack()

        self.submit_button = tk.Button(self, text="Cadastrar", command=self.submit_form)
        self.submit_button.pack()

        self.error_label = tk.Label(self, fg="red")
        self.error_label.pack()

    def validate_name(self, name):
        
        if not re.match("^[a-zA-Z ]*$", name):
            return False
        return True

    def validate_age(self, age):
        
        if not age.isdigit() or len(age) > 2:
            return False

       
        if int(age) == 0 or age[0] == "0":
            return False

        return True

    def submit_form(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        marital_status = self.marital_status_var.get()
        gender = self.gender_var.get()
        cpf = self.cpf_entry.get()

        
        if not self.validate_name(name):
            self.error_label.config(text="Por favor, insira um nome válido!")
            return
        if not self.validate_age(age):
            self.error_label.config(text="Por favor, insira uma idade válida!")
            return
        if not cpf.isdigit() or len(cpf) != 11:
            self.error_label.config(text="Por favor, insira um CPF válido!")
            return
        if not cpf.isdigit():
            self.error_label.config(text="Por favor, insira um CPF válido!")
            return

    
        info_window = tk.Toplevel(self.master)
        info_window.title("Informações do Cliente")

        
        info_window.geometry("400x300")

        
        name_label = tk.Label(info_window, text=f"Nome: {name}")
        name_label.pack(pady=5)

        age_label = tk.Label(info_window, text=f"Idade: {age}")
        age_label.pack(pady=5)

        marital_status_label = tk.Label(info_window, text=f"Estado Civil: {marital_status}")
        marital_status_label.pack(pady=5)

        gender_label = tk.Label(info_window, text=f"Gênero: {gender}")
        gender_label.pack(pady=5)

        cpf_label = tk.Label(info_window, text=f"CPF: {cpf}")
        cpf_label.pack(pady=5)

       
        close_button = tk.Button(info_window, text="Fechar", command=info_window.destroy)
        close_button.pack(pady=20)


root = tk.Tk()
app = Application(master=root)
app.mainloop()