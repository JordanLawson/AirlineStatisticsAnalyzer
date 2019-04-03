#Jordan Lawson
#CSCI 431 PROJECT
#April 30, 2018
#This program evaluates airline flight data

import cmd, sys, pandas
from collections import OrderedDict
from tkinter import *
pandas.set_option('display.expand_frame_repr',False)
currentDisplay=pandas.DataFrame()#Holds the data frame to be displayed on screen, intitially blank



#Changes a string with a month number into the month name
def monthName(month):
    name=""
    if month == 1:
        name="January"
    elif month ==2 :
        name="February"
    elif month == 3:
        name="March"
    elif month == 4:
        name="April"
    elif month == 5:
        name="May"
    elif month == 6:
        name="June"
    elif month == 7:
        name="July"
    elif month == 8:
        name="August"
    elif month == 9:
        name="September"
    elif month == 10:
        name="October"
    elif month == 11:
        name="November"
    elif month == 12:
        name="December"
    else:
        name="Error"
        print("ERROR INVALID MONTH")
    return name;
#End monthName


#Changes a string with a month name into the month number
def monthInt(month):
    num=0
    if month == "January":
        num=1
    elif month == "February":
        num=2
    elif month == "March":
        num=3
    elif month == "April":
        num=4
    elif month == "May":
        num=5
    elif month == "June":
        num=6
    elif month == "July":
        num=7
    elif month == "August":
        num=8
    elif month == "September":
        num=9
    elif month == "October":
        num=10
    elif month == "November":
        num=11
    elif month == "December":
        num=12
    else:
        num=0
        print("ERROR INVALID MONTH")
    return num;
#End monthInt



#Returns list of average month scores in order of month
def bestMonth():
    monthFrame1=(bestOfMonth(1,data))
    monthFrame2=(bestOfMonth(2,data))
    monthFrame3=(bestOfMonth(3,data))
    monthFrame4=(bestOfMonth(4,data))
    monthFrame5=(bestOfMonth(5,data))
    monthFrame6=(bestOfMonth(6,data))
    monthFrame7=(bestOfMonth(7,data))
    monthFrame8=(bestOfMonth(8,data))
    monthFrame9=(bestOfMonth(9,data))
    monthFrame10=(bestOfMonth(10,data))
    monthFrame11=(bestOfMonth(11,data))
    monthFrame12=(bestOfMonth(12,data))

    monthScores=[
    monthFrame1['SCORE'].mean(),
    monthFrame2['SCORE'].mean(),
    monthFrame3['SCORE'].mean(),
    monthFrame4['SCORE'].mean(),
    monthFrame5['SCORE'].mean(),
    monthFrame6['SCORE'].mean(),
    monthFrame7['SCORE'].mean(),
    monthFrame8['SCORE'].mean(),
    monthFrame9['SCORE'].mean(),
    monthFrame10['SCORE'].mean(),
    monthFrame11['SCORE'].mean(),
    monthFrame12['SCORE'].mean()
    ]

    return monthScores;
#End best month




#Find best filghts in a particular month
#Month takes in a integer to determine which month to use
#Month: 1=January, 2=Feb... 12=December
#csvDataFrame takes in a Pandas data frame
#Returns an ordered Pandas data frame
def bestOfMonth(month, csvDataFrame):
    newData=csvDataFrame[['SCORE','SUCCESS_RATE','MONTH','UNIQUE_CARRIER_NAME','SEATS','DEPARTURES_SCHEDULED','DEPARTURES_PERFORMED']].copy()
    newData=newData.drop(newData[newData.MONTH != month].index)
    return newData;
#End bestOfMonth




