import calculation as cl
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)


# Input user's data and record to original data set(Need only what is handled in this project)
def ui(user, avg, data, direction):

    if direction == 'y' :
    
        print("You can skip some Information. It will be replaced with average.\n")
        for i in [2,5,6,7,12,13,14,15,16,17,18,25]:
            if i == 2:
                name = '(1. male 2. female)'
            elif i == 5:
                name = 'Height'
            elif i == 6:
                name = 'Weight'
            elif i == 7:
                name = 'Waist measurement'
            elif i == 12:
                name = 'Contraction Blood Pressure'
            elif i == 13:
                name = 'Relaxtion Blood Pressure'
            elif i == 14:
                name = 'Blood Sugar rate befor meal'
            elif i == 15:
                name = 'Whole Cholesterol'
            elif i == 16:
                name = 'Triglycerides'
            elif i == 17:
                name = 'HDL Cholesterol'
            elif i == 18:
                name = 'LDL Cholesterol'
            else:
                name = '1.smoking 2. not smoking 3. smoked before but not now'
        
            if i in (2, 25):
                if i == 2:
                    while True:
                        user_value = (input("Choose one(You can't skip this) {0} : ".format(name)))
                        if user_value in('1', '2'):
                            break
                if i == 25:
                    while True:
                        user_value = (input("Choose one(You can't skip this) {0} : ".format(name)))
                        if user_value in ('1', '2', '3'):
                            break
                    else:
                        print("Wrong Input. Please Try again")
            else:
                user_value = float(input("Please Input your {0}(If you want to skip this data input 0) : ".format(name)))

            user[i] = user_value
    
        data.append(user)
    
        print("\nCalculating..Please Wait..")
    
        for j in [5,6,7,12,13,14,15,16,17,18]:
            avg[j] = cl.calc_average(j, data)
            if user[j] == 0:
                user[j] = avg[j]
            
    else:
        print("\nCalculating..Please Wait..")
        for i in [5,6,7,12,13,14,15,16,17,18]:
            avg[i] = cl.calc_average(i, data)
            user[i] = avg[i]


# Declare function for draw the Graph
def graph(name, standard ,indicator, users, sex):
    truth = 0
    indicator.insert(0, standard)

    if indicator[1] != users and users != 23.982040006760176:
        x_name=('standard','whole', 'male' , 'female' , 'yours')
        truth = 1
        
    else :
        del indicator[4]
        x_name=('standard','whole', 'male' , 'female')

    y1_value = indicator
    n_groups = len(x_name)
    index = np.arange(n_groups)

    plt.bar(index, y1_value, tick_label=x_name, width = 0.5 , align='center')
    plt.title(name)
    plt.show()

    if truth == 1:
        print("The diffrence between you and standard", "%0.2f" % (users - standard))
        print("The diffrence between you and whole avearage","%0.2f" % (users - indicator[1]))
    
    if sex == 1 :
        print("The diffrence between you and male avearage","%0.2f" % (users - indicator[2]))   
    elif sex == 2 :
        print("The diffrence between you and female avearage" ,"%0.2f" % (users - indicator[3]))

def smoke_graph(name, indicator):

    x_name=('Whole', 'Male' , 'Female')
    y1_value = indicator
    n_groups = len(x_name)
    index = np.arange(n_groups)
    

    plt.bar(index,  y1_value,  tick_label=x_name, width = 0.3)
    plt.title(name)
    plt.show()


def prior_death_Rate(name, indicator):

    x_name=('당뇨병', '고혈압성 질환' , '심장질환', '뇌혈관 질환')
    y1_value = indicator
    n_groups = len(x_name)
    index = np.arange(n_groups)
    

    plt.bar(index,  y1_value,  tick_label=x_name, width = 0.3)
    plt.title(name)
    plt.show()

def bl_chl_graph(user ,target_list):
    x = []
    y = []
    
    for i in range(len(target_list)-1):
        i = i+1
        if target_list[i][12] =='' or target_list[i][15] =='' or float(target_list[i][12]) < 150 or float(target_list[i][15]) < 200:
            pass
        else:
            x.append(float(target_list[i][12]))
            y.append(float(target_list[i][15]))
    plt.figure()
    plt.xlim(150, 240)
    plt.ylim(200, 500)
    plt.scatter(x,y, s=0.3)
    plt.scatter(user[12], user[15], s = 15 , c = 'r', label = 'Yours')
    plt.legend()
    plt.title("Both High Blood pressure and Cholesterol")
    plt.show()

def bl_su_graph(user,target_list):
    x = []
    y = []

    for i in range(len(target_list)-1):
        i = i+1
        if target_list[i][12] =='' or target_list[i][14] =='' or float(target_list[i][12]) < 150 or float(target_list[i][14]) < 125:
            pass
        else:
            x.append(float(target_list[i][12]))
            y.append(float(target_list[i][14]))
    plt.figure()
    plt.xlim(150, 240)
    plt.ylim(120, 500)
    plt.scatter(x,y, s=0.3)
    plt.scatter(user[12], user[14], s = 15 , c = 'r', label = 'Yours')
    plt.legend()
    plt.title("Both High Blood pressure and Blood Sugar")
    plt.show()    

def chl_su_graph(user, target_list):
    x = []
    y = []

    for i in range(len(target_list)-1):
        i = i+1
        if target_list[i][15] =='' or target_list[i][14] =='' or float(target_list[i][15]) < 200 or float(target_list[i][14]) < 125:
            pass
        else:
            x.append(float(target_list[i][14]))
            y.append(float(target_list[i][15]))
    plt.figure()
    plt.xlim(125, 300)
    plt.ylim(200, 500)
    plt.scatter(x,y, s=0.3)
    plt.scatter(user[14], user[15], s = 15 , c = 'r', label = 'Yours')
    plt.legend()
    plt.title("Both High Blood Sugar and Cholesterol")
    plt.show()    