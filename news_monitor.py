import streamlit as st
import pandas as pd
from newsapi import NewsApiClient
import datetime

newsapi = NewsApiClient(api_key=st.secrets['api_key'])

search_term = st.text_input('输入关键词', max_chars=15)
if search_term:
    data = newsapi.get_everything(q=search_term)
    df = pd.DataFrame(data['articles'])
    for col in df.select_dtypes(include='object'):
        df[col] = df[col].str.strip()
    df.drop_duplicates(subset='title', inplace=True)
    for news in data['articles'][:5]:
        st.write(f"来源：{news['source']['name']}")
        st.write(f"标题：{news['title']}")
        st.write(f"作者：{news['author']}")
        st.write(f"正文：{news['description']}")
        st.write(f"原文链接：{news['url']}")
        st.write('\n')