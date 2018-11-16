def print_log(data, id):
    assert isinstance(id, int), \
        "please set id as an integer number"
    assert data and id >= 0 , \
        "please input valid data and id."
    
    true_log_len = 7
    log_content = data.splitlines()
    total_row = len(log_content)
    if id >= total_row:
        print("Cannot find "+str(id))
    elif id == 0:
        print(log_content[0])
    else:
        for i in range(1,id+1):
            data_row = log_content[i].split()
            if len(data_row) != true_log_len:
                print("Error: "+str(id))
                break
            elif i == id:
                print(data_row[0]+' '+ str(id) + cal_position(data_row[1:]))

def cal_position(signal):
    pos_str = ''
    half = len(signal)//2
    for i in range(0,half):
        pos_str = pos_str + ' ' + str(int(signal[i]) + int(signal[i+half]))
    return pos_str

    

if __name__ == '__main__':
    data = """plane1 1 1 1
plane1 1 1 1 1 2 3
plane1 2 3 4 1 1 1
plane1 3 4 5
plane1 1 1 1 1 2 3"""
    id = 2
    print_log(data, id)
    id = 4
    print_log(data, id)
    id = 100
    print_log(data, id)