#Button buttonPress
def buttonPress():
    output.delete('1.0',END)#Clears output section of screen
    selection=choice.get()#Holds the current user selection
    currentDisplay=data[['SCORE','SUCCESS_RATE','DISTANCE_RANGE','MONTH','UNIQUE_CARRIER_NAME','SEATS','DISTANCE']].copy()#Reduced data table to display
    monthList=['January','February','March','April','May','June','July','August','September','October','November','December']

    #Check if selection is a month
    if selection in monthList:
        currentDisplay = bestOfMonth(monthInt(selection),data)
 
    elif selection=="Automatic":
        currentDisplay=data[['SCORE','SUCCESS_RATE','DISTANCE_RANGE','AIRCRAFT_TYPE','MONTH','UNIQUE_CARRIER_NAME','SEATS']].copy()
        #Determine best month
        monthList=bestMonth()
        monthNum=monthList.index(max(monthList))+1
        #Determine best aircraft
        tableAir=aircraft.sort_values('SCORE',ascending=False)
        airCol=tableAir.columns.get_loc("NAME")
        bestAir=tableAir.iloc[0,airCol]
        #Determine best carrier
        tableCar=carrier.sort_values('SCORE',ascending=False)
        carCol=tableCar.columns.get_loc("NAME")
        bestCar=tableCar.iloc[0,carCol]        
        #Determine best carrier
        tableDes=destCity.sort_values('SCORE',ascending=False)
        desCol=tableDes.columns.get_loc("NAME")
        bestDes=tableDes.iloc[0,desCol]        
        
        
        output.insert(END,"BEST AIRCRAFT IS TYPE : "+ str(bestAir) +"\n")
        output.insert(END,"This aircraft type had the higher total score of all flight data.\n")
        output.insert(END,"BEST CARRIER IS TYPE : "+ str(bestCar) +"\n")
        output.insert(END,"This carrier type had the higher total score of all flight data.\n")
        output.insert(END,"BEST DESTINATION IS TYPE : "+ str(bestDes) +"\n")
        output.insert(END,"This destination had the higher total score of all flight data.\n")
        output.insert(END,"BEST MONTH IS : "+monthName(monthNum)+"\n")
        output.insert(END,"Best Month average score : "+str(currentDisplay['SCORE'].mean())+" is higher that every other month.\n\n")
        output.insert(END, "The flights with the best score are listed below.\n")
        currentDisplay=currentDisplay.sort_values('SCORE',ascending=False)
        
 
    elif selection=="Best Aircraft & Month":
        currentDisplay=data[['SCORE','SUCCESS_RATE','DISTANCE_RANGE','AIRCRAFT_TYPE','MONTH','UNIQUE_CARRIER_NAME','SEATS']].copy()
        #Determine best month
        monthList=bestMonth()
        monthNum=monthList.index(max(monthList))+1
        #Remove all flights not during best month
        currentDisplay=currentDisplay.drop(currentDisplay[currentDisplay.MONTH != monthNum].index)
        #Determine best aircraft
        tableAir=aircraft.sort_values('SCORE',ascending=False)
        airCol=tableAir.columns.get_loc("NAME")
        bestAir=tableAir.iloc[0,airCol]
        #Remove all filghts not with the best aircraft
        currentDisplay=currentDisplay.drop(currentDisplay[currentDisplay.AIRCRAFT_TYPE != bestAir].index)
        output.insert(END,"BEST AIRCRAFT IS TYPE : "+ str(bestAir) +"\n")
        output.insert(END,"This aircraft type had the higher total score of all flight data.\n")
        output.insert(END,"BEST MONTH IS : "+monthName(monthNum)+"\n")
        output.insert(END,"Best Month average score : "+str(currentDisplay['SCORE'].mean())+" is higher that every other month.\n\n")
        output.insert(END,"The flights for this aircraft during the best month are listed below.\n")


    elif selection=="Best Carrier & Month":
        currentDisplay=data[['SCORE','SUCCESS_RATE','DISTANCE_RANGE','AIRCRAFT_TYPE','MONTH','UNIQUE_CARRIER_NAME','SEATS']].copy()
        #Determine best month
        monthList=bestMonth()
        monthNum=monthList.index(max(monthList))+1
        #Remove all flights not during best month
        currentDisplay=currentDisplay.drop(currentDisplay[currentDisplay.MONTH != monthNum].index)
        #Determine best carrier
        tableCar=carrier.sort_values('SCORE',ascending=False)
        carCol=tableCar.columns.get_loc("NAME")
        bestCar=tableCar.iloc[0,carCol]
        #Remove all filghts not with the best carrier
        currentDisplay=currentDisplay.drop(currentDisplay[currentDisplay.UNIQUE_CARRIER_NAME != bestCar].index)
        output.insert(END,"BEST CARRIER IS TYPE : "+ str(bestCar) +"\n")
        output.insert(END,"This carrier type had the higher total score of all flight data.\n")
        output.insert(END,"BEST MONTH IS : "+monthName(monthNum)+"\n")
        output.insert(END,"Best Month average score : "+str(currentDisplay['SCORE'].mean())+" is higher that every other month.\n\n")
        output.insert(END,"The flights for this carrier during the best month are listed below.\n")


    elif selection=="Best Destination & Month":
        currentDisplay=data[['SCORE','SUCCESS_RATE','DISTANCE_RANGE','DEST_CITY_NAME','MONTH','UNIQUE_CARRIER_NAME','SEATS']].copy()
        #Determine best month
        monthList=bestMonth()
        monthNum=monthList.index(max(monthList))+1
        #Remove all flights not during best month
        currentDisplay=currentDisplay.drop(currentDisplay[currentDisplay.MONTH != monthNum].index)
        #Determine best carrier
        tableDes=destCity.sort_values('SCORE',ascending=False)
        desCol=tableDes.columns.get_loc("NAME")
        bestDes=tableDes.iloc[0,desCol]
        #Remove all filghts not with the best carrier
        currentDisplay=currentDisplay.drop(currentDisplay[currentDisplay.DEST_CITY_NAME != bestDes].index)
        output.insert(END,"BEST DESTINATION IS TYPE : "+ str(bestDes) +"\n")
        output.insert(END,"This destination had the higher total score of all flight data.\n")
        output.insert(END,"BEST MONTH IS : "+monthName(monthNum)+"\n")
        output.insert(END,"Best Month average score : "+str(currentDisplay['SCORE'].mean())+" is higher that every other month.\n\n")
        output.insert(END,"The flights to this city during the best month are listed below.\n")
        
    
    elif selection=="Aircraft":
        currentDisplay=aircraft.sort_values('SCORE',ascending=False)
        output.insert(END,"BEST AIRCRAFT IS TYPE : " +(currentDisplay['NAME'].head(1).reset_index(drop=True).to_string()+"\n"))
        output.insert(END,"This aircraft type had the higher total score of all flight data.\n")
        output.insert(END,"All aircraft type numbers and there scores are shown below.\n")

    elif selection=="Best Month":
        monthList=bestMonth()
        monthNum=monthList.index(max(monthList))+1#Determines best month
        currentDisplay=currentDisplay.drop(currentDisplay[currentDisplay.MONTH != monthNum].index)#Reduces data table to only best month
        output.insert(END,"BEST MONTH IS : "+monthName(monthNum)+"\n")
        output.insert(END,"Best Month average score : "+str(currentDisplay['SCORE'].mean())+" is higher that every other month.\n\n")
        for i in range(1,13):
            output.insert(END,(monthName(i)+" : " + str(monthList[i-1])+"\n"))
        output.insert(END,"\n\nBest month flights shown below."+"\n\n\n")

    elif selection=="Carrier":
        currentDisplay=carrier.sort_values('SCORE',ascending=False)
        output.insert(END,"BEST CARRIER IS : " +(currentDisplay['NAME'].head(1).reset_index(drop=True).to_string()+"\n"))
        output.insert(END,"This carrier had the higher total score of all flight data.\n")
        output.insert(END,"All carriers and there scores are shown below.\n")

    elif selection=="State":
        currentDisplay=state.sort_values('SCORE',ascending=False)
        output.insert(END,"BEST STATE TO FLY TO IS : " +(currentDisplay['NAME'].head(1).reset_index(drop=True).to_string()+"\n"))
        output.insert(END,"This state had the higher total score of all flight data.\n")
        output.insert(END,"All state destinations and there scores are shown below.\n")

    elif selection=="Destination":
        currentDisplay=destCity.sort_values('SCORE',ascending=False)
        output.insert(END,"BEST CITY TO FLY TO IS : " +(currentDisplay['NAME'].head(1).reset_index(drop=True).to_string()+"\n"))
        output.insert(END,"This destination had the higher total score of all flight data.\n")
        output.insert(END,"All city destinations and there scores are shown below.\n")  

    elif selection=="Origin":
        currentDisplay=orCity.sort_values('SCORE',ascending=False)
        output.insert(END,"BEST CITY TO DEPART FROM IS : " +(currentDisplay['NAME'].head(1).reset_index(drop=True).to_string()+"\n"))
        output.insert(END,"This origin city had the higher total score of all flight data.\n")
        output.insert(END,"All origin cites and there scores are shown below.\n")  
        
    elif selection=="Distance":
        currentDisplay=currentDisplay.sort_values('DISTANCE')
        currentDisplay.reset_index(inplace=True)
        currentDisplay.drop(columns=['index'],inplace=True)
        output.insert(END, "The flights below are sorted from shorted travel distance to longest.\n")        
        output.insert(END, currentDisplay.to_string(justify='center'))
        output.pack()        
        return;
        
    currentDisplay=currentDisplay.sort_values('SCORE',ascending=False)
    currentDisplay.reset_index(inplace=True)
    currentDisplay.drop(columns=['index'],inplace=True)
    output.insert(END, currentDisplay.to_string(justify='center'))
    output.pack()
    return;


