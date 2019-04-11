import requests
import datetime
 
# getting current date and time, this is in UTC format
d = datetime.datetime.today()

# getting current year
currentYear = d.year
 
#getting current month
currentMonth = d.month
 
#getting current day
currentDay = d.day


def potholeScore():
    url = "https://chelseama.ogopendata.com/datastore/odata3.0/50fd4973-d1c9-4897-8b7d-092a87ebc23b?&$top=5000000&$format=json"
    r = requests.get(url)
    data = r.json()
    #print(data)
    potholes = data['value']
    scores = []
    for row in potholes:
     closed_days = float(row['Days to Closed'])
     if (closed_days < 7 and row['Category'] == 'Pothole'):
       scores.append(1)
     else:
       scores.append(0)
       
    pothole_score = (sum(scores) / len(scores))
    print('pothole score', pothole_score)
    
#results = potholeScore()

def theft():
    #if you search for motor in type you get all the motor theft vehicle incidents
    #search "Robbery - Street" in type and you get all of them
    #search "Assault"
    url = "https://chelseama.ogopendata.com/datastore/odata3.0/fceb31a5-3ebc-48de-baf6-979cf53b7e2b?&$top=5000000&$format=json"
    r = requests.get(url)
    data = r.json()
    theft = data['value']
    scores = []
    for row in theft:
     #closed_days = float(row['Days to Closed'])
        if ('Theft' in row['Type'] ):
            scores.append(1)
    print(scores)
    #this is the total number of thefts in the date
    totalNumberOfThefts = len(scores)

#These are the total number of scores 
#result = theft()

"""
def theftHistoricData():
    #I'm computing the month by month average scores of the historic data.
    url = "https://chelseama.ogopendata.com/datastore/odata3.0/1ccc9e28-0f47-4866-ba00-8ed5b4ef5ef5?&$top=5000000&$format=json"
    r = requests.get(url)
    data = r.json()
    theft = data['value']
    scores = []
    for row in theft:
        month,day,year = str(row['Date']).split('/')
        if ('Theft' in row['Type']):
            if  (month == '10' and year == '12'):
                scores.append(1)
    print(scores)
    #this is the total number of thefts in the date
    totalNumberOfThefts = len(scores)
    print(totalNumberOfThefts)
    

theftHistoricData()
"""

def theftHistoricDataDict():
    #I'm computing the month by month average scores of the historic data.
    url = "https://chelseama.ogopendata.com/datastore/odata3.0/1ccc9e28-0f47-4866-ba00-8ed5b4ef5ef5?&$top=5000000&$format=json"
    r = requests.get(url)
    data = r.json()
    theft = data['value']
    dict = {}
    for row in theft:
        month,day,year = str(row['Date']).split('/')
        if ('Theft' in row['Type']):
            if year == '17':
                monthYear = month + '/' + year
                dict[monthYear] = dict.get(monthYear, 0) +1
    print(dict)
    print(len(dict))
    totalMonths = 0
    totalThefts = 0
    for date in dict:
        value = dict[date]
        totalThefts += value
        totalMonths +=1
    print(totalThefts,totalMonths)
    #Average of 38.1785714 thefts per months
#theftHistoricDataDict()


def assaultHistoricData():
    #I'm computing the month by month average scores of the historic data.
    url = "https://chelseama.ogopendata.com/datastore/odata3.0/1ccc9e28-0f47-4866-ba00-8ed5b4ef5ef5?&$top=5000000&$format=json"
    r = requests.get(url)
    data = r.json()
    theft = data['value']
    dict = {}
    for row in theft:
        month,day,year = str(row['Date']).split('/')
        if ('Assault' in row['Type'] or 'assault' in row['Type']):
            if year == '17':
                monthYear = month + '/' + year
                dict[monthYear] = dict.get(monthYear, 0) +1
    print(dict)
    print(len(dict))
    totalMonths = 0
    totalThefts = 0
    for date in dict:
        value = dict[date]
        totalThefts += value
        totalMonths +=1
    print(totalThefts,totalMonths)
