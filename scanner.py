#DEVELOPED BY <PRIYANSHUL SHARNA>
# WEBPAGE Priyanshul.is-a.dev

from tkinter import *
from PIL import ImageTk,Image
import cv2
from pyzbar.pyzbar import decode


window=Tk()
window.title("bar code scanner")
window.configure(bg="tan4")
window.geometry("300x400")

vdo=Label(window)
vdo.grid(padx=10,pady=10)


cap=cv2.VideoCapture(0)

def read_barcode(frame):
    barcode=decode(frame)
    txt.delete(0,END)#delete previous entry

    for barcodes in barcode:
        x,y,w,h=barcodes.rect
        
        #1
        barcode_info=pyzbar.pyzbar.barcode.data.decode('utf-8')
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0))

        #2
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x - 6, y - 6), font, 2.0, (0, 0, 0), 1)
        txt.insert (0, barcode_info+" " )#insert new entry
    return frame
    
#function for video streaming
def video_stream():
    _,frame=cap.read()

    frame=cv2.resize(frame,(250,250))
    frame = cv2.copyMakeBorder(frame, 10, 10, 10, 10, cv2.BORDER_CONSTANT)#optional

    frame=read_barcode(frame)
    cv2_image=cv2.cvtColor(frame,cv2.COLOR_BGR2RGBA)
    img=Image.fromarray(cv2_image)
    imgtk = ImageTk.PhotoImage(image=img)
    vdo.imgtk=imgtk
    vdo.configure(image=imgtk)
    vdo.after(1,video_stream())
    




txt=Entry(window,width=25)
txt.grid(pady=25)

video_stream()
window.mainloop()



    
    
