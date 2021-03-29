import jieba
import jieba.posseg as psg
from snownlp import SnowNLP

words1 = "速度快，包装好，看着特别好，喝着肯定不错！价廉物美"
words2 = jieba.cut(words1)
words3 = list(words2)
print("/".join(words3))

# 速度/快/，/包装/好/，/看着/特别/好/，/喝/着/肯定/不错/！/价廉物美

stop_words = ["，", "！"]
words4 = [x for x in words3 if x not in stop_words]
print(words4)

# ['速度', '快', '包装', '好', '看着', '特别', '好', '喝', '着', '肯定', '不错', '价廉物美']

words5 = [(w.word, w.flag) for w in psg.cut(words1)]
saved = ['a', ]
words5 = [x for x in words5 if x[1] in saved]
print(words5)

words6 = [x[0] for x in words5]
print(words3)
s1 = SnowNLP(" ".join(words6))
print(s1.sentiments)

positive = 0
negtive = 0
for word in words6:
    s2 = SnowNLP(word)
    if s2.sentiments > 0.7:
        positive += 1
    else:
        negtive += 1
    print(word, str(s2.sentiments))
print(f"正向评价数量:{positive}")
print(f"负向评价数量:{negtive}")
