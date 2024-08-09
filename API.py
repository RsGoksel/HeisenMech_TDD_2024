import pandas as pd

import matplotlib.dates     as mdates
import plotly.graph_objects as go
import matplotlib.pyplot    as plt

import locale
locale.setlocale(locale.LC_ALL, "tr_TR.utf8")

API_KEY    = 'N8...4' # Binance api key
API_SECRET = 'uj...B'

from binance.client import Client
client = Client(API_KEY, API_SECRET)

def fetch_market_data(symbol: str):
    # Finansal değerin bilgilerinin getirilmesi
    # İlgili fonksiyonun Dokümanı: https://binance-docs.github.io/apidocs/spot/en/#symbol-price-ticker
    
    """
        # en populer x değer elde edilir
        sorted_tickers = sorted(tickers, key=lambda x: float(x['quoteVolume']), reverse=True)
        x = 10
        top_x_symbols = [ticker['symbol'] for ticker in sorted_tickers[:x]]
    
        print("En popüler x değer:")
        for symbol in top_x_symbols:
            print(symbol)
    
    """
    tickers = client.get_ticker()

    """İlgili değerin piyasasını döndürür"""
    ticker = client.get_symbol_ticker(symbol=symbol)
    return ticker

def get_df(klines: list):
    # Candle Lines formatını veri çerçevesine dönüştürür 
    
    df = pd.DataFrame(klines, columns=[
        'Open Time', 'Open', 'High', 'Low', 'Close', 'Volume',
        'Close Time', 'Quote Asset Volume', 'Number of Trades',
        'Taker Buy Base Asset Volume', 'Taker Buy Quote Asset Volume',
        'Ignore'
    ])
    
    df['Open Time']  = pd.to_datetime(df['Open Time'] , unit='ms')
    df['Close Time'] = pd.to_datetime(df['Close Time'], unit='ms')
    
    df.set_index('Open Time', inplace=True)
    
    df[['Open', 'High', 'Low', 'Close', 'Volume']] = df[['Open', 'High', 'Low', 'Close', 'Volume']].astype(float)

    return df
    
def display_plot(data_frame: pd.DataFrame, interval: str, symbol: str, use_streamlit: bool = True):
    #Bar ve grafik plot'larını döndürür
    
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=data_frame.index, y=data_frame['Close'], mode='lines', name='Kapanış Fiyatı'))

    fig.update_layout(
        #title=f'{interval} {symbol} Kapanış Fiyatı',
        yaxis_title      = 'Değer (fiyat) (USDT)',
        xaxis_title      = 'Tarih',
        xaxis_tickformat = '%d %B %Y',
        
        legend = dict(x=0, y=1),
        margin = dict(l=40, r=40, t=40, b=40),
        bargap = 0.5  # Barlar arası boşluk 
    )

    # Yüzdelik dilim değişim hesabı
    latest_price   = data_frame['Close'].iloc[-1]
    previous_price = data_frame['Close'].iloc[-2]
    percent_change = ((latest_price - previous_price) / previous_price) * 100
    price_info     = f'{symbol}\n{latest_price:.3f} ({percent_change:.2f}%)'

    fig.add_annotation(
        x = data_frame.index[-1],
        y = latest_price,
        
        text      = price_info,
        showarrow = True,
        arrowhead = 1
    )

    colors = ['green' if row['Open'] < row['Close'] else 'red' for index, row in data_frame.iterrows()]
    fig.add_trace(go.Bar(x=data_frame.index, y=data_frame['Volume'], marker_color=colors, name='Hacim', opacity=0.7))

    return fig if use_streamlit else fig.show()


