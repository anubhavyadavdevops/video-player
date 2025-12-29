import customtkinter as ctk
import vlc
import os
import sys

VIDEO_PATH = r"C:\\Users\\Dell\\Downloads\\01_Anubhav_Yadav\\00_Learning\\04_Soft_Head_PL\\video_player\\sample_video.mp4"  # <-- change this

class VideoPlayer(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("VLC Player")
        self.geometry("900x500")

        # video frame
        self.video_frame = ctk.CTkFrame(self, fg_color="black")
        self.video_frame.pack(fill="both", expand=True)

        # controls
        controls = ctk.CTkFrame(self)
        controls.pack(fill="x")

        self.play_btn = ctk.CTkButton(controls, text="Play", command=self.play)
        self.play_btn.pack(side="left", padx=10, pady=5)

        self.pause_btn = ctk.CTkButton(controls, text="Pause", command=self.pause)
        self.pause_btn.pack(side="left", padx=10)

        # VLC setup
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        media = self.instance.media_new(VIDEO_PATH)
        self.player.set_media(media)

        self.update()  # ensure window exists
        self._set_video_handle()

    def _set_video_handle(self):
        handle = self.video_frame.winfo_id()
        if sys.platform.startswith("win"):
            self.player.set_hwnd(handle)
        elif sys.platform.startswith("linux"):
            self.player.set_xwindow(handle)
        elif sys.platform == "darwin":
            self.player.set_nsobject(handle)

    def play(self):
        self.player.play()

    def pause(self):
        self.player.pause()


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    app = VideoPlayer()
    app.mainloop()
