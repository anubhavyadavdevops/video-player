import customtkinter as ctk
from app.player.vlc_player import VLCPlayer

VIDEO_PATH = r"C:\\Users\\Dell\\Downloads\\01_Anubhav_Yadav\\00_Learning\\04_Soft_Head_PL\\video_player\\sample_video.mp4"  # same as before

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("VLC Player")
        self.geometry("900x500")

        self.video_frame = ctk.CTkFrame(self, fg_color="black")
        self.video_frame.pack(fill="both", expand=True)

        controls = ctk.CTkFrame(self)
        controls.pack(fill="x")

        self.player = VLCPlayer(VIDEO_PATH)

        ctk.CTkButton(controls, text="Play", command=self.player.play).pack(
            side="left", padx=10, pady=5
        )
        ctk.CTkButton(controls, text="Pause", command=self.player.pause).pack(
            side="left", padx=10
        )

        self.update()
        self.player.set_window(self.video_frame)
