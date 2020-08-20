# list_1 = []
# with open('E:/new 2.txt', 'r', encoding='utf-8') as f:
#     content = f.readlines()
#     for i in content:
#         i = i.replace('\n', '').split('\t')
#         i = i[0]
#         list_1.append(i)
# print(list_1)
# list_2 = []
# with open('E:/new 6.txt', 'r', encoding='utf-8') as f:
#     content = f.readlines()
#     for j in content:
#         j = j.replace('\n', '').split('\t')
#         j = j[0]
#         list_2.append(j)
# print(list_2)
# for m in list_1:
#     if m not in list_2:
#         print(m)


# with open("E:\\colaOpt\\3.csv","r",encoding="utf-8") as f:
#     lines = f.readlines()
#     for i in lines:
#         i = i.strip().split(',')
#         a = i[0]
#         b = i[1]
#         c = i[2]
#         d = i[3]
#         e = i[4]
#         f = i[5]
#         g = i[6]
#         h = i[7]
#         date = "INSERT INTO colaOpt VALUES ('{}','{}','{}','{}','{}','{}','{}','{}');\n".format(a,b,c,d,e,f,g,h)
#         with open('colaPrize.txt', 'a', encoding='utf-8') as g:
#             g.write(date)
#
# with open('E:\\colaOpt\\1.csv', 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#     for i in lines:
#         i = i.strip().split(',')
#         yonghubiaoshi = i[0]
#         date = str(yonghubiaoshi) + '\n'
#         with open('1.txt', 'a', encoding='utf-8') as g:
#             g.write(date)

# with open('')
# import re
#
# str_0 =?
# str = str(str_0)
# str_1 = re.findall('<span class="(.*?)">', str)
# print(str_1)

# from redis import Redis
# redis_cli = Redis('127.0.0.1', 6379, db=9)
# import re
# def handle(value):
#         comment_1 = str(value)[0:-9].replace('[', '').replace(']', '').replace('\'<span class="tag">', '')
#         print(comment_1)
#         comment_2 = re.findall('<span class="(.*?)">', comment_1)
#         for i in comment_2:
#             t = redis_cli.hget('rzygwo', i)
#             if t:
#                 t = t.decode('utf-8')
#                 temp = '<span class="{}"></span>'.format(i)
#                 comment_1 = comment_1.replace(temp, t)
#         return comment_1
#
# if __name__ == '__main__':
#     comment = ['<span class="tag"><span class="zdc3im"></span><span class="zdczub"></span><span class="zdc5bc"></span></span>']
#     a = handle(comment)
#     # a = handle([])
#     print(a)

# l =['<span class="tag"><span class="rzygwo"></span><span class="rzygwo"></span><span class="rzygwo"></span>KTV</span>']
# l = str(l)[0:-9]
# print(l)
import re
# response = 'https://pimg.dmcdn.cn/perform/project/1747/174763_n.jpg?_t=1550108143703'
# https://img.alicdn.com/bao/uploaded/i3/2251059038/O1CN01PO4FUu2GdS91mS1OX_!!0-item_pic.jpg
# jpgname = response.split('/')[-1]
# if '?' in jpgname:
#     jpgname = jpgname.split('?')[0]
# time_in = re.findall('/(\d+.)jpg', response)[0]
# print(time_in)
# print(jpgname)
# time_in = str(time_in)[1: -1].replace("'", '')
# print(time_in)
# import os
#
# os.mkdir('E:\\img_damai\%s' % (17))


