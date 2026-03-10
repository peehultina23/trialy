from picamera import PiCamera
from time import sleep
import datetime,os,subprocess

os.makedirs('/home/pi/videos',exist_ok=True)
camera=PiCamera();camera.resolution=(1024,768)
ts=datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
video_h264="/home/pi/videos/video_{}.h264".format(ts)
camera.start_recording(video_h264);sleep(10);camera.stop_recording()
subprocess.run(["MP4Box","-add",video_h264,"/home/pi/videos/video_{}.mp4".format(ts)],check=True);os.remove(video_h264)
