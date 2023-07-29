import customtkinter
from checkboxframe import ScrollableCheckboxFrame
from radiobuttonframe import RadiobuttonFrame
from processingframe import ProcessingFrame

from disk import get_drives
from recover import RecoverFiles

from multiprocessing import Process, cpu_count

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.destinationPath: str = "C:/recovered-files"
        file_extensions = [ "JPG", "PNG", "PDF" ]

        self.process = None
        self.processing_frame: customtkinter.CTkFrame | None = None

        self.title("FrankensFile")
        self.geometry("400x300")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.radiobutton_frame = RadiobuttonFrame(self, "Drives", values=get_drives())
        self.radiobutton_frame.grid(row=0, column=0, padx=(10, 0), pady=(10, 0), sticky="nsew")

        self.checkbox_frame = ScrollableCheckboxFrame(self, "File Types", values=file_extensions)
        self.checkbox_frame.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="nsew")

        self.destPath = customtkinter.CTkLabel(self, text=self.destinationPath, fg_color="gray30", corner_radius=6)
        self.destPath.grid(row=3, column=0, padx=10, pady=(10, 0), sticky="w", columnspan=2)

        self.button = customtkinter.CTkButton(self, text="Choose the destination path for the files.", fg_color="#062f4f", command=self.open_file_explorer)
        self.button.grid(row=4, column=0, padx=10, pady=(10, 0), sticky="ew", columnspan=2)

        self.button = customtkinter.CTkButton(self, text="START", fg_color="#010057", command=self.button_callback)
        self.button.grid(row=5, column=0, padx=10, pady=10, sticky="ew", columnspan=2)
        

    def open_file_explorer(self):
        # Open the file explorer dialog and store the selected path
        path: str = customtkinter.filedialog.askdirectory()

        if path.lower() == 'c:/' or path.lower() == '':
            path = f'{path}/recovered-files'

        self.destPath.configure(text=path)
        self.destinationPath = path

    def button_callback(self):
        drive = self.radiobutton_frame.get()
        file_exts = self.checkbox_frame.get()

        print(f"Drives:                    -> {drive}")
        print(f"File Extensions:           -> {file_exts}")
        print(f"Recovery Destination Path: -> {self.destinationPath}")

        self.processing_frame = ProcessingFrame(self, "Processing...", self.stop)
        self.processing_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew", columnspan=2, rowspan=7)

        self.update()

        self.process = Process(target=RecoverFiles, args=(drive, file_exts, self.destinationPath))
        self.process.start()

    def stop(self):
        print('stop')
        self.process.terminate()
        self.processing_frame.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()
