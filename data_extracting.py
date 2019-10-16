

def delete_day_name(temp_string):
    # Checking if first element in list is a day name

    days =['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    for i in temp_string:
        if i in days:
            temp_string = temp_string[1:]
            return temp_string
        else:
            return temp_string

def check_first_elem_in_list(splited_list, date):
    # Checking if given date is first element in given data list
    if check_if_elem_is_date(splited_list[0]):
        return splited_list
    else:
        splited_list.insert(0, date)
        return splited_list

def check_if_elem_is_date(elem):
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

def extract_data(data):
    # changing to string
    joined_list = ' '.join(data)
    # spliting by spaces
    splited_list = joined_list.split(" ")
    # cleaning empty lists
    splited_list = [x for x in splited_list if x]
    # removing first element in list
    splited_list = splited_list[1:]
    date = splited_list[1]
    extracted_data_list = []
    while len(splited_list) > 8:
        headers = ['date','time_stamp','windspeed','gaust','wind_direction','wave','wavepeak','wavedirection','periods']
        splited_list = delete_day_name(splited_list)
        if check_first_elem_in_list(splited_list,date):
            date = splited_list[0]
        else:
            date = date
        splited_list = check_first_elem_in_list(splited_list,date)
        temp_data = splited_list[:9]
        one_record = dict(zip(headers,temp_data))
        extracted_data_list.append(one_record)
        splited_list = splited_list[9:]
        
    return extracted_data_list

  

