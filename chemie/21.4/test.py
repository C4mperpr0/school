
def listToStr(data, header=None): # 2D only
    x = data.copy()
    if header != None:
        x.insert(0, header)
    datalen = 0
    for line in x:
        for data in line:
            if len(str(data)) > datalen:
                datalen = len(str(data))
    str_list = []
    for line in x:
        line_str = ''
        for data in line:
            fullspacing = datalen - len(str(data))
            if (fullspacing%2) == 1:
                spacing = [round((fullspacing/2)-0.5), round((fullspacing/2)+0.5)]
            else:
                spacing = [round(fullspacing/2), round(fullspacing/2)]
            line_str = line_str + '| ' + (' '*spacing[0]) + str(data) + (' '*spacing[1]) + ' '
        line_str = line_str + '|'
        str_list.append(line_str)
    if header != None:
        line_str = ''
        for i in header:
            line_str = line_str + '|' + ('-'*(datalen+2))
        line_str = line_str + '|'
        str_list.insert(1, line_str)
    final_str = '' 
    for line in str_list:
        final_str = final_str + line + '\n'
    return final_str

def versuch(start_a, start_b, speed):
    datalist = []
    header = ["Nummer des Spielzugs", "Zahl der Kugeln N-A", "Zahl der Kugeln N-B"]
    def step(a, b, speed):
        add_a = round(b * speed)
        add_b = round(a * speed)
        new_a = a - add_b + add_a
        new_b = b - add_a + add_b
        return {"a":new_a, "b":new_b}
    a = start_a
    b = start_b
    datalist.append([len(datalist), a, b])
    while (len(datalist) < 3) or not (datalist[-1][1:] == datalist[-2][1:] == datalist[-3][1:]):
        data = step(a, b, speed)
        a, b = data["a"], data["b"]
        datalist.append([len(datalist), a, b])
    with open("versuch.txt", "w+") as file:
        file.write(listToStr(datalist, header))

versuch(501, 334, 0.5)
            




















