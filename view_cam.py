from faulthandler import disable
from Cam import Cam, CamManager
from tkinter import *
from tkinter import filedialog,Entry


camManager=CamManager()

def close_addCam():
    addCamWindow.withdraw()

def addCam():
    tCamName.delete(0,END)
    tCamPath.delete(0,END)
    mainWindow_x=mainWindow.winfo_x()
    mainWindow_y=mainWindow.winfo_y()

    addCamWindow.geometry("+{}+{}".format(int(mainWindow_x+10),int(mainWindow_y+60)))
    addCamWindow.deiconify()

def addCamera(path,name):
    camId=camManager.addCam(Cam(path,name))
    viewCam()
    addCamWindow.withdraw()

def cancelAdd():
    addCamWindow.withdraw()

def viewCam():
    frame=camManager.cams[0].getFrame(int(mainWindow.winfo_width()/3))
    cam.configure(image=frame)
    cam.image=frame
    cam.after(10,viewCam)

mainWindow=Tk()
mainWindow.title("Cam viewer")
mainWindow.geometry("720x480")

wWidth=mainWindow.winfo_screenwidth()
wHeight=mainWindow.winfo_screenheight()

mainWindow.geometry("+{}+{}".format(int((wWidth/2)-360),int((wHeight/2)-240)))

addCamWindow=Toplevel(mainWindow)
addCamWindow.geometry("240x240")
addCamWindow.title("Add new camera")
addCamWindow.protocol("WM_DELETE_WINDOW",close_addCam)
addCamWindow.resizable(False,False)
addCamWindow.withdraw()



addWindowFrame1=Frame(addCamWindow)
addWindowFrame1.pack(fill=X)

lCamName=Label(addWindowFrame1,text="Camera Name",width=10)
lCamName.pack(side=LEFT,padx=5,pady=5)
tCamName=Entry(addWindowFrame1,width=32)
tCamName.pack(fill=X,padx=5,expand=True)

addWindowFrame2=Frame(addCamWindow)
addWindowFrame2.pack(fill=X)

lCamPath=Label(addWindowFrame2,text="Camera Path",width=10)
lCamPath.pack(side=LEFT,padx=5,pady=5)
tCamPath=Entry(addWindowFrame2, width=32)
tCamPath.pack(fill=X,padx=5,expand=True)

addWindowFrame3=Frame(addCamWindow)
addWindowFrame3.pack(fill=X)

addBtn=Button(addWindowFrame3, text="Add Camera", width=32, command=lambda:addCamera(tCamPath.get(),tCamName.get()))
addBtn.pack(side=RIGHT,padx=5,pady=15, expand=True)

addWindowFrame4=Frame(addCamWindow)
addWindowFrame4.pack(fill=X)

cancelBtn=Button(addWindowFrame4, text="Cancel",width=32,command=cancelAdd)
cancelBtn.pack(side=RIGHT,padx=5,expand=True) 



#menu bar
menuBar=Menu(mainWindow)
#filemenu
fileMenu=Menu(menuBar, tearoff=0)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=mainWindow.quit)
#cams menu
camsMenu=Menu(menuBar,tearoff=0)
camsMenu.add_command(label="Add Cam", command=addCam)
camsMenu.add_command(label="Edit Cam")
camsMenu.add_command(label="View Cam", command=viewCam)


menuBar.add_cascade(label="File", menu=fileMenu)
menuBar.add_cascade(label="Cameras", menu=camsMenu)
mainWindow.config(menu=menuBar)

mainWindowFrame1=Frame(mainWindow)
mainWindowFrame1.pack()

viewer=Label(mainWindow)
camListLabel=Label(mainWindowFrame1,text="Available cameras:", width=20, padx=100,anchor="w")
camListLabel.pack()
camList=Listbox(mainWindowFrame1)
camList.pack()

cams=[]

# cam=Label(mainWindow)
# cam.grid(column=0,row=2,rowspan=2)




mainWindow.mainloop()