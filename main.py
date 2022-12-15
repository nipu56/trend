"""
라이브러리
데이터 프레임 : pandas
구글 트렌드 api : pytrends https://pypi.org/project/pytrends/#credits
데이터 그래프 : plotly
"""
from pytrends.request import TrendReq
import pandas as pd
import matplotlib
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

# 카테고리 목록 https://github.com/pat310/google-trends-api/wiki/Google-Trends-Categories

# plot 설정
fm.get_fontconfig_fonts()
font_location = 'C:/Windows/Fonts/GULIM.TTC' # For Windows
font_name = fm.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

# 검색량 비교
trends = TrendReq(hl="en-US", tz=360)  # 한국, 시간대 오프셋
kw_list = ["apple", "samsung"]  # 키워드 지정
trends.build_payload(kw_list, cat=0, timeframe="2022-01-01 2022-11-01", geo="")  # 카테고리, 시간대, 국가
data = trends.interest_over_time()
print(data.head(20))
if all(data.isPartial == False):
    del data['isPartial']


# 데이터 그래프 화
def plot_searchterms(df):
    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_subplot(111)
    df.plot(ax=ax)
    plt.xlabel("date")
    plt.ylabel("searchterms")
    plt.ylim(0, 120)
    plt.legend(loc='lower left')
    return ax


plt.style.use('ggplot')
ax = plot_searchterms(data)
plt.show()

# 실시간 급상승 검색어 - 한국
trend = trends.trending_searches(pn='south_korea')  # 일별 인기 급상승 검색어
# trend2 = trends.realtime_trending_searches(pn='IN') # 실시간 인기 급상승 검색어(한국 지원 x)
print(trend.head(2).values)