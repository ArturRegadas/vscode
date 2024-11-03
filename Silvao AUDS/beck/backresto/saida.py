def saids(mixags):    
    import os
    import ctypes
    import sys
    def change_audio_input(device_index):
        powershell_command = f"Set-AudioDevice -Index {device_index}"
        os.system(f"powershell.exe -Command \"{powershell_command}\"")

    device_id = mixags

    change_audio_input(device_id)