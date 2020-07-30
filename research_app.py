import tkinter as tk
import main

class Application(tk.Tk):
    def __init__(self, research_name, menu_list):
        tk.Tk.__init__(self)
        self.title(research_name)
        self.mainloop()
        self.menu_list=menu_list
        self.back_to_main()
        self.entry=tk.Entry(self, text=research_name)
        self.entry.pack()
        self.search_button = tk.Button(self, text="recherche", command=t)
        self.search_button.pack()
    
    def t(self):
        menu_list = menudb.searchRecipe(menudb.init(), user.get_id(), self.search_entry_var.get(), vg=int(self.search_veg_var.get()), exp=self.search_expensive_var.get(), dif=self.search_difficuty_var.get())
        Application(self.search_entry_var.get(), menu_list)
        self.quit()
        
    def back_to_main(self):
        self.search_button = tk.Button(self, text="Back", command=self.quit)
        self.search_button.pack(side=tk.LEFT)
        app = main.Application()
        app.title("PyMenu")
        app.mainloop()
        