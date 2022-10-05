from genericpath import isfile
import random
from requests.exceptions import ConnectionError
import time
from collections import namedtuple
from bs4 import BeautifulSoup
import requests
import socks
import ast
import os
from http.client import IncompleteRead
import json
import socket
import os

# result=requests.get('https://www.houzz.ru/professionals/query?l=%D1%81%D0%BE%D1%87%D0%B8&tid=14028')
# source = result.text
#  ###############################
# #  soup = BeautifulSoup(source, 'html.parser')
# # data = soup.find('script', type='application/ld+json')
# # # res = soup.find('script',type='application/ld+json')
# # print(data)
# ########################################
# absolute_path = os.path.abspath(__file__)

# def html_yaratish(res):
#         with open(f"{os.path.dirname(absolute_path)}\link-sochi\product1.html", 'w',
#                   encoding='utf-8') as file:
#             file.write(res)

# with open(f"{os.path.dirname(absolute_path)}\product1.html", encoding='utf-8') as file:
#                     source = file.read()
# soup = BeautifulSoup(source, 'html.parser')
# datas = soup.findAll(class_='hz-pro-search-results__item')
# for data in datas:
#   r=data.find(class_='hz-pro-search-result').find('a').get('href')
#   print(r)


# html_yaratish(source)
###########################################################################
# content 1
# vladi vostok  https://www.houzz.ru/professionals/dizayn-interyera/c/%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%B2%D0%BE%D1%81%D1%82%D0%BE%D0%BA--%D0%9F%D1%80%D0%B8%D0%BC%D0%BE%D1%80%D1%81%D0%BA%D0%B8%D0%B9-%D0%BA%D1%80%D0%B0%D0%B9
# vladi i https://www.houzz.ru/professionals/dizayn-interyera/c/%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%B2%D0%BE%D1%81%D1%82%D0%BE%D0%BA--%D0%9F%D1%80%D0%B8%D0%BC%D0%BE%D1%80%D1%81%D0%BA%D0%B8%D0%B9-%D0%BA%D1%80%D0%B0%D0%B9/p/30
# 19

# novgorod https://www.houzz.ru/professionals/dizayn-interyera/c/%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9-%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4--%D0%9D%D0%B8%D0%B6%D0%B5%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D1%81%D0%BA%D0%B0%D1%8F-%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C
# nov i https://www.houzz.ru/professionals/dizayn-interyera/c/%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9-%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4--%D0%9D%D0%B8%D0%B6%D0%B5%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D1%81%D0%BA%D0%B0%D1%8F-%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C/p/30
# 38

# def html_yaratish(res, i):
#     with open(f"{os.path.dirname(absolute_path)}\link-novgorod\{i}.html", 'w',
#               encoding='utf-8') as file:
#         file.write(res)


# result = requests.get(f'https://www.houzz.ru/professionals/dizayn-interyera/c/%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9-%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4--%D0%9D%D0%B8%D0%B6%D0%B5%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D1%81%D0%BA%D0%B0%D1%8F-%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C')
# source = result.text
# html_yaratish(source, 1)

# for i in range(1, 38):
#     result = requests.get(
#         f'https://www.houzz.ru/professionals/dizayn-interyera/c/%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9-%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4--%D0%9D%D0%B8%D0%B6%D0%B5%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D1%81%D0%BA%D0%B0%D1%8F-%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C/p/{i*15}')
#     source = result.text
#     html_yaratish(source, i+1)
# time.sleep(2)

#############################################################################
# content 2
# for j in range(1,4):

# y=2
# if y == 2:
#   link=[]
#   for i in range(1,39):
#     print(f'page {i}')
#     with open(f"{os.path.dirname(absolute_path)}\link-novgorod\html\{i}.html", encoding='utf-8') as file:
#                         source = file.read()
#     soup = BeautifulSoup(source, 'html.parser')
#     datas = soup.findAll(class_='hz-pro-search-results__item')
#     for data in datas:
#       r=data.find(class_='hz-pro-search-result').find('a').get('href')
#       link.append(r)
#     print(len(datas))
#   d={}
#   d['result']=link
#   with open(f"{os.path.dirname(absolute_path)}\\link-novgorod\\result.json", 'w',
#                                               encoding='utf-8') as file:
#                                       json.dump(d, file, indent=4, ensure_ascii=False)
#   y+=1
# if y == 3:
#   link=[]
#   for i in range(1,20):
#     print(f'page {i}')
#     with open(f"{os.path.dirname(absolute_path)}\link-vostok\html\{i}.html", encoding='utf-8') as file:
#                         source = file.read()
#     soup = BeautifulSoup(source, 'html.parser')
#     datas = soup.findAll(class_='hz-pro-search-results__item')
#     for data in datas:
#       r=data.find(class_='hz-pro-search-result').find('a').get('href')
#       link.append(r)
#     print(len(datas))
#   d={}
#   d['result']=link
#   with open(f"{os.path.dirname(absolute_path)}\\link-vostok\\result.json", 'w',
#                                               encoding='utf-8') as file:
#                                       json.dump(d, file, indent=4, ensure_ascii=False)
#   y+=1

# print(len(link))
#######################################################################################
# # content 3
# def html_yaratish(res, i, papka):
#     with open(f"{os.path.dirname(absolute_path)}\link-{papka}\{i}.html", 'w',
#               encoding='utf-8') as file:
#         file.write(res)


# def read_file(path):
#     file = open(path, "r", encoding='utf-8')
#     data = file.read()
#     file.close()
#     return data


# def read_json(path):
#     return json.loads(read_file(path))


# p_name = ['vostok', 'novgorod']
# for j in p_name:
#     links = read_json(
#         f"{os.path.dirname(absolute_path)}\link-{j}\\result.json")['result']
#     x = 1
#     for link in links:
#         result = requests.get(link)
#         source = result.text
#         html_yaratish(source, x, j)
#         x += 1
# # time.sleep(2)
# print(links)
#############################################################################
# content 4
# l = []
# name = []
# for i in range(1, 7543):
#     # for i in range(1,5):
#     all = {}
#     print(
#         f'########################### {i} ######################################')
#     if not isfile(f"{os.path.dirname(absolute_path)}\link-peter\{i}.html"):
#         continue
#     with open(f"{os.path.dirname(absolute_path)}\link-peter\{i}.html", encoding='utf-8') as file:
#         source = file.read()
#     soup = BeautifulSoup(source, 'lxml')
#     data = soup.find('script', type='application/ld+json')
#     try:
#         d = data.get_text()
#     except:
#         continue
#     # print(d)

#     lists = json.loads(d)[0]
#     all['Name'] = lists['name']
#     if lists['name'] in name:
#         continue
#     else:
#         name.append(lists['name'])

#     if 'address' in lists:
#         all['Address'] = lists['address']['addressLocality']
#     else:
#         all['Address'] = lists['areaServed']['name']
#     if '@id' in lists:
#         all['Link'] = lists['@id']
#     if 'telephone' in lists:
#         all['Telephone'] = lists['telephone']
#     if 'aggregateRating' in lists:
#         all['Rating'] = lists['aggregateRating']['ratingValue']
#     if 'description' in lists:
#         all['Description'] = lists['description']
#     if 'geo' in lists:
#         all['latitude'] = lists['geo']['latitude']
#         all['longitude'] = lists['geo']['longitude']

#     l.append(all)
# print(len(l))
# with open(f"{os.path.dirname(absolute_path)}\\link-peter\\result_all.json", 'w',
#           encoding='utf-8') as file:
#     json.dump(l, file, indent=4, ensure_ascii=False)
