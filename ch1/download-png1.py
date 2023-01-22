# ライブラリの取り込み --- (※1)
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# URLと保存パスを指定
url = "https://uta.pw/shodou/img/28/214.png"
savename = "test.png"

# ダウンロード --- (※2)
urllib.request.urlretrieve(url, savename)
print("保存しました")