#assaultHistoricData()

def RobberyStreetHistoricData():
    url = "https://chelseama.ogopendata.com/datastore/odata3.0/1ccc9e28-0f47-4866-ba00-8ed5b4ef5ef5?&$top=5000000&$format=json"
    r = requests.get(url)
    data = r.json()
    theft = data['value']
    dict = {}
    for row in theft:
        month,day,year = str(row['Date']).split('/')
        if ('Robbery - Street' in row['Type']):
            if year == '17':
                monthYear = month + '/' + year
                dict[monthYear] = dict.get(monthYear, 0) +1
    print(dict)
    print(len(dict))
    totalMonths = 0
    totalThefts = 0
    for date in dict:
        value = dict[date]
        totalThefts += value
        totalMonths +=1
    print(totalThefts,totalMonths)
#RobberyStreetHistoricData()

#assigning global variables for the historic static data
    
def CurrentRobbingStreetScore():
    #calculate year score, this will be done by taking into consideration data from today's date - 1 year
    url = "https://chelseama.ogopendata.com/datastore/odata3.0/fceb31a5-3ebc-48de-baf6-979cf53b7e2b?&$top=5000000&$format=json"
    r = requests.get(url)
    data = r.json()
    theft = data['value']
    #calculating year score
    YearScore = []
    for row in theft:
        #think about edge case January
        month,day,year = str(row['Date']).split('/')
        if ('Robbery - Street' in row['Type']):
            if(int(year)  == currentYear):
                YearScore.append(1)
            elif(int(year) == currentYear - 1 and int(month) > currentMonth):
                YearScore.append(1)
            elif(int(year) == currentYear - 1 and int(month) >= currentMonth and int(day) >= currentDay):
                YearScore.append(1)

    print(YearScore)
    #total number of robbings this year
    TotalNumberOfRobbingYear = len(YearScore)
    print(TotalNumberOfRobbingYear)

    #calculating month score, information is outdated the months score can't be calculated
    MonthScore = []
    for row in theft:
        month,day,year = str(row['Date']).split('/')
        if ('Robbery - Street' in row['Type']):
            if(int(year)  == currentYear and int(month) == currentMonth):
                MonthScore.append(1)
            #edge case if it's January
            elif(int(year) == currentYear - 1 and int(month) == 12 and currentMonth == 1 and int(day) >= currentDay):
                MonthScore.append(1)
            elif(int(year) == currentYear and int(month) == currentMonth -1 and int(day) >= currentDay):
                MonthScore.append(1)
    print(MonthScore)
    #total number of robbings this year
    TotalNumberOfRobbingMonth = len(MonthScore)
    print(TotalNumberOfRobbingMonth)
    
    #calculating the day score will be yesterdays score.

    #dictDay is a key value pair with months per day
    dictDays = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31,11:30, 12:31}
    DayScore = []
    for row in theft:
        month,day,year = str(row['Date']).split('/')
        if ('Robbery - Street' in row['Type']):
            if(int(year) == currentYear and int(month) == currentMonth and int(day) == currentDay -1):
                DayScore.append(1)
            elif(int(year) == currentYear -1 and int(month) == 12 and currentDay == 1 and int(day) == 31 and currentMonth == 1):
                DayScore.append(1)
                #calculate Dec. 31st score, since today is Jan 1st
            #now test to see if we're in the first of this month
            elif(currentDay == 1 and int(year) == currentYear and int(month)== currentMonth - 1 and int(day) == dictDays[int(month)]):
                DayScore.append(1)
            
        
    print(DayScore)
    #total number of robbings this year
    TotalNumberOfRobbingDay = len(DayScore)
    print(TotalNumberOfRobbingDay)

    

CurrentRobbingStreetScore()
