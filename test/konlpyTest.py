from konlpy.tag import Kkma, Hannanum
from konlpy.utils import pprint
import tensorflow as tf
import numpy as np
import csv
tf.set_random_seed(777)

hannanum = Hannanum()

kkma = Kkma()
xy = np.loadtxt('sample.csv', delimiter=',', dtype=np.str)
x_data = xy[:,0:1]
y_data = xy[:,1:2]
x = []
y = []
p = []
#print(x_data)
#print(y_data)
#print(x_data[0][0])
#x = kkma.morphs(x_data[0][0])
#sen = ["네 안녕하세요 반갑습니다"]
#print(sen[0])
#print(kkma.morphs(sen[0]))
for i in range(len(x_data)):
    for j in range(len(x_data[i])):
        k=kkma.morphs(x_data[i][j])
        x.insert(i,k)
for i in range(len(y_data)):
    for j in range(len(y_data[i])):
        k=[int(y_data[i][j])]
        y.insert(i,k)
print(x)
print(y)

x_one_hot = []
a=0
x_one_hot = [[0 for a in  range(len(x[a]))]for b in range(len(x[a]))]
print(x[0])
print(x_one_hot)
for i in range(len(x[a])):
    x_one_hot[i][i] = 1

f = open('output.csv', 'w', newline='')
wr = csv.writer(f)
r=[[0 for c in  range(20)]for d in range(20)]
for i in range(20):
    wr.writerow([r[i][0],r[i][1],r[i][2],r[i][3],r[i][4],r[i][5],
                 r[i][6],r[i][7],r[i][8],r[i][9],r[i][10],r[i][11],
                 r[i][12],r[i][13],r[i][14],r[i][15],r[i][16],
                 r[i][17],r[i][18],r[i][19]])
f.close()

#print(x_one_hot)

#pprint(kkma.sentences(u'네, 안녕하세요. 반갑습니다.'))
#pprint(kkma.nouns(u'질문이나 건의사항은 깃헙 이슈 트래커에 남겨주세요.'))
#pprint(kkma.pos(u'오류보고는 실행환경, 에러메세지와함께 설명을 최대한상세히!^^'))

#print(kkma.morphs
#       ('진짜 내 인생 영화다 지금까지 20번 봤다 장면 하나하나가 아름답고 섬세하다. 아주 훌륭한 영화 '))
#print()
#print(kkma.morphs
#       ('완전 좋아요. 최고의영화'))
#print()
#print(kkma.morphs
#       ('정말 흥미진진 사랑스러운 영화 '))

