#Python Interface Program Using Tkinter and Other External Libraries to plot and predict data using given datasets
#importing required libraries(both internal and external) 
import csv
import matplotlib.pyplot as plt
import matplotlib.style as stl
import numpy as np
from tkinter import *
#intialising global variables for use in all the function along with the "global" keyword before variable names
md=0
yr=0
mn=0
cr=0
py=0
gr=0
#making the window for the interface
window=Tk()
window.title("Data Analysis and Plotting using Python")
window.geometry('500x350') #setting default size of the window
#intialising variables for getting values from Tkinter widgets 
mode=StringVar(window)
year=StringVar(window)
month=StringVar(window)
car=StringVar(window)
graph=StringVar(window)
#function for About option in the menu
def about():
	about=Tk()
	about.title("About")
	about.geometry('235x165')
	msg_about=Message(about, text="This application can be used to predict and plot data as per the data entered by the user. The prediction is done using the annual growth rate model. Plotting is done after reading the data from the files and plotting them on bar-charts or pie-charts, as per the user requirement.")
	msg_about.pack()
	about.mainloop()
#function for User Instructions option in the menu
def user_ins():
	userins=Tk()
	userins.title("User Instructions")
	userins.geometry('340x260')
	msg_user=Message(userins, text="\nSelect Plotting or Prediction of data.\n\nSelect year for which you want to import data. Select \"ALL\" for all years or any specific value for a particular year.\n\nSelect month as per your requirement,\"All\" or any specific value for the desired month.\n\nSelect car accordingly or select \"All\" for all cars.\n\nSelect type of graph you want to plot or select the year for which you want to predict data for.\n\nTo predict data for any specific month, select that month from the month dropdown.")
	msg_user.pack()
	userins.mainloop()
#function to get values entered by the user using the Tkinter widgets
def value_func(*args):
        global md, yr, mn, cr, py, gr #importing global variables as values we will be set to them accordingly 
        m=mode.get() #xyz.get() : function to retrieve values from the variable in the widgets
        y=year.get()
        mon=month.get()
        c=car.get()
        g=graph.get()
        py=int(pre_year.get()) #converting to integer type
        #setting md variable to 0 or 1 for the mode of operation of the code selected by the user
        if(m=="PLOTTING"):
                md=0
        elif(m=="PREDICTION"):
                md=1
        #setting the yr variable as per the value of the year selected by the user
        if(y=="ALL"):
                yr=0
        if(y=="2007"):
                yr=1
        if(y=="2008"):
                yr=2
        if(y=="2009"):
                yr=3
        if(y=="2010"):
                yr=4
        if(y=="2011"):
                yr=5
        if(y=="2012"):
                yr=6
        if(y=="2013"):
                yr=7
        if(y=="2014"):
                yr=8
        if(y=="2015"):
                yr=9
        if(y=="2016"):
                yr=10
        #setting the mn variable as per the value of the month selected by the user
        if(mon=="ALL"):
                mn=0
        if(mon=="JAN"):
                mn=1
        if(mon=="FEB"):
                mn=2
        if(mon=="MAR"):
                mn=3
        if(mon=="APR"):
                mn=4
        if(mon=="MAY"):
                mn=5
        if(mon=="JUN"):
                mn=6
        if(mon=="JUL"):
                mn=7
        if(mon=="AUG"):
                mn=8
        if(mon=="SEP"):
                mn=9
        if(mon=="OCT"):
                mn=10
        if(mon=="NOV"):
                mn=11
        if(mon=="DEC"):
                mn=12
        #setting the cr variable as per the car selected by the user
        if(c=="ALL"):
                cr=0
        if(c=="ALTO"):
                cr=1
        if(c=="BELANO"):
                cr=2
        if(c=="DESIRE"):
                cr=3
        if(c=="ERTIGA"):
                cr=4
        if(c=="GYPSY"):
                cr=5
        if(c=="OMNI"):
                cr=6
        if(c=="SWIFT"):
                cr=7
        if(c=="WOGONR"):
                cr=8
        #setting the gr variable for the graph type required by the user
        if(g=="PIE CHART"):
                gr=-1
        else:
                gr=1