#End button buttonPress






#Main Begin---------------------------------

#Read in csv data
Location=r'ProjectDataS18NCSC2017.csv'
data=pandas.read_csv(Location)#Orignal data table

#PreProcess data table
data=data[data.DEPARTURES_SCHEDULED != 0]#Removes flights with no scheduled departures
data=data[data.DEPARTURES_PERFORMED < data.DEPARTURES_SCHEDULED]#Removes flights where there were more departures than scheduled
data['SUCCESS_RATE']=data['DEPARTURES_PERFORMED']/data['DEPARTURES_SCHEDULED']#Determines percentage of filghts that actually take off
data['SUCCESS_RATE']=data['SUCCESS_RATE'].clip(upper=1.0)#Prevents flights from having over 100% success rate (if they have more take offs, than scheduled)
data['SCORE']=data['SEATS']*data['SUCCESS_RATE']#Gives each flight a score based on total number of seats and success rate
data.insert(0,"DISTANCE_RANGE","")
col1=data.columns.get_loc("DISTANCE")
col2=data.columns.get_loc("DISTANCE_RANGE")
for row1 in range(0,len(data.index)):
    if(data.iat[row1,col1] in range(0,99)):
        data.iat[row1,col2]="0-99"
    if(data.iat[row1,col1] in range(100,199)):
         data.iat[row1,col2]="100-199"
    if(data.iat[row1,col1] in range(200,299)):
        data.iat[row1,col2]="200-299"
    if(data.iat[row1,col1] in range(300,399)):
        data.iat[row1,col2]="300-399"
    if(data.iat[row1,col1] in range(400,499)):
        data.iat[row1,col2]="400-499"
    if(data.iat[row1,col1] in range(500,999)):
        data.iat[row1,col2]="500-999"
    if(data.iat[row1,col1] in range(1000,1499)):
        data.iat[row1,col2]="1000-1499"
    if(data.iat[row1,col1] in range(1500,1999)):
        data.iat[row1,col2]="1500-1999"
    if(data.iat[row1,col1] in range(2000,2499)):
        data.iat[row1,col2]="2000-2499"
    if(data.iat[row1,col1] in range(2500,2999)):
        data.iat[row1,col2]="2500-2999"
    if(data.iat[row1,col1] in range(3000,3499)):
        data.iat[row1,col2]="3000-3499"
    if(data.iat[row1,col1] in range(3500,3999)):
        data.iat[row1,col2]="3500-3999"
    if(data.iat[row1,col1] in range(4000,4499)):
        data.iat[row1,col2]="4000-4499"
    if(data.iat[row1,col1] in range(4500,4999)):
        data.iat[row1,col2]="4500-4999"
