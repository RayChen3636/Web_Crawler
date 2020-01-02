from urllib.request import urlopen,urlretrieve
import json
import os
# MAC電腦才要加的兩行
# import ssl
# ssl._create_default_https_context = ssl.create_unverified_context()

# range(12) == range(0, 12) -> [0, 1, 2,..., 11]
for m in range(10):
    url = "https://www.google.com/doodles/json/2019/" + str(m + 1) +"?hl=zh_TW"
    print("現在在處理頁面", url)
    response = urlopen(url)

    doodles = json.load(response)
    # doodles -> list  d -> Dictionary
    for d in doodles:
        url = "https:" + d["url"]
        print(d["title"], url)
        # print(url.split("/")[-1])

        dirname = "doodles/" + str(m + 1) + "/"
        if not os.path.exists(dirname):
            os.mkdir(dirname)

        frame = dirname + url.split("/")[-1]
        urlretrieve(url, frame)