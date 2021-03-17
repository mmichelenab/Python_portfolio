import csv

total_nw = 0
money_nw = 0
total_ne = 0
money_ne = 0
total_southwest = 0
money_southwest = 0
total_southeast = 0
money_southeast = 0
average_nw = 0
average_ne = 0
average_southeast = 0
average_southwest = 0
total_cost = 0
total_average = 0
total_people = 0



with open('insurance.csv') as insurance_info:
    insu_info = csv.reader(insurance_info)
    for row in insu_info:
        if row[5] == 'northwest':
            total_nw += 1
            money_nw += float(row[6])
            average_nw = float("{:.2f}".format(money_nw/total_nw))
        elif row[5] == 'northeast':
            total_ne += 1
            money_ne += float(row[6])
            average_ne = float("{:.2f}".format(money_ne/total_ne))
        elif row[5] == 'southwest':
            total_southwest += 1
            money_southwest += float(row[6])
            average_southwest = float("{:.2f}".format(money_southwest/total_southwest))
        elif row[5] == 'southeast':
            total_southeast += 1
            money_southeast += float(row[6])
            average_southeast = float("{:.2f}".format(money_southeast/total_southeast))
    total_cost = float("{:.2f}".format(money_nw + money_ne + money_southwest + money_southeast))
    total_people = total_nw + total_ne + total_southwest + total_southeast
    total_average = float("{:.2f}".format(total_cost/total_people))
        
    print('The average insurance cost for the Northeast area is ' + str(average_ne))
    print('The average insurance cost for the Northwest area is ' + str(average_nw))
    print('The average insurance cost for the Southeast area is ' + str(average_southeast))
    print('The average insurance cost for the Southwest area is ' + str(average_southwest))
    print('The average cost nation wide is ' + str(total_average))
    print('There seems to be a significant difference in cost between the east side and the west side of the country. The east side being above the national average, specially the Southeast area, whereas the west side is below in both north and south.')