#end preprocess data table ---

#Create best carrier table
carrier=pandas.DataFrame()
carrier['NAME']=data.UNIQUE_CARRIER_NAME.unique()
carrier['SCORE']=0.0

col1=data.columns.get_loc("UNIQUE_CARRIER_NAME")
col2=carrier.columns.get_loc("NAME")
col3=data.columns.get_loc("SCORE")
col4=carrier.columns.get_loc("SCORE")
for row1 in range(0,len(data.index)):
    for row2 in range(0,len(carrier.index)):
        if(data.iat[row1,col1]==carrier.iat[row2,col2]):
            carrier.iat[row2, col4]=  (carrier.iat[row2,col4] + data.iat[row1,col3])
#end best carrier table---

#Create best state table
state=pandas.DataFrame()
state['NAME']=data.DEST_STATE_ABR.unique()
state['SCORE']=0.0

col1=data.columns.get_loc("DEST_STATE_ABR")
col2=state.columns.get_loc("NAME")
col3=data.columns.get_loc("SCORE")
col4=state.columns.get_loc("SCORE")
for row1 in range(0,len(data.index)):
    for row2 in range(0,len(state.index)):
        if(data.iat[row1,col1]==state.iat[row2,col2]):
            state.iat[row2, col4]=  (state.iat[row2,col4] + data.iat[row1,col3])


