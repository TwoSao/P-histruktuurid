import customtkinter as ctk
from ui import loo_ui, valmistu

app = ctk.CTk()
app.geometry("800x500")
app.title("PhotoRobot")

valmistu()
loo_ui(app)

app.mainloop()
