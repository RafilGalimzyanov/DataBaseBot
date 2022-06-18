import requests
from bs4 import BeautifulSoup

'''
    Парсинг курса доллара с оф. сайта ЦБ РФ

'''


def dollar():
    url = 'https://cbr.ru/'

    source = requests.get(url)
    main_text = source.text
    soup = BeautifulSoup(main_text, "html.parser")

    course = soup.find('div', {'class': 'col-md-2 col-xs-9 _right mono-num'})
    course = course.text

    return float(course[:7].replace(',', '.'))