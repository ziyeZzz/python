def generate(numRows):
    last_row = []
    this_row = []
    if numRows>0:
        last_row = [1]
        for i in range(2,numRows+1):
            last_row = [0] + last_row + [0]
            for num in range(1,i+1):
                this_row.append(last_row[num-1]+last_row[num])
            last_row = this_row
            this_row = []
    print(last_row)

if __name__=='__main__':
    generate(5)