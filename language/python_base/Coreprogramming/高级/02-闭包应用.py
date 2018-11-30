def line_conf(a,b):
    def line(x):
        return a*x +b
    return line
line1 = line_conf(1,2)
line2 = line_conf(3,4)
print(line1(5))
print(line2(2))
