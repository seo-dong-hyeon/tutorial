import konlpy
from konlpy.tag import Okt
import csv

#print('morp : sample_twitter_data_{}_to_{}.csv'.format(my_crawler.days_range[0], my_crawler.days_range[-1]))
#df_tweet = pd.read_csv('sample_twitter_data_{}_to_{}.csv'.format(my_crawler.days_range[0], my_crawler.days_range[-1]))
#df_tweet = pd.read_csv('sample_twitter_data_2019-04-20_to_2019-04-20.csv')

f = open('sample_twitter_data_2019-04-20_to_2019-04-20.csv','r',encoding='UTF8')
rdr = csv.reader(f)

x_data = [[0]*60 ]*60

for i, document in enumerate(rdr):
    print("index:{}, document:{}".format(i,document[3]))
    okt = Okt()
    for word in okt.pos(document[3]):
        #if word[1] in ['Noun', 'Verb', 'Adjective']:  # 명사, 동사, 형용사
        if word[1] in ['Verb']:  # 명사, 동사, 형용사
            print("동사:{}".format(word[0]))
        if word[1] in ['Noun']:  # 명사, 동사, 형용사
            print("명사:{}".format(word[0]))
        if word[1] in ['Adjective']:  # 명사, 동사, 형용사
            print("형용사:{}".format(word[0]))
f.close



#텍스트 정제 (형태소 추출)
for i, document in enumerate(rdr):
    print("read:{}" .format(document))
    okt = konlpy.tag.Okt()
    clean_words = []
    for word in okt.pos(document, stem=True): #어간 추출
        if word[1] in ['Noun', 'Verb', 'Adjective']: #명사, 동사, 형용사
            clean_words.append(word[0])
        print(clean_words) #['스토리', '진짜', '노잼']
        document = ' '.join(clean_words)
        #print("clean:{}".format(document)) #스토리 진짜 노잼
        x_data[i] = document
#print(df_tweet) #['스토리 진짜 노잼' '똥 말' '쓰레기 영화 시간' '점도 쓰레기 영화' '이 기분' '이건 명작 임' '느낌 영화' '영화' '로코 대사 아주' '후회 감동']


