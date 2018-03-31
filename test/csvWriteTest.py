import csv    
f = open('output.csv', 'w', newline='')
wr = csv.writer(f)
r=[[0 for c in  range(20)]for d in range(20)]
print(r)
for i in range(20):
    wr.writerow([r[i][0],r[i][1],r[i][2],r[i][3],r[i][4],r[i][5],
                 r[i][6],r[i][7],r[i][8],r[i][9],r[i][10],r[i][11],
                 r[i][12],r[i][13],r[i][14],r[i][15],r[i][16],
                 r[i][17],r[i][18],r[i][19]])
f.close()
