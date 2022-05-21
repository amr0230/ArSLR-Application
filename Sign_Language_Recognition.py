"""""""""""""""
By: Amr IDrees
"""""""""""""""
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from sklearn.svm import LinearSVC, SVC
import sklearn.metrics as m
import joblib
from sklearn.neighbors import KNeighborsClassifier as knn

import random
from tkinter import *
from tkinter import filedialog
# loading Python Imaging Library 
from PIL import ImageTk, Image
from time import perf_counter
from sklearn.metrics import classification_report, confusion_matrix


DATADIR = "Dataset/training_dataset/"
TESTDIR = "Dataset/testing_dataset/"

LABEL = os.listdir(DATADIR)
LABELTEST = os.listdir(TESTDIR)
#print(LABEL) --- to print the name of the folders that contain a letters(labels)

categories={
"ain":'ع',
"aleff":'أ',
"bb":'ب',
"dal":'د',
"dha":'ظ',
"dhad":"ض",
"fa":"ف",
"gaaf":'ق',
"ghain":'غ',
"ha":'هـ',
"haa":'ح',
"jeem":'ج',
"kaaf":'ك',
"khaa":'خ',
"laam":'ل',
"meem":'م',
"nun":"ن",
"ra":'ر',
"saad":'ص',
"seen":'س',
"sheen":"ش",
"ta":'ط',
"taa":'ت',
"thaa":"ث",
"thal":"ذ",
"waw":'و',
"yaa":"ي",
"zay":'ز'
}

training_data = []
def create_training_data():
    for label in LABEL:
        path = os.path.join(DATADIR, label)
        class_num = LABEL.index(label)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
                #training_data.append([img_array, class_num])
                training_data.append([img_array, label])
                #print(label)
            except Exception as e:
                pass
        
create_training_data()
#print(len(training_data))


testing_data = []
def create_testing_data():
    for labeltest in LABELTEST:
        path = os.path.join(TESTDIR, labeltest)
        class_num = LABEL.index(labeltest)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
                #training_data.append([img_array, class_num])
                testing_data.append([img_array, labeltest])
                #print(label)
            except Exception as e:
                pass
        
create_testing_data()
#print(len(testing_data))

"""
random.shuffle(training_data)#!!!! to take a random labels(name ofa folder in training_dataset) and print them. from 0 to 9 -> :10 
for sample in training_data[:10]: 
    print(sample[1])# when sample[0] that will print 10th labels as array (PIXELS), when it is 1 it will print them as label(name of a folder in Training_dataset)

"""
# For training
X = []
y = []

# For testing
X_test = []
y_test = []

for features, label in training_data:
    features = cv2.resize(features, (64,64)).flatten()
    X.append(features)
    y.append(label)
    
for featuretest, label_test in testing_data:
    featuretest = cv2.resize(featuretest, (64,64)).flatten()
    X_test.append(featuretest)
    y_test.append(label_test)


# SVM model training: taked 7.766 min to train
def run_svm():
    start_time = perf_counter()
    clf = SVC(kernel='rbf',C=28,degree=3,coef0=0.001,gamma='scale')
    #fit to the trainin data
    print("svm started")
    print('Training...')
    svmmodel = clf.fit(X, y)
    print('Saving model...')
    joblib.dump(svmmodel, "svm_model.pkl")
    print('model saved')
    print (perf_counter() - start_time," Seconds")

#run_svm()
    
        
# KNN model training: taked 24.968 sec  to train
def run_knn():
    start_time = perf_counter()
    clf=knn(n_neighbors=5)
    print("knn started")
    print('Training...')
    knnmodel = clf.fit(X, y)
    print('Saving model...')
    joblib.dump(knnmodel, "knn_model.pkl")
    print('model saved')
    print (perf_counter() - start_time," Seconds")
    
#run_knn()

#=========================================GUI===============================================================

root = Tk() #Makes the window
root.title("Hand Sign Recognition") #Makes the title that will appear in the top left
root.geometry("1350x700+0+0")

root.config(bg = "#5f615e")
root.bg=ImageTk.PhotoImage(file="images/bg9.jpg")
bg=Label(root,image=root.bg).place(x=140,y=0,width=1000)


