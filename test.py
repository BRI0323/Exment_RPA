from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# URLと認証情報
url = "http://10.106.1.60/admin/"
username = "admin"
password = "p@$$w0rd"

# WebDriverのパス
driver_path = "/path/to/your/chromedriver"

# WebDriverの設定とインスタンス化
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--incognito")
driver = webdriver.Chrome(driver_path, options=options)

# 指定された回数だけ繰り返す
for _ in range(指定された回数):
    try:
        # URLにアクセス
        driver.get(url)

        # ログイン処理（必要に応じて）

        # 最後のページへのナビゲーション
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#app > section.content > div > div > div > div.box-footer.table-footer.clearfix > ul > li.page-item.active > span"))).click()

        # 全選択
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#app > section.content > div > div > div > div:nth-child(1) > div.pull-left > div.icheckbox_minimal-blue > ins"))).click()

        # プルダウン押す
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#app > section.content > div > div > div > div:nth-child(1) > div.pull-left > div.btn-group.grid-select-all-btn > button > span.caret"))).click()

        # 一括削除
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#app > section.content > div > div > div > div:nth-child(1) > div.pull-left > div.btn-group.grid-select-all-btn.open > ul > li > a"))).click()

    except Exception as e:
        print(f"An error occurred: {e}")

# ブラウザを閉じる
driver.quit()
