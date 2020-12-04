def write_2D_to_file(w):
    f = open('data_parameter.csv', 'w')
    f.write("w")
    f.write('\n')
    for cate in w:
        s = ''
        for i in cate:
            s = s + str(i) + ' '
        f.write(s)
        f.write('\n')
    f.close()
