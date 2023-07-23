import os

class RecoverFiles:
    def __init__(self, drive, file_exts, destination_path):
        removed_trailing_backslash = os.path.splitdrive(drive)[0]
        self.drive = f"\\\\.\\{removed_trailing_backslash}"
        self.file_exts = file_exts
        self.dest_path = destination_path
        self.terminate = False

        self.file_data = {
            "JPG" : { "signature" : b"\xff\xd8\xff\xe0\x00\x10\x4a\x46", "trailer" :  b"\xFF\xD9", "trailer_count": 2 },
            "PNG" : { "signature" : b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A", "trailer" :  b"\x49\x45\x4E\x44\xAE\x42\x60\x82", "trailer_count" : 8 },
            "PDF" : { "signature" : b"\x25\x50\x44\x46\x2D\x31\x2E", "trailer" :  b"\x45\x4F\x46", "trailer_count" : 3 }
        }

        os.makedirs(self.dest_path, exist_ok=True)
        self.find_files(self.drive)

    def find_files(self, drive):
        with open(drive, "rb") as fileD:
            size = 512  # Size of bytes to read
            byte = fileD.read(size)  # Read 'size' bytes
            offs = 0  # Offset location
            drec = False  # Recovery mode
            rcvd = 0  # Recovered file ID
            while byte:
                for _, extension in enumerate(self.file_exts):
                    f_data = self.file_data[extension]
                    print(f_data)
                    found = byte.find(f_data['signature'])
                    if found >= 0:
                        drec = True
                        print(f"--- Found {extension} at location: {hex(found+(size*offs))} ---")
                        # Now let's create recovered file and search for ending signature
                        file_path = os.path.join(self.dest_path, f"{rcvd}.{extension.lower()}")
                        fileN = open(file_path, "wb")
                        fileN.write(byte[found:])
                        while drec:
                            byte = fileD.read(size)
                            bfind = byte.find(f_data['trailer'])
                            if bfind >= 0:
                                fileN.write(byte[:bfind + f_data['trailer_count']])
                                fileD.seek((offs + 1) * size)
                                drec = False
                                rcvd += 1
                                fileN.close()
                            else:
                                fileN.write(byte)
                byte = fileD.read(size)
                offs += 1