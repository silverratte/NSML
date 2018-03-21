from konlpy.tag import Kkma, Hannanum

from konlpy.utils import pprint

hannanum = Hannanum()

kkma = Kkma()



#pprint(kkma.sentences(u'네, 안녕하세요. 반갑습니다.'))
#pprint(kkma.nouns(u'질문이나 건의사항은 깃헙 이슈 트래커에 남겨주세요.'))
#pprint(kkma.pos(u'오류보고는 실행환경, 에러메세지와함께 설명을 최대한상세히!^^'))


print(kkma.morphs
       ('진짜 내 인생 영화다 지금까지 20번 봤다 장면 하나하나가 아름답고 섬세하다. 아주 훌륭한 영화 '))
print()
print(kkma.morphs
       ('완전 좋아요. 최고의영화'))
print()
print(kkma.morphs
       ('정말 흥미진진 사랑스러운 영화 '))

#이걸로!

