#import collection.my_crawler as my_crawler
from WebCrawling import Test_Code_Twitter
from Model1 import MyAnalyzer
from Model1 import MyMorpheme
from Model1 import MySentiment


if __name__ == '__main__':
    #비교대상 크롤링
    #twitter_crawler = Test_Code_Twitter.TwitterCrawler()
    #twitter_crawler.make_condition()
    #witter_crawler.collect_data()
    print("크롤링 끝")

    #학습
    read_file = 'ratings_test.txt'
    json_file = 'train_docs.json'
    model_name = 'tmp_model.h5'

    morpheme = MyMorpheme.Morpheme()
    train_data = morpheme.read_data(read_file)
    morpheme.write_data(json_file, train_data)
    print("형태소 분리 끝")

    model = MySentiment.Sentiment()
    model.open_file(json_file)
    model.make_model(model_name)

    analyzer = MyAnalyzer.Analyzer(json_file, model_name)
    analyzer.predict_pos_neg(analyzer, "올해 최고의 영화! 세 번 넘게 봐도 질리지가 않네요.")
    analyzer.predict_pos_neg(analyzer, "배경 음악이 영화의 분위기랑 너무 안 맞았습니다. 몰입에 방해가 됩니다.")
    analyzer.predict_pos_neg(analyzer, "주연 배우가 신인인데 연기를 진짜 잘 하네요. 몰입감 ㅎㄷㄷ")
    analyzer.predict_pos_neg(analyzer, "믿고 보는 감독이지만 이번에는 아니네요")
    analyzer.predict_pos_neg(analyzer, "주연배우 때문에 봤어요")



