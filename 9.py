import cv2 #pip install opencv-python
from tkinter import *
from tkinter import messagebox
import pyrebase
import time
import requests

quantity= 0    # number of bottles inserted
points = 0
root = Tk()

root.geometry("1300x860")
root.title("REVERSE VENDING MACHINE")
config_file = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt' #file names  // architecture
frozen_model = 'frozen_inference_graph.pb'                   #           // model


model = cv2.dnn_DetectionModel(frozen_model,config_file) #load the model

model.setInputSize(320,320)  # in config file specification
model.setInputScale(1/127.5) #255/2
model.setInputMean((127.5,127.5,127.5))  # mobile net takes input as [-1,1]
model.setInputSwapRB(True)

def save_image():

    cap = cv2.VideoCapture(0)

    success,img = cap.read()

   # cv2.imshow('image',img)
    #cv2.waitKey(1)
    cv2.imwrite('test.png',img)

    cap.release()
    cv2.destroyAllWindows()


def scan_image():
    global quantity,points
    global nob,p
    

    img = cv2.imread('test.png')
    z=0
    classIndex , confidece, bbox = model.detect(img,confThreshold= 0.5 )
    print(classIndex)
    bool = False
    for item in classIndex:
        if item==44:
            print("bottle")
            bool = True
            quantity+=1
            points=quantity*2
            b2_window = c.create_window(830,400,anchor="nw",window=b2) 
                
            
            if(quantity>1):
                c.delete(nob)    # number of bottles
                c.delete(p)
                
            nob=c.create_text(500,400,text="TOTAL NUMBER OF BOTTLES ENTERED:"+str(quantity),font = ("Copperplate",10),fill='black',anchor="nw")
            p=c.create_text(500,420,text="TOTAL POINTS:"+str(points),font = ("Copperplate",10),fill='black',anchor="nw")
            break
            
    if bool == False:
        messagebox.showinfo("Say Hello", "BOTTLE NOT FOUND")
        
def base():
    global total_points,total_bottles
    """
    firebaseConfig = {
  'apiKey': "AIzaSyA7EhJGK9LsBaWA1MDxqM6_bh2DgF4CtAU",
  'authDomain': "database-e9a59.firebaseapp.com",
  'databaseURL': "https://database-e9a59-default-rtdb.asia-southeast1.firebasedatabase.app/",  
  'projectId': "database-e9a59",
  'storageBucket': "database-e9a59.appspot.com",
  'messagingSenderId': "37948786342",
  'appId': "1:37948786342:web:ba373b220167437593d667",
  'measurementId': "G-YX0R7HV7BL"
    }
    """
    firebaseConfig = {
    'apiKey': "AIzaSyCkH50BGqPJMUnhk4zq5318q75SrL50sCw",
    'authDomain': "reverse-vending-machine-19a48.firebaseapp.com",
    'databaseURL': "https://reverse-vending-machine-19a48-default-rtdb.firebaseio.com",
    'projectId': "reverse-vending-machine-19a48",
    'storageBucket': "reverse-vending-machine-19a48.appspot.com",
    'messagingSenderId': "315054345931",
    'appId': "1:315054345931:web:3e5da1a1909d9d08f4954e",
    'measurementId': "G-YH430D3G2E"
  };

    firebase = pyrebase.initialize_app(firebaseConfig)
    db = firebase.database()
    real_time = time.asctime()
    print("till here")
    total_bottles = quantity
    total_points = points
    users = db.child('user').get()
    try:
        for user in users.each():
            if user.key() == phone:
                dates = db.child('user').child(phone).get()
                date = dates[-1].key()

                data = db.child('user').child(phone).child(date).get()
                total_bottles = data.val()['total bottles']+quantity
                total_points = data.val()['total points']+points
            #for x in z:
             #   print(x.val())
              #  print(x.key())
            
            #total_points = db.child('user').child(phone).child(date).val()['total points']+points
    except:
        pass
    print("lol")
    data = {'phone':phone,'number of bottles':quantity,'points':points,'total bottles':total_bottles,'total points':total_points,'time':real_time}
    
    db.child('user').child(phone).child(real_time).update(data);
    print("updated")
    
    
    
    
   
            
def message():
    global phone
    phone=e1.get()
    base()
    
    print(phone)
    
    url = "https://www.fast2sms.com/dev/bulk"
    querystring = {"authorization":"52L7HMmUf8l09JTNKnRGz3cAPIpsFEwrauWSjCiXhOgeodBvbYaLjgOrh8wvWzuypt5RJ0Dc93iI21ZM","sender_id":"REV-VEND","message":"YOU HAVE RECIEVED "+str(points)+" POINTS FOR ENTERING "+str(quantity)+" BOTTLES"+"\nTOTAL POINTS: "+str(total_points)+"\nTOTAL BOTTLES: "+str(total_bottles)+"\nTHANK YOU FOR USING OUR SERVICE","language":"english","route":"p","numbers":phone}

    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    
    
    print("done")
    
def add():
    save_image()
    scan_image()
    
def terminate():
    sys.exit()
    
def new():
    global e1
    pw = Toplevel()
    pw.title("PHONE NUMBER")
    Label(pw,text="ENTER PHONE NUMBER: ").grid(row=0,column=0)
    e1=Entry(pw,bd=5,width=50)
    e1.grid(row=0,column=1)
    b3=Button(pw,command=message,bg='gray',activebackground='blue',height=1,width=5,text='SUBMIT',font = ("Copperplate",10)).grid(row=1,column=1)
    
    
# GUI 


    ##background

bg = PhotoImage(file="bg3.png",master = root)

c = Canvas(root,width=1300,height=860)
c.pack(fill="both",expand=True)
c.create_image(0,0,image = bg,anchor="nw")

    ##background>


c.create_text(650,290,text="WELCOME",font = ("Copperplate",50),fill='green')
    
b1=Button(root,command=add,bg='gray',activebackground='blue',height=3,width=10,text='ADD',font = ("Copperplate",20))
b2=Button(root,command=new,bg='gray',activebackground='blue',height=3,width=10,text='PROCEED',font = ("Copperplate",20))


b1_window = c.create_window(300,400,anchor="nw",window=b1)



root.mainloop()
