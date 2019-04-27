s="dvdf"
i = 0
sub_str = []
count = 0
count_list = [0]
if len(s) == 0:
    print(0)
else:
    while i < len(s):
        if s[i] in sub_str:
            count_list.append(count)
            for i in range(0,len(sub_str)):
                if sub_str[i]==s[i]:
                    new_start=i+1
            count = count-new_start+1
            sub_str = sub_str[new_start:]
            sub_str.append(s[i])
        else:
            sub_str.append(s[i])
            count = count + 1
        i = i + 1
    count_list.append(count)
    print(max(count_list))