def select_image():
    global path_to_image
    
    path_to_image = filedialog.askopenfilename(initialdir="/", 
                                               title= "open File",
                                              filetypes=(("JPGs", "*.jpg"), ("PNGs", "*.png"), ("GIFs", "*.gif"), ("All Files", "*.*")))
    if path_to_image is not None: 
        #content = path_to_image.read() 
        return path_to_image
        
def open_img(): 
    # Select the Imagename  from a folder  
    x = select_image()
    global img
    
    # opens the image 
    img = Image.open(x)
      
    # resize the image and apply a high-quality down sampling filter 
    img = img.resize((230, 230), Image.ANTIALIAS)
  
    # PhotoImage class is used to add image to widgets, icons etc 
    img = ImageTk.PhotoImage(img)
    
    circleCanvas.create_image(0, 0, anchor=NW, image=img)
    
def predict():
    svmCanvas.delete("all")
    knnCanvas.delete("all")
    z = path_to_image
    pred1 = []
    svmclassifier = joblib.load("svm_model.pkl")
    img_array = cv2.imread(z, cv2.IMREAD_GRAYSCALE)
    feature = cv2.resize(img_array, (64,64)).flatten()
    pred1.append(feature)
    prediction1 = svmclassifier.predict(pred1)
    print("Prediction by SVM - {0}".format(prediction1[0]))
    print(categories[prediction1[0]])
    svmCanvas.create_text(130,80,fill="darkblue",font="Times 100 bold",text=categories[prediction1[0]])
    svmCanvas.update

    
    pred2 = []
    pred2.append(feature)
    knnclassifier = joblib.load("knn_model.pkl")
    prediction2 = knnclassifier.predict(pred2)
    print("Prediction by KNN - {0}".format(prediction2[0]))
    print(categories[prediction2[0]])
    knnCanvas.create_text(130,80,fill="darkblue",font="Times 100 bold",text=categories[prediction2[0]])
    knnCanvas.update

def _exit_():
    root.destroy()
    import login
        


Manage_Frame=Frame(root,relief=RIDGE,bg="black",bd=4)
Manage_Frame.place(x=1000,y=0,width=345,height=230)
title=Label(Manage_Frame,text="Arabic Alphabet Sign Language \nRecognition Based on Machine \nLearning Methods\n\nAhliya University\nInformation Technology Department\n\n Developed By:  Amr Idrees"
            ,font=("times new roman",16,"bold"),fg="white",bg="black")
title.place(x=0,y=11)

circleCanvas = Canvas(width=200, height=125, bg='white', highlightthickness=7, highlightbackground="#333")
circleCanvas.place(x=570,y=10,width=230,height=230)
Note1=Label(text="Here the selected image will appear",font=("times new roman",11,"bold"),fg="white",bg="black")
Note1.place(x=565,y=240)


open_btn = Button( text="Open Image", bd=5,command=open_img, bg="white",fg="black",font=("times new roman",24,"bold"))
open_btn.place(x=390,y=270,width=280,height=50)

predict_btn = Button( text="Predict", bd=5,command=predict, bg="green",fg="white",font=("times new roman",24,"bold"))
predict_btn.place(x=690,y=270,width=280,height=50)

panelsvm = Label(text="SVM",font=("times new roman",20,"bold"),bg="black",fg="white") 
panelsvm.place(x=510,y=335)

panelknn = Label(text="KNN",font=("times new roman",20,"bold"),bg="black",fg="white")
panelknn.place(x=790,y=335)

svmCanvas = Canvas(width=270, height=200 ,bg='white', highlightthickness=7, highlightbackground="#333")
svmCanvas.place(x=385,y=370)

Note2=Label(text="In these screens the characters predicted by each algorithms will be shown",font=("times new roman",13,"bold"),fg="white",bg="black")
Note2.place(x=405,y=580)

knnCanvas = Canvas(width=270, height=200, bg='white', highlightthickness=7, highlightbackground="#333")
knnCanvas.place(x=690,y=370)

exit_btn = Button(text="Exit", bd=5,command=_exit_, bg="#1e72c7",fg="white",font=("times new roman",24,"bold"))
exit_btn.place(x=560,y=635,width=240,height=50)


mainloop()











