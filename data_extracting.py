
def deleteDayName(temp_string):
    # Checking if first element in list is a day name

    days =['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    for i in temp_string:
        if i in days:
            temp_string = temp_string[1:]
            return temp_string
        else:
            return temp_string

def checkFirstElemInList(splited_list, date):
    # Checking if given date is first element in given data list
    if checkIfElemIsDate(splited_list[0]):
        return splited_list
    else:
        splited_list.insert(0, date)
        return splited_list

def checkIfElemIsDate(elem):
    # Checking if given element is a date element in format 'nn/nn' where n is number
    trigger = 0
    # checking if elem contain '/' sign
    for i in elem:
        if i in ['/']:
            trigger +=1
        else:
            continue
    if trigger > 0:
        return True

def extractData(data):
    # function which extracting data to list of dictionaries collected from website
    # changing to string
    joined_list = ' '.join(data)
    # spliting by spaces on lists
    splited_list = joined_list.split(" ")
    # because some element had two spaces we have to remove lists contains just spaces
    splited_list = [x for x in splited_list if x]
    # removing first element in list
    splited_list = splited_list[1:]
    date = splited_list[1]
    extracted_data_list = []
    while len(splited_list) > 8:
        headers = ['Dates','Dayquaters','Windspeed','Gust','Winddirection','Wave','Wavepeak','Wavedirection','Periods']
        splited_list = deleteDayName(splited_list)
        if checkFirstElemInList(splited_list, date):
            date = splited_list[0]
        else:
            date = date
        splited_list = checkFirstElemInList(splited_list,date)
        temp_data = splited_list[:9]
        one_record = dict(zip(headers,temp_data))
        extracted_data_list.append(one_record)
        splited_list = splited_list[9:]
        
    return extracted_data_list

  