#main function of the application
def function():
    global md, yr, mn, cr, py, gr #importing the global variables with their changed values
    #working on prediction mode
    if(md==1):
        py=py%2016 #to see how years into the future the user wants to make the prediction for
        fl="" #empty string variable for storing the name of the file to be opened
        counter=1 #counter variable used for skipping rows in the data imported
        r=0 #variable to calculate and store the avaerage annual graowth rate
        data=[] #list to read and store the data read from the CSV file
        #selecting file to be opened, and writing its name to fl variable
        if(mn==0):
            fl="cars.csv"
        else:
            if (cr==1):
                fl="Alto.csv"
            if (cr==2):
                fl="Belano.csv"
            if (cr==3):
                fl="Desire.csv"
            if (cr==4):
                fl="Ertiga.csv"
            if (cr==5):
                fl="Gypsy.csv"
            if (cr==6):
                fl="Omni.csv"
            if (cr==7):
                fl="Swift.csv"
            if (cr==8):
                fl="WagonR.csv"
        #opening file as csvfile into the variable read
        with open(fl) as csvfile:
            read=csv.reader(csvfile, delimiter=',')
            next(read) #skipping the header rows
            #code for yearly prediction value
            if(mn==0):
                for row in read: #traversing rows of the imported data in the read variable
                    if(counter<cr): #skipping to the car from the top of the read data
                        counter=counter+1
                        continue
                    else:
                        for i in range(1,11):
                            data.append(int(row[i])) #reading and appending the values to the data list
                        break
                for i in range(1,10): #traversing the values in the list
                    r=r+data[i]/data[i-1] #calculating cummulative sum of growth index for every year
                r=r/9 #finding average of the growth rate
                value=data[-1]*pow(r,py) #multiplying the value for year 2016 into growth factor for the required year
            #code for month wise yearly prediction value
            else:
                for row in read: #traversing rows of the imported data in the read variable
                    if(counter<mn): #skipping to the month from the top of the read data
                        counter=counter+1
                        continue
                    else:
                        for i in range(1,11):
                            data.append(int(row[i])) #reading and appending the values to the data list
                        break
                for i in range(1,10): #traversing the values in the list
                    r=r+data[i]/data[i-1] #calculating cummulative sum of growth index for every year
                r=r/9 #finding average of the growth rate
                value=data[-1]*pow(r,py) #multiplying the value for year 2016 into growth factor for the required year
        #printing the predicted value
        print("Predicted Value = %1.2f"%value)
    #code for plotting of data
    else:
        #making labels for car names into the variable car_labels
        car_labels = np.loadtxt('cars.csv', dtype='str', delimiter=',', skiprows = 1, usecols = (0,)) 
        #code for plotting of bar-graphs
        if(gr==1):
            #plotting for a particular car sold in a particular month of all years
            if(yr==0 and mn!=0 and cr!=0):
                #assinging file name to fl varaible
                if (cr==1):
                    fl="Alto.csv"
                if (cr==2):
                    fl="Belano.csv"
                if (cr==3):
                    fl="Desire.csv"
                if (cr==4):
                    fl="Ertiga.csv"
                if (cr==5):
                    fl="Gypsy.csv"
                if (cr==6):
                    fl="Omni.csv"
                if (cr==7):
                    fl="Swift.csv"
                if (cr==8):
                    fl="WagonR.csv"
                #importing data into data named variable
                data = np.loadtxt(fl, dtype='str', delimiter=',', usecols = (1,2,3,4,5,6,7,8,9,10))
                #making month names into the varaible month_labels
                month_labels = np.loadtxt(fl, dtype='str', delimiter=',', usecols = (0,))
                #assinging month name needed to the month_name variable
                month_name=month_labels[mn]
                #assinging car name needed to the car_name variable
                car_name=car_labels[cr-1]
                values=[] #list for values
                years=[] #list for year
                for i in range(0,10): #traversing through the data values in data variable
                    years.append(data[0][i]) #appending years to the years list
                    values.append(data[mn][i]) #appending values to the values variable
                #plotting code
                stl.use("ggplot") #using style as ggplot
                plt.plot(years,values) #plotting years on X-axis and values on Y-axis
                plt.title("%s sold in all the years in the month of %s..."%(car_name,month_name)) #giving title to the plot
                plt.xlabel("Years") #label on X_axis
                plt.ylabel("Numbers in '000") #label on Y_axis
                plt.show() #showing the plot, finally
            #plotting for all cars sold in all the months of a particular year
            if(yr!=0 and mn==0 and cr==0):
                #importing the data into the data variable from the cars.csv file
                data = np.loadtxt('cars.csv', delimiter=',', skiprows = 1, usecols = range(1,11))
                data=data.transpose() #transposing the data imported
                yr=yr%2007 #finding index for the year after doing modulus from 2007
                values=[] #creating empty list for the values
                for i in range(0,8): #looping for finding the values
                    values.append(data[yr][i]) #appending cars sold in a particular year for every car  
                stl.use("ggplot") #using style as ggplot
                plt.plot(car_labels,values) #plotting Cars on X-axis and values on Y-axis
                plt.title("Cars sold in the year %d..."%(2007+yr)) #giving title to the plot
                plt.xlabel("Cars") #label on X_axis
                plt.ylabel("Numbers in '000") #label on Y_axis
                plt.show() #showing the plot, finally
            #plotting for all cars sold in a particular month in a particular year
            elif(yr!=0 and mn!=0 and cr==0):
                yr=yr%2007 #finding year index
                values=[] #empty list for values
                for i in range(1,9): #looping for the files, one by one
                    if (i==1):
                        fl="Alto.csv"
                    if (i==2):
                        fl="Belano.csv"
                    if (i==3):
                        fl="Desire.csv"
                    if (i==4):
                        fl="Ertiga.csv"
                    if (i==5):
                        fl="Gypsy.csv"
                    if (i==6):
                        fl="Omni.csv"
                    if (i==7):
                        fl="Swift.csv"
                    if (i==8):
                        fl="WagonR.csv"
                    #importing all files, one by one
                    data = np.loadtxt(fl, dtype='str', delimiter=',',skiprows = 1, usecols = range(1,11))
                    #appending values for the asked month and the asked year
                    values.append(data[mn-1][yr])
                #making month labels
                month_labels = np.loadtxt(fl, dtype='str', delimiter=',', usecols = (0,))
                #assinging month name to the month_name variable
                month_name=month_labels[mn]
                stl.use("ggplot") #using style as ggplot
                plt.plot(car_labels,values) #plotting Cars on X-axis and values on Y-axis
                plt.title("Cars sold in the year %d, in the month of %s..."%((2007+yr),month_name)) #giving title to the plot
                plt.xlabel("Cars") #label on X_axis
                plt.ylabel("Numbers in '000") #label on Y_axis
                plt.show() #showing the plot, finally
        #code for pie-charts     
        elif(gr==-1):
            values=[] #empty list for the values
            #assinging file name to the fl variable
            if (cr==1):
                fl="Alto.csv"
            if (cr==2):
                fl="Belano.csv"
            if (cr==3):
                fl="Desire.csv"
            if (cr==4):
                fl="Ertiga.csv"
            if (cr==5):
                fl="Gypsy.csv"
            if (cr==6):
                fl="Omni.csv"
            if (cr==7):
                fl="Swift.csv"
            if (cr==8):
                fl="WagonR.csv"
            #plotting for all cars sold in a particular year
            if(cr==0):
                #reading cars.csv and giving cars names to the car_labels variable
                data = np.loadtxt("cars.csv", dtype='str', delimiter=',', skiprows=1, usecols = range(1,11))
                car_labels = np.loadtxt('cars.csv', dtype='str', delimiter=',', skiprows = 1, usecols = (0,))
                #traversing the data 
                for i in range(0,8):
                    values.append(data[i][yr]) #appending values to the values list
                #making pie-chart
                plt.pie(values, labels=car_labels, autopct='%1.1f%%', shadow=True, startangle=90)
                plt.axis('equal') #making axis equal
                plt.title("Percentage of cars sold in the year %d"%(2007+yr)) #title of the plot
                plt.show() #showing the plot, finally
            #plotting for a particular car sold in all months of a particular year
            else:
                #reading the file required and giving month names to the month_labels variable
                data = np.loadtxt(fl, dtype='str', delimiter=',', skiprows=1, usecols = range(1,11))
                month_labels = np.loadtxt(fl, dtype='str', delimiter=',', skiprows=1, usecols = (0,))
                for i in range(0,12):
                    values.append(data[i][yr]) #appending values to the values list
                car_name=fl[0:-4] #assinging car name to the car_name variable
                #making pie-chart
                plt.pie(values, labels=month_labels, autopct='%1.1f%%', shadow=True, startangle=90)
                plt.axis('equal') #making axis equal
                plt.title("Percentage of %ss sold in all the months of year %d"%(car_name,2007+yr)) #title of the plot
                plt.show() #showing the plot, finally