#end best state table---


#Create best destination table
destCity=pandas.DataFrame()
destCity['NAME']=data.DEST_CITY_NAME.unique()
destCity['SCORE']=0.0

col1=data.columns.get_loc("DEST_CITY_NAME")
col2=destCity.columns.get_loc("NAME")
col3=data.columns.get_loc("SCORE")
col4=destCity.columns.get_loc("SCORE")
for row1 in range(0,len(data.index)):
    for row2 in range(0,len(destCity.index)):
        if(data.iat[row1,col1]==destCity.iat[row2,col2]):
            destCity.iat[row2, col4]=  (destCity.iat[row2,col4] + data.iat[row1,col3])


#end best destination table---


#Create best origin table
orCity=pandas.DataFrame()
orCity['NAME']=data.ORIGIN_CITY_NAME.unique()
orCity['SCORE']=0.0

col1=data.columns.get_loc("ORIGIN_CITY_NAME")
col2=orCity.columns.get_loc("NAME")
col3=data.columns.get_loc("SCORE")
col4=orCity.columns.get_loc("SCORE")
for row1 in range(0,len(data.index)):
    for row2 in range(0,len(orCity.index)):
        if(data.iat[row1,col1]==orCity.iat[row2,col2]):
            orCity.iat[row2, col4]=  (orCity.iat[row2,col4] + data.iat[row1,col3])


#end best origin table---

#create best aircraft table
aircraft=pandas.DataFrame()
aircraft['NAME']=data.AIRCRAFT_TYPE.unique()
aircraft['SCORE']=0.0

col1=data.columns.get_loc("AIRCRAFT_TYPE")
col2=aircraft.columns.get_loc("NAME")
col3=data.columns.get_loc("SCORE")
col4=aircraft.columns.get_loc("SCORE")
for row1 in range(0,len(data.index)):
    for row2 in range(0,len(aircraft.index)):
        if(data.iat[row1,col1]==aircraft.iat[row2,col2]):
            aircraft.iat[row2, col4]=  (aircraft.iat[row2,col4] + data.iat[row1,col3])
#end best aircraft table---


#Start Window
root = Tk()
root.title('Best Flight Program')

#Window organized into frames
leftFrame=Frame(root)
leftFrame.pack(side=LEFT)
rightFrame=Frame(root)
rightFrame.pack(side=RIGHT, fill=BOTH)

#widgets
instructions=Label(leftFrame, text="Choose an option using the drop down menu.")
instructions.pack()

#Dropdown menu
choice=StringVar(root)#Creates a tkinter variable that will hold the menu item selected
choice.set('Automatic')#Default value, use choice.get() to return a string of selection
options=['Automatic','Aircraft','Carrier','Best Month','Destination',
'Distance','Origin','State','January',
'February','March','April','May',
'June','July','August','September',
'October','November','December',
'Best Aircraft & Month','Best Carrier & Month','Best Destination & Month']
menu=OptionMenu(leftFrame,choice,*options)
menu.pack()

#Used to get user selection from Dropdown menu and display the output
button1=Button(leftFrame, text="START", fg="blue", command=buttonPress)
button1.pack()

#text box to display program output based on user selection
output=Text(rightFrame, height=30, width=140)

buttonPress()#called once for automatic output


root.mainloop()


#Main End-----------------------------------
