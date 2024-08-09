import locale
from datetime import datetime, timedelta
from pathlib  import Path

import streamlit      as st
import plotly.express as px

from API      import *
from Tools    import *
from gpt4all  import GPT4All
from config   import Config

from local_model import get_model

from langchain_core.prompts import (
    ChatPromptTemplate          ,
    HumanMessagePromptTemplate  ,
    MessagesPlaceholder         ,
)

#locale.setlocale(locale.LC_ALL, "tr_TR.utf8")

config = Config()

st.sidebar.markdown("# Heisen-Mech")  
st.sidebar.markdown("## Girdi değerleri") 

def graph_prediction():

    advice_prompt = config.graph_advice_prompt
    system_prompt = config.graph_system_prompt 
    st.write("graph")
    model = GPT4All(model_name="tinyllama-1.1b-chat-v1.0.Q2_K.gguf", model_path= './' ,allow_download=False, device='cpu')

    # Grafik analiz modeli için API ile binance üzerinden bilgi çekildiğinde ve bu bilgi hakkında soru soruldğunda:
    #if graph_button_flag:
    
    # Dataframe üzerinden bilgiler derlenir ve değişkene atanır.
    kripto_degerleri = generate_detailed_summary(data_frame, interval=interval[1].upper())

    system_prompt = '### System:\n VSen finansal alanda yardımbı bir dil modelisin. Sorulara yardımcı ol\n\n'
    prompt_template = '### Kullanıcı:\n{0}\n\n### Cevap:\n'

    
    tokens = []
    with model.chat_session(system_prompt=graph_advice_prompt,prompt_template=prompt_template):
        for token in model.generate(f"{advice_prompt}{kripto_degerleri}{user_query}+'Türkçe olarak cevapla'", streaming=True, max_tokens=920):
            yield token 
            
    tokens = []
       
   

def RAG_prediction():
    graph_prompt  = """Sana verilen portföy veya bilgileri finansal başlık altında kullanıcıya açıkla ve yardımcı ol."""
    
    model = GPT4All(model_name="tinyllama-1.1b-chat-v1.0.Q2_K.gguf", model_path= './' ,allow_download=False, device='cpu')
                    
    tokens = []
    with model.chat_session(system_prompt = graph_prompt):
        for token in model.generate(rag_text + user_query, streaming=True, max_tokens=320):
            yield token 

DEFAULT_SYMBOL = 'BTCUSDT'
DEFAULT_INTERVAL = Client.KLINE_INTERVAL_1DAY


today = datetime.today()
default_start_date = today - timedelta(days=30)
default_end_date = today

start_date = st.sidebar.date_input("Başlangıç Tarihi", value=default_start_date)
end_date = st.sidebar.date_input("Bitiş Tarihi", value=default_end_date)

start_time = start_date.strftime('%Y-%m-%d')
end_time = end_date.strftime('%Y-%m-%d')

crypto_pairs = [
    'BTCUSDT',
    'ETHUSDT',
    'BNBUSDT',
    'XRPUSDT',
    'LTCUSDT'
]

interval_options = {
    "Günlük":   Client.KLINE_INTERVAL_1DAY,
    "Haftalık": Client.KLINE_INTERVAL_1WEEK,
    "Aylık":    Client.KLINE_INTERVAL_1MONTH
}


selected_interval = st.sidebar.selectbox("Bir aralık seçin:", options=list(interval_options.keys()))
interval = interval_options[selected_interval]

selected_pair = st.sidebar.selectbox('Kripto birim seçin:', crypto_pairs)

# Query button in the sidebar
graph_button = st.sidebar.button("Grafik İncele")
query_button = st.sidebar.button("Sorgula")


with st.sidebar:
    st.subheader("")
    st.subheader("Belgeleriniz:")
    pdf_docs = st.file_uploader(
        "Belgelerinizi yükleyip 'Yükle' tuşuna basın", accept_multiple_files=True)

    RAG_button = st.sidebar.button("Belgeyi sorgula")

    
graph_button_flag = 0

# Ana başlık
st.title("Kriptovarlık Analiz Panosu")

user_query = st.text_area("Modele Yorumlat", height=200)

klines = client.get_historical_klines(selected_pair, interval, start_str=start_time, end_str=end_time)
data_frame = get_df(klines)

if graph_button:
    graph_button_flag = 1
    # Fetch historical data
    klines = client.get_historical_klines(selected_pair, interval, start_str=start_time, end_str=end_time)
    data_frame = get_df(klines)

    # Display plots in a container to adjust positioning
    with st.container():
        fig = display_plot(data_frame, interval, selected_pair, use_streamlit=True)
        st.plotly_chart(fig, use_container_width=True)

    with st.container():
        fig2 = display_closing_prices(data_frame, interval, selected_pair, use_streamlit=True)
        st.plotly_chart(fig2, use_container_width=True)

if query_button and len(user_query) > 0:
    st.write_stream(graph_prediction)


if RAG_button:# and len(user_query):
    rag_text = extract_singlepage_from_pdf_writer(pdf_docs[0],0)
    st.write_stream(RAG_prediction)
    