import os
import platform
import subprocess

def text_to_speech(text):
    tts = gTTS(text=text, lang='en') 
    file_path = "response.mp3"
    tts.save(file_path)

    # Cross-platform audio playback
    system_name = platform.system()
    try:
        if system_name == "Linux":
            subprocess.call(["xdg-open", file_path])
        elif system_name == "Darwin":  # macOS
            subprocess.call(["open", file_path])
        elif system_name == "Windows":
            os.startfile(file_path)
        else:
            print("Unsupported OS for audio playback.")
    except Exception as e:
        print(f"Error playing audio: {e}")
