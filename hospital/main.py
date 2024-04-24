import csv
import pandas as pd
from hospital import models 
import random 
from .qlearning import MDP

file_path = "C:\\Users\\TEJAS\\Desktop\\EDI PROJECT\\hospital\\persons.csv"
data = pd.read_csv(file_path)
low = pd.DataFrame(columns=data.columns)
medium = pd.DataFrame(columns=data.columns)
high = pd.DataFrame(columns=data.columns)
listP = []
def write_csv():
    queryset = models.Patient.objects.all()

    with open(file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        writer.writerow(['id', 'symptoms', 'assignedDoctorId'])  # Write headers outside the loop

        for person in queryset:
            writer.writerow([person.id, person.symptoms, person.assignedDoctorId])




def pseudo_main():
    
    write_csv()
    Time()
    Distribution()
    class1 = MDP(listP)
    class1.Actions()
    class1.Q_learning()
    Final_List =max( class1.Q[class1.time_slots - 1])
    print(Final_List[1])
    return Final_List[1]


severity_levels = {'low': [], 'medium': [], 'high': []}

def Distribution():
    print(data)
    if "symptoms" in data.columns:
         data.drop('symptoms',inplace=True,axis=1)
    temp = data.values.tolist()
    for patient in temp:
        severity = int(patient[2])
        patient[0],patient[1] =patient[1],patient[0]
        
        listP.append(patient)   
        if severity <= 2:
            severity_levels['low'].append(patient)
        elif severity <= 4:
            severity_levels['medium'].append(patient)
        else:
            severity_levels['high'].append(patient)
    # print(severity_levels)
newlist = []
def Time(): 
    Time = []
    for i in range(10,14):
        Time.append(i)
    column_to_update = 'Time' 
    random.seed(42)
    if "Time" not in data.columns:
        data.insert(0,'Time',0)
    for i in range(data.shape[0]):
        data['Time'][i] = random.choice(Time)