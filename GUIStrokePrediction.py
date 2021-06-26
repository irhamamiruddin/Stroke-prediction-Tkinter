#import library
import tkinter as tk
from tkinter import *
import  numpy as np
import pickle
from sklearn import metrics


def Output():
    df = np.array([[int(gender.get()),int(age.get()),int(hp.get()),int(hp.get()),int(em.get()),
                    int(work.get()),int(residence.get()),float(glu.get()),float(bmi.get()),int(smoke.get())]])
     
    loaded_model = pickle.load(open('randomForest_model.sav', 'rb'))    
    p_output=loaded_model.predict(df)
    Predict(p_output)

def Predict(p_output):
    #result
    if p_output==0:
        label_result.config(text = "Predicted with NO STROKE.")
        
    elif p_output==1:
        label_result.config(text = "Predicted with STROKE.")

    
#GUI
win = tk.Tk()
#window title
win.title('Stroke Prediction System')

#window size
win.geometry("450x500")

#win.minsize(450,500)
#win.maxsize(450,500)

#Column gender
label1 = tk.Label(win,text="1. Gender")
label1.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
gender = IntVar()
#male-1,female-0
gender_r1=Radiobutton(win,text="Male",variable=gender,value=1)
gender_r1.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)
gender_r2=Radiobutton(win,text="Female",variable=gender,value=0)
gender_r2.grid(column=2, row=0, sticky=tk.W, padx=5, pady=5)

#Column age
label2 = tk.Label(win,text="2. Age")
label2.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
age = IntVar()
age_entrybox = tk.Entry(win,width=25,textvariable=age)
age_entrybox.grid(column=1, columnspan=2, row=1, sticky=tk.W, padx=5, pady=5)

#Column hypertension*
label3 = tk.Label(win,text="3. Hypertension")
label3.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
hp = IntVar()
#yes-1,no-0
hp_r1=Radiobutton(win,text="Yes",variable=hp,value=1)
hp_r1.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)
hp_r2=Radiobutton(win,text="No",variable=hp,value=0)
hp_r2.grid(column=2, row=2, sticky=tk.W, padx=5, pady=5)

#Column heart disease*
label4 = tk.Label(win,text="4. Heart Disease")
label4.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
hd = IntVar()
#yes-1,no-0
hd_r1=Radiobutton(win,text="Yes",variable=hd,value=1)
hd_r1.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)
hd_r2=Radiobutton(win,text="No",variable=hd,value=0)
hd_r2.grid(column=2, row=3, sticky=tk.W, padx=5, pady=5)

#Column ever married
label5 = tk.Label(win,text="5. Ever Married")
label5.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
em = IntVar()
#yes-1,no-0
em_r1=Radiobutton(win,text="Yes",variable=em,value=1)
em_r1.grid(column=1, row=4, sticky=tk.W, padx=5, pady=5)
em_r2=Radiobutton(win,text="No",variable=em,value=0)
em_r2.grid(column=2, row=4, sticky=tk.W, padx=5, pady=5)

#Column work type
label6 = tk.Label(win,text="6. Work Type")
label6.grid(column=0, row=5, rowspan=2, sticky=tk.NW, padx=5, pady=5)
work = IntVar()
#private-0,self-employe-1,government-2,children-3,never worked-4
work_r1=Radiobutton(win,text="Private",variable=work,value=0)
work_r1.grid(column=1, row=5, sticky=tk.W, padx=5, pady=5)
work_r2=Radiobutton(win,text="Self-Employed",variable=work,value=1)
work_r2.grid(column=2, row=5, sticky=tk.W, padx=5, pady=5)
work_r3=Radiobutton(win,text="Government",variable=work,value=2)
work_r3.grid(column=3, row=5, sticky=tk.W, padx=5, pady=5)
work_r4=Radiobutton(win,text="Children",variable=work,value=3)
work_r4.grid(column=1, row=6, sticky=tk.W, padx=5, pady=5)
work_r5=Radiobutton(win,text="Never Work",variable=work,value=4)
work_r5.grid(column=2, row=6, sticky=tk.W, padx=5, pady=5)

#Column residence
label7 = tk.Label(win,text="7.Residence")
label7.grid(column=0, row=7, sticky=tk.W, padx=5, pady=5)
residence = IntVar()
#rural-0,urban-1
residence_r1=Radiobutton(win,text="Urban",variable=residence,value=1)
residence_r1.grid(column=1, row=7, sticky=tk.W, padx=5, pady=5)
residence_r2=Radiobutton(win,text="Rural",variable=residence,value=0)
residence_r2.grid(column=2, row=7, sticky=tk.W, padx=5, pady=5)

#Column average glucose
label8 = tk.Label(win,text="8. Average glucose")
label8.grid(column=0, row=8, sticky=tk.W, padx=5, pady=5)
glu = DoubleVar()
glu_entrybox = tk.Entry(win,width=25,textvariable=glu)
glu_entrybox.grid(column=1,columnspan=2, row=8, sticky=tk.W, padx=5, pady=5)

#Column bmi
label9 = tk.Label(win,text="9. BMI")
label9.grid(column=0, row=9, sticky=tk.W, padx=5, pady=5)
bmi = DoubleVar()
bmi_entrybox = tk.Entry(win,width=25,textvariable=bmi)
bmi_entrybox.grid(column=1, columnspan=2, row=9, sticky=tk.W, padx=5, pady=5)

#Column smoking status
label10 = tk.Label(win,text="10. Smoking Status")
label10.grid(column=0, row=10, sticky=tk.W, padx=5, pady=5)
smoke = IntVar()
#smoke-0,former-1,never-2,unknown
smoke_r1=Radiobutton(win,text="Smoke",variable=smoke,value=0)
smoke_r1.grid(column=1, row=10, sticky=tk.W, padx=5, pady=5)
smoke_r2=Radiobutton(win,text="Former Smoke",variable=smoke,value=1)
smoke_r2.grid(column=2, row=10, sticky=tk.W, padx=5, pady=5)
smoke_r3=Radiobutton(win,text="Never Smoke",variable=smoke,value=2)
smoke_r3.grid(column=3, row=10, sticky=tk.W, padx=5, pady=5)

#input data
df = [gender,age,hp,hd,em,work,residence,glu,bmi,smoke]

#predict button      
p_button = tk.Button(win,text="Predict",command=Output)
p_button.grid(row=11,columnspan=4, sticky=tk.S, padx=5, pady=5)

label_result = tk.Label(win, text = "",fg='red')
label_result.grid(row=12, columnspan=4,sticky=tk.S, padx=5, pady=5)

win.mainloop()

