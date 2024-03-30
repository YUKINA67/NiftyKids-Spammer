# 使用できない場合
# VPNまたはProxyを使用してください
# GoogleChromeがインストールされているか確認してください
# GoogleChromeとChromeDriverの互換性があるか確認してください
# ChromeDriverのパスが正しいか確認してください
# ファイルパスの\を二つにしてください
# これでもできない場合はDiscord @yukina67のDMまで
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading
import time

threads = [] 

url = "https://kids.nifty.com/cs/catalog/kids_vote/result/1.htm?aid=240325569306"

print("このツールはゆきなさんが作りました、あまりゆきなさんを舐めるなよ\nちんちんは舐めてもらうけどな(笑)\n\n") 
option = int(input("投票するオプションを1から5の間で選択してください: "))
kaisuu = int(input("投票する回数を入力してください: "))

def touhyou(url, option):
    service = Service("") # chrome driverのぱす
    driver = webdriver.Chrome(service=service)
    driver.get(url)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "240325569306_vote4")))

    vote_option_id = "240325569306_vote" + str(option)
    vote_option = driver.find_element(By.ID, vote_option_id)
    vote_option.click()

    submit_button = driver.find_element(By.NAME, "submit2")
    submit_button.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "completeBtn")))
    
    complete_btn = driver.find_element(By.ID, "completeBtn")
    complete_btn.click()
    
    time.sleep(0.01) # 閉じるまで何秒か
    print("success：投票成功！")
    driver.quit()

    print("投票を開始します")

for _ in range(kaisuu):
    thread = threading.Thread(target=touhyou, args=(url, option))
    threads.append(thread) 
    thread.start()
    
    time.sleep(2.5) # 遅延
    # 高スペック 2.5以下
    # 低スペック 5.3以上
    # 長時間やる場合はさらに遅延を増やすことを推奨します
    # 少ない数を何回もやったほうが効率的だと思います
    # インターネットの環境にもよるので自分で試して決めてください 

    for thread in threads: 
        thread.join()

    print("全ての投票が完了しました。")
