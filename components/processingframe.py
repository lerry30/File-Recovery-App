import customtkinter

class ProcessingFrame(customtkinter.CTkFrame):
    def __init__(self, master, title, callback):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.title = title

        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(90, 4), sticky="ew")

        self.button = customtkinter.CTkButton(self, text="STOP", fg_color="darkred", command=callback)
        self.button.grid(row=2, column=0, padx=10, pady=(0, 0), sticky="ew", columnspan=2)