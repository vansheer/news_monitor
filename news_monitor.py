import streamlit as st
import pandas as pd
from newsapi import NewsApiClient
import datetime

newsapi = NewsApiClient(api_key=st.secrets['api_key'])

search_term = st.text_input('输入关键词', max_chars=50)
if search_term:
    data = newsapi.get_everything(q=search_term, language='en')
    df = pd.DataFrame(data['articles'])
    for col in df.select_dtypes(include='object'):
        df[col] = df[col].str.strip()
    df.drop_duplicates(subset='title', inplace=True)
    df['publishedAt'] = df['publishedAt'].str.split('T').str[0]
    df['publishedAt'] = pd.to_datetime(df['publishedAt'])
    df.sort_values(by='publishedAt', ascending=False, inplace=True)
    for news in df.to_dict(orient='records'):
        st.write(f"原文链接：{news['url']}")
        st.write(f"来源：{news['source']['name']}")
        st.write(f"标题：{news['title']}")
        st.write(f"作者：{news['author']}")
        st.write(f"发布日期：{news['publishedAt']}")
        st.write(f"正文：{news['description']}")
        st.write('\n')