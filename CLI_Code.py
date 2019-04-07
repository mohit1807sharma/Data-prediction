import csv
import matplotlib.pyplot as plt
import matplotlib.style as stl
import numpy as np

def function(mode, year, month, car, pre_year, graph):
    
    if(mode==1):
        file=""
        counter=1
        r=0
        data=[]
        pre_year=pre_year%2016
        
        if(month==0):
            file="cars.csv"
        else:
            if (car==1):
                file="Alto.csv"
            if (car==2):
                file="Belano.csv"
            if (car==3):
                file="Desire.csv"
            if (car==4):
                file="Ertiga.csv"
            if (car==5):
                file="Gypsy.csv"
            if (car==6):
                file="Omni.csv"
            if (car==7):
                file="Swift.csv"
            if (car==8):
                file="WagonR.csv"
        
        with open(file) as csvfile:
            read=csv.reader(csvfile, delimiter=',')
            next(read)
    
            if(month==0):
                for row in read:
                    if(counter<car):
                        counter=counter+1
                        continue
                    else:
                        for i in range(1,11):
                            data.append(int(row[i]))
                        break
                for i in range(1,10):
                    r=r+data[i]/data[i-1]
                r=r/9
                value=data[-1]*pow(r,pre_year)
                return (value)
    
            else:
                for row in read:
                    if(counter<month):
                        counter=counter+1
                        continue
                    else:
                        for i in range(1,11):
                            data.append(int(row[i]))
                        break
                for i in range(1,10):
                    r=r+data[i]/data[i-1]
                r=r/9
                value=data[-1]*pow(r,pre_year)
                return (value)
            
    else:
        car_labels = np.loadtxt('cars.csv', dtype='str', delimiter=',', skiprows = 1, usecols = (0,))
        
        if(graph==1):
            if(year==0 and month!=0 and car!=0):
                if (car==1):
                    file="Alto.csv"
                if (car==2):
                    file="Belano.csv"
                if (car==3):
                    file="Desire.csv"
                if (car==4):
                    file="Ertiga.csv"
                if (car==5):
                    file="Gypsy.csv"
                if (car==6):
                    file="Omni.csv"
                if (car==7):
                    file="Swift.csv"
                if (car==8):
                    file="WagonR.csv"
                data = np.loadtxt(file, dtype='str', delimiter=',', usecols = (1,2,3,4,5,6,7,8,9,10))
                month_labels = np.loadtxt(file, dtype='str', delimiter=',', usecols = (0,))
                month_name=month_labels[month]
                car_name=car_labels[car-1]
                values=[]
                years=[]
                for i in range(0,10):
                    years.append(data[0][i])
                    values.append(data[month][i])
                stl.use("ggplot")
                plt.plot(years,values)
                plt.title("%s sold in all the years in the month of %s..."%(car_name,month_name))
                plt.xlabel("Years")
                plt.ylabel("Numbers in '000")
                plt.show()
            if(year!=0 and month==0 and car==0):
                data = np.loadtxt('cars.csv', delimiter=',', skiprows = 1, usecols = range(1,11))
                data=data.transpose()
                year=year%2007
                values=[]
                for i in range(0,8):
                    values.append(data[year][i])
                stl.use("ggplot")
                plt.plot(car_labels,values)
                plt.title("Cars sold in the year %d..."%(2007+year))
                plt.xlabel("Cars")
                plt.ylabel("Numbers in '000")
                plt.show()
            elif(year!=0 and month!=0 and car==0):
                year=year%2007
                values=[]
                for i in range(1,9):
                    if (i==1):
                        file="Alto.csv"
                    if (i==2):
                        file="Belano.csv"
                    if (i==3):
                        file="Desire.csv"
                    if (i==4):
                        file="Ertiga.csv"
                    if (i==5):
                        file="Gypsy.csv"
                    if (i==6):
                        file="Omni.csv"
                    if (i==7):
                        file="Swift.csv"
                    if (i==8):
                        file="WagonR.csv"
                    data = np.loadtxt(file, dtype='str', delimiter=',',skiprows = 1, usecols = range(1,11))
                    values.append(data[month-1][year])
                month_labels = np.loadtxt(file, dtype='str', delimiter=',', usecols = (0,))
                month_name=month_labels[month]
                stl.use("ggplot")
                plt.plot(car_labels,values)
                plt.title("Cars sold in the year %d, in the month of %s..."%((2007+year),month_name))
                plt.xlabel("Cars")
                plt.ylabel("Numbers in '000")
                plt.show()
        else:
            values=[]
            year=year%2007
            if (car==1):
                file="Alto.csv"
            if (car==2):
                file="Belano.csv"
            if (car==3):
                file="Desire.csv"
            if (car==4):
                file="Ertiga.csv"
            if (car==5):
                file="Gypsy.csv"
            if (car==6):
                file="Omni.csv"
            if (car==7):
                file="Swift.csv"
            if (car==8):
                file="WagonR.csv"
    
            if(car==0):
                data = np.loadtxt("cars.csv", dtype='str', delimiter=',', skiprows=1, usecols = range(1,11))
                car_labels = np.loadtxt('cars.csv', dtype='str', delimiter=',', skiprows = 1, usecols = (0,))
                for i in range(0,8):
                    values.append(data[i][year])
                plt.pie(values, labels=car_labels, autopct='%1.1f%%', shadow=True, startangle=90)
                plt.axis('equal')
                plt.title("Percentage of cars sold in the year %d"%(2007+year))
                plt.show()
            else:
                data = np.loadtxt(file, dtype='str', delimiter=',', skiprows=1, usecols = range(1,11))
                month_labels = np.loadtxt(file, dtype='str', delimiter=',', skiprows=1, usecols = (0,))
                for i in range(0,12):
                    values.append(data[i][year])
                car_name=file[0:-4]
                plt.pie(values, labels=month_labels, autopct='%1.1f%%', shadow=True, startangle=90)
                plt.axis('equal')
                plt.title("Percentage of %ss sold in all the months of year %d"%(car_name,2007+year))
                plt.show()

        return (0)

mode=int(input("Enter mode...0 for Plotting and 1 for Prediction...\n"))

if (mode==0):
    pre_year=0
    graph=int(input("Enter Graph Type...0 for Pie Chart and 1 for Bar Graph...\n"))
    if(graph==1):
        year=int(input("Enter Year...0 for all...\n"))
        month=int(input("Enter Month Number...0 for all...\n"))
        car=int(input("Enter Car's Serial Number...0 for all...\n"))
    else:
        year=int(input("Enter Year...0 for all...\n"))
        car=int(input("Enter Car's Serial Number...0 for all...\n"))
        month=0
else:
    year=0;
    graph=0;
    car=int(input("Enter Car's Serial Number...0 for all...\n"))
    month=int(input("Enter Month Number...0 for all...\n"))
    pre_year=int(input("Enter Year for Prediction...\n"))

f=function(mode, year, month, car, pre_year, graph)
print("Predicted Value = %d\n" %(f))
