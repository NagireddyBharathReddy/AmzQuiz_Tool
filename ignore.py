from datetime import datetime

import requests as r
from bs4 import BeautifulSoup


class AmazonAnswers:
    def __init__(self):
        self.now = datetime.now()
        self.answers = []
        self.url1 = 'https://tophunt.in/amazon-quiz-{}-{}-{}/'.format(self.now.strftime('%d'),
                                                                      self.now.strftime('%B').lower(),
                                                                      self.now.strftime('%Y'))
        self.url2 = 'https://www.gktoday.in/amazon-quiz-answers-{}-{}-{}/'.format(self.now.strftime('%d'),
                                                                                  self.now.strftime('%B').lower(),
                                                                                  self.now.strftime('%Y'))
        self.url3 = 'https://tophunt.in/amazon-rewind-2020-quiz-answers/'
        self.url4 = 'https://tophunt.in/amazon-pay-later-quiz-answers-20000/'

        self.ans = [f'Answer {i}' for i in range(10)]

    def get_data(self, url, tagname):
        a = r.get(url)
        soup = BeautifulSoup(a.text, 'html.parser')
        b2 = soup.find_all(tagname)
        return b2

    def source2(self):
        for i in self.get_data(self.url1, 'strong'):
            for j in self.ans:
                if j in i.text:
                    self.answers.append(i.text.split(':')[1].strip())
        return self.answers

    def source1(self):
        for i in self.get_data(self.url2, 'strong'):
            self.answers.append(i.text.strip())
        return self.answers


a = AmazonAnswers().source2()
# a1 = AmazonAnswers().source2()
#print(a)


def convert_cookies():
    try:
        with open('cookies.txt', 'r', encoding='utf-8') as f:
            data = f.readlines()
        raw_cookie = data[0]
        #print(raw_cookie)
        cookie_dict = {}
        raw_cookie = raw_cookie.split(';')
        for i in raw_cookie:
            i = i.split('=')
            cookie_dict[i[0]] = i[1]
        print(cookie_dict)
        return cookie_dict
    except:
        pass
    return None


def save_cookies(cookies):
    cookies_v2 = ''
    for i in cookies:
        cookies_v2 = cookies_v2 + i['name']+'='+i['value']+';'
    with open('cookies.txt', 'w+', encoding='utf-8') as f:
        f.write(cookies_v2)


def read_userData():
    with open('userDetails.txt', 'r', encoding='utf-8') as f:
        data = f.readlines()
    return data


def save_userData(data):
    with open('userDetails.txt', 'w+', encoding='utf-8') as f:
        f.write(data[0])
        f.write('\n')
        f.write(data[1])
