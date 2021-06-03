class export_xlsx:
    def export_class101(df):
        from review_preprocessing import string_preprocessing
        from review_preprocessing import sentiment_preprocessing
        from tqdm import tqdm

        print('C사이트 데이터 변환 중')
        tqdm.pandas()
        df = df[df['review'] != 'none']

        df['title'] = df.progress_apply(lambda x: string_preprocessing.cleanName(x['title']), axis=1)
        print('강좌명 대괄호 제거 완료')
        df['title'] = df.progress_apply(lambda x: string_preprocessing.cleansingEmoticon(x['title']), axis=1)
        print('강좌명 정규표현식 적용 완료')

        df['review'] = df.progress_apply(lambda x: string_preprocessing.cleansingEmoticon(str(x['review'])), axis=1)
        print('리뷰 정규표현식 적용 완료')
        df['review'] = df.progress_apply(lambda x: string_preprocessing.stemming(str(x['review'])), axis=1)
        print('리뷰 형태소 변환 완료')

        df['review_year'] = df['review_date'].progress_map(string_preprocessing.return_year_c)
        print('연도 추출 완료')
        df['review_month'] = df['review_date'].progress_map(string_preprocessing.return_month_c)
        print('월 추출 완료')

        df['sentiment'] = df.review.progress_map(sentiment_preprocessing.return_sentiment)
        print('감정분석 적용 완료')
        df = df.loc[(df['sentiment'] != 'not enough data') & (df['review'] != '좋다') & (df['review'] != '아쉽다')]

        df = sentiment_preprocessing.return_review_cat(df)
        print('리뷰 기반 긍부정 카테고리 적용 완료')
        df = df.loc[df.sentiment_cat.notnull()]
        df.to_csv('./dataset/preprocessed_dataset_Csite.csv', encoding='utf-8-sig')
        print('C사이트 데이터 변환 완료')
        return df

    def export_idus(df):
        from review_preprocessing import string_preprocessing
        from review_preprocessing import sentiment_preprocessing
        from tqdm import tqdm

        print('I사이트 데이터 변환 중')
        tqdm.pandas()
        df = df[df['review'] != 'none']

        df['title'] = df.progress_apply(lambda x: string_preprocessing.cleansingEmoticon(x['title']), axis=1)
        print('강좌명 정규표현식 적용 완료')

        df['review'] = df.progress_apply(lambda x: string_preprocessing.cleansingEmoticon(str(x['review'])), axis=1)
        print('리뷰 정규표현식 적용 완료')
        df['review'] = df.progress_apply(lambda x: string_preprocessing.stemming(str(x['review'])), axis=1)
        print('리뷰 형태소 변환 완료')

        df['review_year'] = df['datetime'].progress_map(string_preprocessing.return_year_i)
        print('연도 추출 완료')
        df['review_month'] = df['datetime'].progress_map(string_preprocessing.return_month_i)
        print('월 추출 완료')

        df['sentiment'] = df.review.progress_map(sentiment_preprocessing.return_sentiment)
        print('감정분석 적용 완료')
        df = df.loc[(df['sentiment'] != 'not enough data') & (df['review'] != '좋다') & (df['review'] != '아쉽다')]

        df = sentiment_preprocessing.return_review_cat(df)
        print('리뷰 기반 긍부정 카테고리 적용 완료')
        df = df.loc[df.sentiment_cat.notnull()]
        df.to_csv('./dataset/preprocessed_dataset_Isite.csv', encoding='utf-8-sig')
        print('I사이트 데이터 변환 완료')
        return df