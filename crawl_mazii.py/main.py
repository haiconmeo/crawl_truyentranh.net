import requests
import bs4 as bs 
import json
# req = requests.get("http://mina.mazii.net/api/getKanji.php?from=1&to=1945")



# with open("manh.txt",'w',encoding='utf-8') as f:
# #     f.write(json.dumps(req.json()))
# # f.write(len(data[i]))
#     for i in range(len(data)):
#         f.write("\n=================================================\n")
#         f.write("Hán tự:{}\n".format(data[i]["word"]))
#         f.write("Hán Việt:{}\n".format(data[i]["cn_mean"]))
#         f.write("Nghĩa tiếng việt:{}\n".format(data[i]["vi_mean"]))
#         f.write("Âm on:{}\n".format(data[i]["onjomi"]))
#         f.write("Âm kun:{}\n".format(data[i]["kunjomi"]))
#         f.write("note:{}\n".format(data[i]["note"].replace('※','\n').replace("∴"," ")))
for i in range(1,19):
    req = requests.get("http://mina.mazii.net/api/getPharse.php?categoryid={}".format(i))
    data = req.json()
    with open("1000 câu giao tiếp.txt",'a',encoding='utf-8') as f:
        for i in range(len(data)):
            f.write("\n=================================\n")
            f.write("Tiếng việt:{}\n".format(data[i]["vietnamese"]))
            f.write("romaji:{}\n".format(data[i]["pinyin"]))
            f.write("Tiếng nhật:{}\n".format(data[i]["japanese"]))

