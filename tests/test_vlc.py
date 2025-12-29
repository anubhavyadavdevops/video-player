import vlc
import time

p = vlc.MediaPlayer()
p.set_mrl("C:\\Users\\Dell\\Downloads\\01_Anubhav_Yadav\\00_Learning\\04_Soft_Head_PL\\video_player\\sample_video.mp4")  # any local video
p.play()
time.sleep(5)
p.stop()