def display_closing_prices(data_frame: pd.DataFrame, interval: str, symbol: str, use_streamlit: bool = False) -> None:
    # Grafik plot'unu döndürür
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x = data_frame.index,
        y = data_frame['Close'],
        
        mode = 'lines',
        name = 'Close Price',
        line = dict(color='blue')
    ))
    
    fig.update_layout(
        #title=f'{interval} {symbol} Kapanış Fiyatı',
        xaxis_title = 'Tarih',
        yaxis_title = 'Değer(fiyat) (USDT)',
        
        xaxis=dict(
            tickformat='%Y-%m-%d' if interval in [Client.KLINE_INTERVAL_1HOUR, Client.KLINE_INTERVAL_1DAY] else '%Y-%m',
            tickangle=-45
        ),
        yaxis  = dict(title='Değer(fiyat) (USDT)'),
        legend = dict(x=0.01, y=0.99),
        margin = dict(l=40, r=10, t=40, b=40),
    )
    
    latest_price   = data_frame['Close'].iloc[-1]
    previous_price = data_frame['Close'].iloc[-2]
    percent_change = ((latest_price - previous_price) / previous_price) * 100
    price_info     = f'{symbol}\n{latest_price:.3f} ({percent_change:.2f}%)'
    
    fig.add_annotation(
        x = data_frame.index[-1],
        y = latest_price,
        
        text      = price_info,
        showarrow = True,
        arrowhead = 2,
        ax = 0,
        ay = -40,
        bgcolor = 'white',
        opacity = 0.8
    )
    return fig if use_streamlit else fig.show()
    
def generate_detailed_summary(df: pd.DataFrame, interval='M'):
    summary = []

    # Verileri belirtilen aralığa göre yeniden örnekler (aylar için M, haftalar için W, günler için D)
    df_resampled = df.resample(interval).agg({
        'Open'  : 'first',
        'High'  : 'max',
        'Low'   : 'min',
        'Close' : 'last',
        'Volume': 'sum',
        'Number of Trades': 'sum'
    })

    # Örneklemler üzerinde bilgiyi formatlama 
    for period, data in df_resampled.iterrows():
        if interval == 'M':
            period_summary = f"\n {period.strftime('%B %Y')} Özeti:"
        elif interval == 'W':
            period_summary = f"\n Hafta {period.strftime('%U, %Y')} Özeti:"
        else:  # interval == 'D'
            period_summary = f"\n {period.strftime('%d %B %Y')} Özeti:"
        
        period_summary += f"\n- Açılış Fiyatı:    {data['Open']  : .2f}  USDT"
        period_summary += f"\n- En Yüksek Fiyat:  {data['High']  : .2f}  USDT"
        period_summary += f"\n- En Düşük Fiyat:   {data['Low']   : .2f}  USDT"
        period_summary += f"\n- Kapanış Fiyatı:   {data['Close'] : .2f}  USDT"
        
        period_summary += f"\n- Toplam Hacim:     {data['Volume']: .2f} units"
        period_summary += f"\n- İşlem Sayısı:     {data['Number of Trades']} trades"
        
        # verilen periyodun trend'ini belirleme
        if data['Close'] > data['Open']:
            period_summary += "\n- Market Trendi: Yukarı Yönlü"
        else:
            period_summary += "\n- Market Trendi: Aşağı Yönlü"
        
        summary.append(period_summary)

    return ' \n '.join(map(lambda text: ' '.join(text.replace('\n', ' ').strip().split()), summary))

    
"""
Kullanılabilir Interval Değerleri 
KLINE_INTERVAL_1MINUTE = '1m'
KLINE_INTERVAL_3MINUTE = '3m'
KLINE_INTERVAL_5MINUTE = '5m'
KLINE_INTERVAL_15MINUTE = '15m'
KLINE_INTERVAL_30MINUTE = '30m'
KLINE_INTERVAL_1HOUR = '1h'
KLINE_INTERVAL_2HOUR = '2h'
KLINE_INTERVAL_4HOUR = '4h'
KLINE_INTERVAL_6HOUR = '6h'
KLINE_INTERVAL_8HOUR = '8h'
KLINE_INTERVAL_12HOUR = '12h'
KLINE_INTERVAL_1DAY = '1d'
KLINE_INTERVAL_3DAY = '3d'
KLINE_INTERVAL_1WEEK = '1w'
KLINE_INTERVAL_1MONTH = '1M'
"""
