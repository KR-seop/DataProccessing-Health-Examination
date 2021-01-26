# Return the whole average of indicator in certain list, except bmi.
def calc_average(n, target_list):
    index = 0
    result = 0

    for i in range(len(target_list)-1):
        i = i + 1
        if target_list[i][n] == '':
            pass
        else:
            result += float(target_list[i][n])
            index += 1       

    return (result / index)

# From Here, Calculating each of health rate Functions Declare.
# The range of health rate is 1 to 2, lower is better.

# Calculating bmi and weight_rate. Return average of bmi and health rate of bmi

def weight_rate(target_list):
    sum_rate = []
    index = 0
    all_bmi = 0
    for i in range(1, len(target_list)):
        if target_list[i][6] == '' or target_list[i][5] == '':
            pass
        else:
            bmi = float(target_list[i][6])/((float(target_list[i][5])/100)**2)
            all_bmi += bmi
            index += 1
            if bmi < 18.5 :
                sum_rate.append(1.7)
            elif 18.5 <= bmi < 23 :
                sum_rate.append(1)
            elif 23 <= bmi < 25:
                sum_rate.append(1.1)
            elif 25 <= bmi < 27:
                sum_rate.append(1.3)
            elif 27 <= bmi <30:
                sum_rate.append(1.5)
            elif bmi >= 30:
                sum_rate.append(2)
    result = 0
    avg_bmi = all_bmi / index
    for j in range(len(sum_rate)):
        result += sum_rate[j]

    return [result / index, avg_bmi, all_bmi]

# Calculating health rate of blood pressure.
def bl_press_rate(target_list):
    high_pressure_rate = []
    sum_rate = 0
    index = 0
    for i in range(len(target_list)-1):
        i = i + 1
        index += 1
        if target_list[i][12] == '' or target_list[i][13] == '':
            pass
        else:
            contraction = float(target_list[i][12])
            relaxation = float(target_list[i][13]) 
            if contraction < 120 and relaxation <80 :
                high_pressure_rate.append(1)
            elif 120 <= contraction < 129 or 80 <=relaxation < 84:
                high_pressure_rate.append(1.2)
            elif 130 <= contraction < 140 or 84 <= relaxation < 90:
                high_pressure_rate.append(1.4)
            elif 140 <= contraction < 160 or 90 <= relaxation < 100:
                high_pressure_rate.append(1.6)   
            elif 160 <= contraction < 200 or 100 <= relaxation < 140:
                high_pressure_rate.append(1.9)
            elif 200 <= contraction or 140 <= relaxation:
                high_pressure_rate.append(2)

    for j in range(len(high_pressure_rate)):
        sum_rate += high_pressure_rate[j]

    return [high_pressure_rate, (sum_rate / index)]


# Calculating health rate of blood sugar before meal
def bl_sugar_rate(target_list):
    sugar_rate = []
    sum_rate = 0
    index = 0
    low_sugar = 0
    low_sugar_ratio = 0
    for i in range(len(target_list)-1):
        i = i + 1
        if target_list[i][14] == '' :
            pass
        else :
            index += 1
            bl_sugar = float(target_list[i][14])
            if  70 <= bl_sugar < 100:
                sugar_rate.append(1)
            elif bl_sugar < 70 : 
                sugar_rate.append(1.5)
                low_sugar += 1
            elif 100 <= bl_sugar < 125:
                sugar_rate.append(1.4)
            elif 125 <= bl_sugar < 150:
                sugar_rate.append(1.7)
            elif 150 <= bl_sugar < 200:
                sugar_rate.append(1.8)
            elif 200 <= bl_sugar:
                sugar_rate.append(2.0)

    for j in range(len(sugar_rate)):
        sum_rate += sugar_rate[j]
    
    low_sugar_ratio = low_sugar / index
    result = [sum_rate / index, low_sugar_ratio*100, sugar_rate]

    return result


def cholesterol_level(target_list):
    chl_rate = []
    sum_rate = 0
    index = 0
    for i in range(len(target_list)-1):
        i = i + 1
        if target_list[i][15] == '' :
            pass
        else :
            index += 1
            chl_level = float(target_list[i][15])
            if  chl_level < 200:
                chl_rate.append(1)
            elif 200 <= chl_level < 240:
                chl_rate.append(1.5)
            elif 240 <= chl_level < 300:
                chl_rate.append(1.8)
            elif 300 <= chl_level:
                chl_rate.append(2.0)

    for j in range(len(chl_rate)):
        sum_rate += chl_rate[j]

    return [sum_rate / index, chl_rate]

