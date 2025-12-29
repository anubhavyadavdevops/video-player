import vlc
import sys


class VLCPlayer:
    def __init__(self, video_path: str):
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        media = self.instance.media_new(video_path)
        self.player.set_media(media)

    def set_window(self, widget):
        handle = widget.winfo_id()
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