#code for interface of the program
#making menubar
menubar=Menu(window)
helpmenu=Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about)
helpmenu.add_command(label="User Instructions", command=user_ins)
helpmenu.add_separator() #adding seperator
helpmenu.add_command(label="Quit", command=window.quit)
menubar.add_cascade(label="Help", menu=helpmenu)
window.config(menu=menubar)
#making the frame for the heading
header=Frame(window, height=50, width=350, relief=RAISED)
heading=Label(header, text="Welcome to Data Analysis and Plotting using Python", font=("Helvetica", 15), pady=10)
heading.pack()
header.pack()
#making the frame for all other widgets
base_frame=Frame(window, height=425, width=300, relief=RAISED, padx=15, pady=15)
#making first frame for selecting the mode of operation
first_frame=Frame(base_frame)
select_mode=Label(first_frame, text="Select Mode :")
select_mode.pack(side=LEFT)
mode_frame=Frame(first_frame)
mode_value=OptionMenu(first_frame,mode,"PLOTTING","PREDICTION",command=value_func)
mode_value.pack(side=RIGHT)
mode_frame.pack(side=RIGHT)
first_frame.pack()
#making second frame for the selection of year
second_frame=Frame(base_frame)
year_label=Label(second_frame, text="Selcet Year :")
year_label.pack(side=LEFT)
year_value=OptionMenu(second_frame,year,"ALL","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016",command=value_func)
year_value.pack(side=RIGHT)
second_frame.pack()
#making third frame for the selection of month
third_frame=Frame(base_frame)
month_label=Label(third_frame, text="Select Month :")
month_label.pack(side=LEFT)
month_value=OptionMenu(third_frame,month,"ALL","JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC",command=value_func)
month_value.pack(side=RIGHT)
third_frame.pack()
#making fourth frame for the selection of car
fourth_frame=Frame(base_frame)
car_label=Label(fourth_frame, text="Select Car :")
car_label.pack(side=LEFT)
car_value=OptionMenu(fourth_frame,car,"ALL","ALTO","BELANO","DESIRE","ERTIGA","GYPSY","OMNI","SWIFT","WAGONR",command=value_func)
car_value.pack(side=RIGHT)
fourth_frame.pack()
#making fifth frame for the selection of graph type
fifth_frame=Frame(base_frame)
graph_label=Label(fifth_frame, text="Graph Type :")
graph_label.pack(side=LEFT)
graph_value=OptionMenu(fifth_frame,graph,"PIE CHART","BAR GRAPH",command=value_func)
graph_value.pack(side=RIGHT)
fifth_frame.pack()
#making sixth frame for the selection of year of prediction type
sixth_frame=Frame(base_frame)
pre_label=Label(sixth_frame, text="Enter year to predict value for :")
pre_label.pack(side=LEFT)
pre_year=Spinbox(sixth_frame, from_=2017, to=2030, command=value_func)
pre_year.pack(side=RIGHT)
sixth_frame.pack()
#making button for result generation
generate_result=Button(base_frame, text="Generate Result", command=function)
generate_result.pack()
base_frame.pack()
window.mainloop()
