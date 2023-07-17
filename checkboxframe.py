import customtkinter

class ScrollableCheckboxFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, title, values):
        super().__init__(master, label_text=title)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.checkboxes = []

        for i, ext in enumerate(self.values):
            checkbox = customtkinter.CTkCheckBox(self, text=ext)
            checkbox.grid(row=i+1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkbox)

    def get(self):
        checked_checkboxes = {}
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked = checkbox.cget("text")
                checked_checkboxes[checked] = self.values[checked]
        print(self.values)
        return checked_checkboxes