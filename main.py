import os
import threading
import time
import shutil
import platform
import subprocess
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def check(chrome_version):
    chromedriver_version_output = subprocess.check_output(["chromedriver", "--version"]).decode("utf-8").strip()
    chromedriver_version = chromedriver_version_output.split()[-1]
    major_chrome_version = chrome_version.split(".")[0]
    major_chromedriver_version = chromedriver_version.split(".")[0]
    if major_chrome_version == major_chromedriver_version:
        return True
    else:
        print(f"ChromeのバージョンとChromeDriverのバージョンが互換性がありません。Chromeのバージョン: {chrome_version}, ChromeDriverのバージョン: {chromedriver_version}")
        return False

print("NiftyKids-Spammer by yukina67")

url = "https://kids.nifty.com/cs/catalog/kids_vote/result/1.htm?aid=240325569308"
dl = "https://cdn.discordapp.com/attachments/1224964635510177802/1224964712744353894/chromedriver.exe?ex=661f684a&is=660cf34a&hm=ac3230400237a3ef3be73cf0d753b5651408bf4d55c4bb5ff3d2fa9168bd147a"
dir = os.path.join(os.environ["USERPROFILE"], "chromedriver")
response = requests.get(url)
path = os.path.join(dir, "chromedriver.exe")
html_content = """<div class="vote-inner" style="width: 300px; /*ie*/ margin: 0; padding: 0 !important;  padding: 0 10px 0 10px;  /*ie*/ overflow: hidden; text-align:left; background:url(/images/top/r3_vote_baseline.gif) left bottom repeat-y;"><div style="margin:0 0 0 10px;"><form name="point" method="post" action="/cs/catalog/kids_vote/complete/catalog_240325569308_1.htm"><p class="vote-theme" style="margin:14px 0 14px 0 !important;"><span style="font-weight:normal !important;" class="CommentB">好きなラーメンの味は？</span><img src="/images/top/main_icon_new.gif" alt="NEW" width="33" height="18"></p><div class="vote-item"><input type="radio" id="240325569308_vote1" name="vote" value="1"> <label for="240325569308_vote1">やっぱり定番！しょうゆ</label></div><div class="vote-item"><input type="radio" id="240325569308_vote2" name="vote" value="2"> <label for="240325569308_vote2">あっさりおいしい！塩</label></div><div class="vote-item"><input type="radio" id="240325569308_vote3" name="vote" value="3"> <label for="240325569308_vote3">食べればあったか！みそ</label></div><div class="vote-item"><input type="radio" id="240325569308_vote4" name="vote" value="4"> <label for="240325569308_vote4">濃厚おいしい！とんこつ</label></div><div class="vote-item"><input type="radio" id="240325569308_vote5" name="vote" value="5"> <label for="240325569308_vote5">1つなんて決められない！全部好き！</label></div><br><table class="vote-link" width="270" cellpadding="0" cellspacing="0" style="font-size:95%;"><tbody><tr><td class="vote-decision" width="160" align="left"><input class="pc-img" type="image" value="決定" src="/images/top/r3_vote_decision_bt.gif" style="width:102px;" name="submit2"><input class="smp-img" type="image" value="決定" src="/images/top/r3_vote_decision_bt_smp.png " style="width:102px; display:none;" name="submit2"></td><td class="vote-result"><p style="background:url(/images/top/gray_arrow.gif) no-repeat; padding-left:20px; background-position:0 3px;/*ie*/"><a href="/cs/catalog/kids_vote/result/1.htm?aid=240325569308">結果をみる</a></p></td></tr></tbody></table></form></div><!--/r3_vote_form --></div>"""
soup = BeautifulSoup(html_content, "html.parser")
options1 = soup.find_all(
    lambda tag: tag.name == "label" and tag.get("for") and tag.get("for").endswith("_vote1")
)
options2 = soup.find_all(
    lambda tag: tag.name == "label" and tag.get("for") and tag.get("for").endswith("_vote2")
)
options3 = soup.find_all(
    lambda tag: tag.name == "label" and tag.get("for") and tag.get("for").endswith("_vote3")
)
options4 = soup.find_all(
    lambda tag: tag.name == "label" and tag.get("for") and tag.get("for").endswith("_vote4")
)
options5 = soup.find_all(
    lambda tag: tag.name == "label" and tag.get("for") and tag.get("for").endswith("_vote5")
)
start_value = 1

for i1, option in enumerate(options1, start=start_value):
    option_text1 = option.text.strip()
    print(f"{i1}. {option_text1}")

start_value += len(options1)

for i2, option in enumerate(options2, start=start_value):
    option_text2 = option.text.strip()
    print(f"{i2}. {option_text2}")

start_value += len(options2)

for i3, option in enumerate(options3, start=start_value):
    option_text3 = option.text.strip()
    print(f"{i3}. {option_text3}")

start_value += len(options3)

for i4, option in enumerate(options4, start=start_value):
    option_text4 = option.text.strip()
    print(f"{i4}. {option_text4}")

start_value += len(options4)

for i5, option in enumerate(options5, start=start_value):
    option_text5 = option.text.strip()
    print(f"{i5}. {option_text5}")

option = int(input("投票するオプションを1から5の間で選択してください: "))
kaisuu = int(input("投票する回数を入力してください: "))
print("投票を開始します")

if not os.path.exists(path):
    os.makedirs(dir, exist_ok=True)
    print("必要なファイルをダウンロードします")
    time.sleep(0.5)
    print("ダウンロードを開始します...")
    response = requests.get(dl)
    with open(path, "wb") as f:
        f.write(response.content)
    print("ファイルのダウンロードが完了しました。")

def touhyou(url, option, nankaimeka):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--allow-running-insecure-content")
    service = Service(path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "240325569308_vote4")))

    vote_option_id = "240325569308_vote" + str(option)
    vote_option = driver.find_element(By.ID, vote_option_id)
    vote_option.click()

    submit_button = driver.find_element(By.NAME, "submit2")
    submit_button.click()

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "completeBtn")))
        
        complete_btn = driver.find_element(By.ID, "completeBtn")
        complete_btn.click()
        
        time.sleep(0.01) # 閉じるまで何秒か

        print(f"\nsuccess:{nankaimeka}回目の投票に成功！\n")
    except Exception as e:
        if "Mixed Content" in str(e):
            pass
        else:
            print(f"\nerror:{nankaimeka}回目投票失敗！\n")
            
        driver.quit()

threads = []
for i in range(kaisuu):
    thread = threading.Thread(target=touhyou, args=(url, option, i + 1))
    threads.append(thread)
    thread.start()
    time.sleep(1)

try:
    for thread in threads:
        thread.join()
except KeyboardInterrupt:
    print("\nCtrl+C が検出されました。プログラムを終了します。")

print("\n全ての投票が完了しました。")
print("10秒後に自動でプログラムを終了します\n手動で終了する場合はCtrl+Cで終了してください。")
time.sleep(10)