def trigly_level(target_list):
    tri_rate = []
    sum_rate = 0
    index = 0
    for i in range(len(target_list)-1):
        i = i + 1
        if target_list[i][16] == '' :
            pass
        else :
            index += 1
            tri_level = float(target_list[i][16])
            if  tri_level < 150:
                tri_rate.append(1)
            elif 150 <= tri_level < 200:
                tri_rate.append(1.5)
            elif 200 <= tri_level < 500:
                tri_rate.append(1.7)
            elif 500 <= tri_level:
                tri_rate.append(2.0)
    for j in range(len(tri_rate)):
        sum_rate += tri_rate[j]

    return [sum_rate / index, tri_rate]

def hdl_level(target_list):
    hdl_rate = []
    sum_rate = 0
    index = 0
    for i in range(len(target_list)-1):
        i = i + 1
        if target_list[i][17] == '' :
            pass
        else :
            index += 1
            hdl_level = float(target_list[i][17])
            if  hdl_level >= 60 :
                hdl_rate.append(1)
            elif 40 <= hdl_level < 60 :
                hdl_rate.append(1.2)
            elif hdl_level < 40:
                hdl_rate.append(2.0)

    for j in range(len(hdl_rate)):
        sum_rate += hdl_rate[j]

    return [sum_rate / index, hdl_rate]

def ldl_level(target_list):
    ldl_rate = []
    sum_rate = 0
    index = 0
    for i in range(len(target_list)-1):
        i = i + 1
        if target_list[i][18] == '' :
            pass
        else :
            index += 1
            ldl_level = float(target_list[i][18])
            if  ldl_level < 100:
                ldl_rate.append(1)
            elif 100 <= ldl_level < 130:
                ldl_rate.append(1.3)
            elif 130 <= ldl_level <160:
                ldl_rate.append(1.6)
            elif 160 <= ldl_level < 190:
                ldl_rate.append(1.8)
            elif 190 <= ldl_level :
                ldl_rate.append(2.0)
    for j in range(len(ldl_rate)):
        sum_rate += ldl_rate[j]

    return [sum_rate / index, ldl_rate]

# Return now smoking rate
def smoking(target_list):
    now_smoke = 0
    index = 0
    for i in range(len(target_list)-1):
        i = i + 1
        if target_list[i][25] == '' :
            pass
        else:
            index += 1
            if float(target_list[i][25]) == 3:
                now_smoke += 1
           

    result = (now_smoke / index)*100 

    return result



def relation_Bp_Bs_Cl(target_list):
    bl_chl = 0
    bl_su = 0
    chl_su = 0
    index = 0 

    for i in range(len(target_list)-1):
        i = i + 1
        index += 1
        
        if target_list[i][12] == '' or target_list[i][14] == '' or target_list[i][15] == '' : 
            pass
        else :
            contraction = float(target_list[i][12])
            sugar = float(target_list[i][14])
            cholesterol = float(target_list[i][15])
            if (150 <= contraction) and (200 <= cholesterol) :
                bl_chl += 1
            elif (150 <= contraction) and (125 <= sugar) :
                bl_su += 1
            elif (125 <= sugar) and (200 <= cholesterol):
                chl_su += 1
        
    return [bl_su/index * 100 , bl_chl/index * 100 , chl_su/index * 100]

def over_weight(target_list):
    over = 0
    index = 0
    for i in range(len(target_list)-1):
        i = i+1
        if target_list[i][7] == '' or target_list[i][2] == '' or target_list[i][6] == '' or target_list[i][5] == '' or target_list[i][16] == '':
            pass
            
        else:
            index += 1
            bmi = float(target_list[i][6])/((float(target_list[i][5])/100)**2)
            if float(target_list[i][2]) == 1 :
                if float(target_list[i][7]) >= 90 and float(target_list[i][16]) >= 150 and bmi >= 25 :
                    over += 1
            else :
                if float(target_list[i][7]) >= 85 and float(target_list[i][16]) >= 150 and bmi >= 25:
                    over += 1
    return (over / index) * 100


def relation_smoke1(ind, target_list):
    
    index_sm = 0
    index_nsm = 0
    sm = 0
    nsm = 0
    
    if ind == 12 :
        num = 150
    elif ind == 14 :
        num = 125
    elif ind == 15:
        num = 240

    for i in range(len(target_list)-1):
        i = i + 1
        if target_list[i][ind] == '' or target_list [i][25] == '': 
            pass
        else :
            smoke = float(target_list[i][25])
            indicator = float(target_list[i][ind])
            if smoke == 1 :
                index_sm += 1
                if num <= indicator:
                    sm += 1
                    
            if smoke == 2 or smoke == 3 :
                index_nsm += 1
                if num <= indicator :
                    nsm += 1
        
    return [(sm / index_sm) * 100 , (nsm / index_nsm) * 100]