import csv
from bs4 import BeautifulSoup

reader = csv.reader(open('senior_lsf.csv', 'r'), delimiter=",")
# 서울시 노인 여가복지시설 데이터 읽기
svg = open('Seoul_map.svg', 'r').read()
# SVG 맵 읽기

senior_count = {}
counts_only = []
min_value = 100; max_value = 0; past_header = False

for row in reader:
    if not past_header:
        past_header = True
        continue

    try:
        unique = row[0]
        count = float(row[1].strip())
        senior_count[unique] = count
        counts_only.append(count)
    except:
        pass

soup = BeautifulSoup(svg, "html.parser")
# 뷰티풀숲으로 로드하기
paths = soup.findAll('path')
# 구를 식별할 path 데이터 찾기
colors = ["#F1EEF6", "#D4B9DA", "#C994D7", "#DF65B0", "#DD1C77", "#980043"]
# 지도시각화에 사용할 색상 설정
path_style = 'font-size: 12px; fill-rule: nonzero; stroke: #FFFFFF; stroke-opacity: 1; stroke-width: 0.1; stroke-miterlimit: 4; stroke-dasharray: none; stroke-linecap: butt; marker-start: none; stroke-linejoin: bevel; fill:'
# 지도에 나타낼 스타일 설정

for p in paths:
    if p['id']:
        try:
            count = senior_count[p['id']]
        except:
            continue

        if count > 250:
            color_class = 5
        elif count > 200:
            color_class = 4
        elif count > 150:
            color_class = 3
        elif count > 100:
            color_class = 2
        elif count > 50:
            color_class = 1
        else:
            count_class = 0

        color = colors[color_class]
        p['style'] = path_style + color

print(soup.prettify())