import tkinter as tk
from client import * 
import menudb
import research_app

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.client_info()
        self.search()
        self.magic_search()
        

    def client_info(self):
        self.client_info_label = tk.Label(self, text="PyMenu")
        self.client_info_label.pack()

    def search(self):
        self.search_entry_var=tk.StringVar()
        self.search_entry = tk.Entry(self, textvariable=self.search_entry_var)
        self.search_entry.pack()
        
        self.search_veg_var=tk.StringVar()
        self.search_veg_var.set(0)
        self.search_veg_checkbutton = tk.Checkbutton(self,  text = "Veg", variable = self.search_veg_var, onvalue = 1, offvalue = 0)
        self.search_veg_checkbutton.pack()
        
        self.search_difficuty_label=tk.Label(self, text="Price:")
        self.search_difficuty_label.pack()
        self.search_difficuty_var = tk.StringVar()
        self.search_difficuty_var.set(4)
        for i in range(1, 5):
            self.b = tk.Radiobutton(self, variable=self.search_difficuty_var, text=i, value=i)
            self.b.pack()
        
        self.search_expensive_label=tk.Label(self, text="Price:")
        self.search_expensive_label.pack()
        self.search_expensive_var = tk.StringVar()
        self.search_expensive_var.set(3)
        for i in range(1, 4):
            self.b = tk.Radiobutton(self, variable=self.search_expensive_var, text=i, value=i)
            self.b.grid_rowconfigure(i)
            self.b.pack()
        
        self.search_button = tk.Button(self, text="recherche", command=self.f)
        self.search_button.pack()
        
    def f(self):
        menu_list = menudb.searchRecipe(menudb.init(), user.get_id(), self.search_entry_var.get(), vg=int(self.search_veg_var.get()), exp=self.search_expensive_var.get(), dif=self.search_difficuty_var.get())
        research_app.Application(self.search_entry_var.get(), menu_list)
        self.quit()
        
    def magic_search(self):
        self.magic_search_button = tk.Button(self, text="Magic Search")
        self.magic_search_button.pack()
        
if __name__ == "__main__":
    app = Application()
    app.title("PyMenu")
    app.mainloop()