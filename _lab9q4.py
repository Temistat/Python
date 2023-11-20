def extract_feb_averages(year_data):
    num_1 = year_data[3]
    num_2 = year_data[4]
    num_2 = year_data[5]
    line = "('{}', '{}', '{}')".format(num_1,num_2,num_3)
    return line

def extract_march_averages(year_data):
    num_1 = year_data[7]
    num_2 = year_data[8]
    num_2 = year_data[9]
    line = "('{}', '{}', '{}')".format(num_1,num_2,num_3)
    return line

def update_totals(month_totals, curr_month_avgs):
    lst = []
    for i in range(len(month_totals)):
        total = month_totals[i] + curr_month_avgs[i]
        lst.append(total)
    return lst

def analyze_data(filename):
    file = open(filename, 'r')
    full_shadow_feb_totals = [0,0,0]
    no_shadow_feb_totals = [0,0,0]
    full_shadow_mar_totals = [0,0,0]
    no_shadow_mar_totals = [0,0,0]
    firstline = file.readline()
    for line in file:
        lst = file.split(",")
        if lst[1] == "No Record":
           no_rec_feb_total = extract_feb_averages(lst)
           no_shadow_feb_totals = update_totals(no_shadow_feb_totals, no_rec_feb_total)
        elif lst[1] == "Full Shadow":
           full_shadow_feb_total = extract_feb_averages(lst)
           full_shadow_feb_totals = update_totals(full_shadow_feb_total, full_shadow_feb_totals)
        elif lst[1] == "No Record":
           no_rec_mar_total = extract_march_averages(lst)
           no_shadow_mar_totals = update_totals(no_shadow_mar_totals, no_rec_mar_total)   
        elif lst[1] == "Full Shadow":
           full_shadow_feb_total = extract_feb_averages(lst)
           full_shadow_feb_totals = update_totals(full_shadow_feb_total, full_shadow_feb_totals)
    feb_northeast =  "finish later"   
