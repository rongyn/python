# def ninenine():
#     for h in range(1, 10):
#         for l in range(1, 10):
#             if (l < h):
#                 print("%d*%d=%d" % (l, h, l * h), end="\t")
#         print()
#
#
# ninenine()
#
#
# def sum1(a, b):
#     sum3 = a + b
#     return sum3


# print(sum1(1, 2))
# c = sum1(3, 4)
# print(c + 3)
#
#
# def zhuanhuan(g):
#     kg = g / 1000
#     kg = str(kg) + 'kg'
#     return kg
#
#
# print(zhuanhuan(1000))
#
#
# def display_message():
#     print("我学到了定义函数和调用")
#
#
# display_message()


# def favorite_book(title):
#     print("one of my favorite books is %s" % title)
#
#
# favorite_book("Alice in Wonderland")
#
#
# def make_shirt(size, logo):
#     print("T-shirt size:%s,logo:%s" % (size.title(), logo.title()))
#
#
# make_shirt("s", "nike")
#
#
# def describe_city(capital, country="China"):
#     print("%s is in %s" % (capital, country))
#
#
# describe_city("Reykjavik", "Iceland")
# describe_city("Beijing")


def make_album(singer_name, special_album, num=None):
    album = {'singer_name': singer_name, 'special_album': special_album}
    if num:
        album['num'] = num
    return album


singer1 = make_album('jason', '这，就是爱')
singer2 = make_album('JJ', '赤壁赋', num=5)
singer3 = make_album('BIGBANG ', 'BANGBANGBANG')
print(singer1, singer2, singer3)
while True:
    print("请输入专辑的歌手和名称,输入q退出")
    singer_n = input("歌手名：")
    if singer_n == 'q':
        break
    album_n = input("专辑名：")
    if album_n == 'q':
        break
    num_n = input("歌曲数量：")
    if num_n == 'q':
        break
    album_info = make_album(singer_n, album_n, num_n)
    print(album_info)
