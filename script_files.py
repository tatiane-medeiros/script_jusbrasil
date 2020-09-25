#limpa os dados para busca


file = open('processos.txt', 'r')
#file.read()
nfile = open('novo.txt', 'w')
for row in file:
    a = row[:-1]
    try:
        int(a[-1:])
    except:
        a = a[:-1]
        
    print(a)
    nfile.write(a)
    nfile.write("\n")

file.close()
nfile.close()