# import collections
# l = ['https://img.alicdn.com/bao/uploaded/i1/2251059038/O1CN01ji6Y0p2GdS8aFQDky_!!0-item_pic.jpg', 'https://img.alicdn.com/bao/uploaded/i1/2251059038/O1CN01Ljkh5w2GdS8rqhtAG_!!0-item_pic.jpg', 'https://img.alicdn.com/bao/uploaded/i1/2251059038/O1CN01riPSuT2GdS8jBIALE_!!0-item_pic.jpg', 'https://pimg.dmcdn.cn/perform/project/1740/174097_n.jpg?_t=1548903058931', 'https://img.alicdn.com/bao/uploaded/i2/2251059038/O1CN01pe2EAq2GdS8mAdsMi_!!0-item_pic.jpg', 'https://pimg.dmcdn.cn/perform/project/1753/175361_n.jpg?_t=1551432421578', 'https://img.alicdn.com/bao/uploaded/i4/2251059038/O1CN01WH12X92GdS8WqtHAa_!!0-item_pic.jpg', 'https://pimg.dmcdn.cn/perform/project/1597/159781_n.jpg?_t=1539149834815', 'https://img.alicdn.com/bao/uploaded/i2/2251059038/O1CN01t6zLrE2GdS8i6cIBc_!!0-item_pic.jpg', 'https://img.alicdn.com/bao/uploaded/i3/2251059038/O1CN019tSuy82GdS8nhkqcv_!!0-item_pic.jpg', 'https://img.alicdn.com/bao/uploaded/i4/2251059038/O1CN012oU1ay2GdS8Y11yKn_!!0-item_pic.jpg', 'https://img.alicdn.com/bao/uploaded/i1/2251059038/O1CN01l4udM22GdS8ePVnbW_!!0-item_pic.jpg', 'https://img.alicdn.com/bao/uploaded/i2/2251059038/O1CN015TuEXx2GdS8VkGVas_!!0-item_pic.jpg', 'https://img.alicdn.com/bao/uploaded/i4/2251059038/O1CN01zfdUXx2GdS8shTKOv_!!0-item_pic.jpg', 'https://img.alicdn.com/bao/uploaded/i4/2251059038/O1CN01cJzaut2GdS90Lgc9A_!!0-item_pic.jpg', 'https://pimg.dmcdn.cn/perform/project/1729/172996_n.jpg?_t=1546506472900', 'https://img.alicdn.com/bao/uploaded/i2/2251059038/O1CN01Et9Ge32GdS8tQsYln_!!0-item_pic.jpg', 'https://img.alicdn.com/bao/uploaded/i2/2251059038/O1CN01UsOmT92GdS8YPWtAx_!!0-item_pic.jpg', 'https://pimg.dmcdn.cn/perform/project/1681/168102_n.jpg?_t=1541661171094', 'https://img.alicdn.com/bao/uploaded/i3/2251059038/O1CN01OuzBoK2GdS8dS8YPv_!!0-item_pic.jpg', 'https://img.alicdn.com/bao/uploaded/i3/2251059038/O1CN01PcyJY62GdS8cF4SsN_!!0-item_pic.jpg', 'https://img.alicdn.com/bao/uploaded/i3/2251059038/O1CN01TnO0Qt2GdS8bT4TEb_!!0-item_pic.jpg', 'https://pimg.dmcdn.cn/perform/project/1584/158453_n.jpg?_t=1531980290325', 'https://pimg.dmcdn.cn/perform/project/1575/157593_n.jpg?_t=1531362342453', 'https://img.alicdn.com/bao/uploaded/i3/2251059038/O1CN01zUcSIe2GdS8RIZEnf_!!0-item_pic.jpg', 'https://pimg.dmcdn.cn/perform/project/1723/172380_n.jpg?_t=1545713535494', 'https://pimg.dmcdn.cn/perform/project/1675/167574_n.jpg?_t=1541144213996', 'https://img.alicdn.com/bao/uploaded/i4/2251059038/O1CN01I4QVIx2GdS8w5ilDP_!!0-item_pic.jpg', 'https://img.alicdn.com/bao/uploaded/i3/2251059038/O1CN013ZA7So2GdS8cNngQg_!!0-item_pic.jpg', 'https://pimg.dmcdn.cn/perform/project/1753/175372_n.jpg?_t=1551423523874', 'https://img.alicdn.com/bao/uploaded/i2/2251059038/O1CN01uNsIXv2GdS8ivaMzS_!!0-item_pic.jpg', 'https://pimg.dmcdn.cn/perform/project/1751/175187_n.jpg?_t=1551151969726', 'https://img.alicdn.com/bao/uploaded/i2/2251059038/O1CN013CEEuG2GdS8apMhwL_!!0-item_pic.jpg', 'https://pimg.dmcdn.cn/perform/project/1753/175342_n.jpg?_t=1551344179125', 'https://img.alicdn.com/bao/uploaded/i1/2251059038/O1CN013VQBsL2GdS8a0QzXF_!!2-item_pic.png', 'https://pimg.dmcdn.cn/perform/project/1695/169521_n.jpg?_t=1551325562136', 'https://pimg.dmcdn.cn/perform/project/1597/159781_n.jpg?_t=1539149834815', 'https://img.alicdn.com/bao/uploaded/i4/2251059038/O1CN01hBrGxB2GdS8lLDKEi_!!0-item_pic.jpg', 'https://img.alicdn.com/bao/uploaded/i2/2251059038/O1CN01r67oVf2GdS8f5cNrA_!!0-item_pic.jpg']
#
# print([item for item, count in collections.Counter(l).items() if count > 1])

#
# l = ['2018.10.10-2020.06.30 【每周,周日13:00-15:00】(13岁-16岁)', '2018-10-10-2020.06.30 【每周,周六13:00-15:00】(9岁-12岁)', '2018.10.10-2020.06.30【每周,周六10:00-12:00】(5岁-8岁)']
# # for i in l:
# #     a = i.join(i, '|')
# #     print(a)
# str = '|'.join(l)
# print(str)

# 、


list_all = [{'grid_y': 124155, 'count': 15, 'grid_x': 484864}, {'grid_y': 124155, 'count': 5, 'grid_x': 484867}, {'grid_y': 124157, 'count': 30, 'grid_x': 484852}]
min_count = list_all[0]["count"]
for i in list_all:
    min_count = min(i['count'], min_count)
print(min_count)
