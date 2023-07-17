import os

class RecoverFiles:
    def __init__(self, drive, file_exts, destination_path):
        removed_trailing_backslash = os.path.splitdrive(drive)[0]
        self.drive = f"\\\\.\\{removed_trailing_backslash}"
        self.file_exts = file_exts
        self.dest_path = destination_path
        self.terminate = False

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
                if self.terminate:
                    break

                for sig, value in self.file_exts.items():
                    found = byte.find(value)
                    if found >= 0:
                        drec = True
                        print(f"--- Found {sig} at location: {hex(found+(size*offs))} ---")
                        # Now let's create recovered file and search for ending signature
                        file_path = os.path.join(self.dest_path, f"{rcvd}.{sig.lower()}")
                        fileN = open(file_path, "wb")
                        fileN.write(byte[found:])
                        while drec:
                            byte = fileD.read(size)
                            bfind = byte.find(b"\x49\x45\x4E\x44")
                            if bfind >= 0:
                                fileN.write(byte[:bfind + 2])
                                fileD.seek((offs + 1) * size)
                                drec = False
                                rcvd += 1
                                fileN.close()
                            else:
                                fileN.write(byte)
                byte = fileD.read(size)
                offs += 1