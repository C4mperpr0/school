from optparse import OptionParser

if __name__=="__main__":
    parser = OptionParser()
    parser.add_option("-r", dest="rule", help="Rule number 0..255.")
    parser.add_option("-f", dest="file_path", help="File path")
    (option, args) = parser.parse_args()
    rule = option.rule
    file_path = option.file_path

    w = 1000
    r = s = [0] * w
    r[int(w/2)] = 1
    z = []
    d = 0
    for j in range(0, int(w/2)):
        n = (r[0] << 1) + r[1]
        o = ""
        for i in range(1, w):
            o += " 0 " if r[i]==1 else "15 "
        z.append(o + "\n")
        for i in range(2,w):
            n = (n << 1) + r[i]
            if n >= 8: n-=8
            s[i-1] = (int(rule) >> n)%2
        r = s
        d += 1

    f = open(file_path,'w')
    f.write("P2\n")
    f.write(str(w-1) + " " + str(d) + "\n")
    f.write("15\n")
    for i in range(len(z)-1, 0, -1):
        f.write(z[i])
    f.close()





















