from cv2 import VideoCapture, waitKey, imshow, destroyAllWindows, CAP_FFMPEG,cvtColor, COLOR_BGR2RGB
from PIL.Image import fromarray
from PIL.ImageTk import PhotoImage
from imutils import resize
class Cam:

    def __init__(self,path,name):
        self.path=path
        self.device=VideoCapture(path,apiPreference=CAP_FFMPEG)
        self.name=name

    def name(self,name):
        self.name=name

    def viewCam(self):
        while True:
            _,frame=self.device.read()
            imshow(self.name,frame)
            if waitKey(1)==ord('q'):break
        self.deinit()

    def getFrame(self,width):
        ret,frame=self.device.read()
        if ret:
            frame=resize(frame,width=width)
            frame=cvtColor(frame,COLOR_BGR2RGB)

            im=fromarray(frame)
            img=PhotoImage(image=im)

            return img

    def deinit(self):
        self.device.release()
        destroyAllWindows()

class CamManager:

    def __init__(self):
        self.cams=[]
    
    def addCam(self,cam):
        id=len(self.cams)
        self.cams.append(cam)
        return id