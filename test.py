from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time
import tkinter as tk

# グローバル変数を定義
number = 0
window = None  # グローバル変数でウィンドウインスタンスを保持

def retrieve_input():
    global number, window  # グローバル変数を関数内で使用する宣言
    # 入力フィールドからテキストを取得
    input_value = input_field.get()
    try:
        # 文字列を整数に変換
        number = int(input_value)
        print("入力された数字:", number)
        if window is not None:
            window.destroy()
        
        # ブラウザを制御し、ログを削除する
        browser = control_browser()
        delete_log(browser)
    except ValueError:
        print("入力された値が数字ではありません:", input_value)


def control_browser():
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    
    # Webサイトにアクセス
    url = 'http://10.106.1.60/admin'
    browser.get(url)
    time.sleep(2)
    browser.fullscreen_window()
    # ログイン処理
    WebDriverWait(browser, 2).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="username"]')))
    browser.find_element(By.NAME, 'username').send_keys('admin')
    
    WebDriverWait(browser, 2).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="password"]')))
    browser.find_element(By.NAME, 'password').send_keys('p@$$w0rd')
    
    # 指定されたセレクタのボタンをクリック
    login_button_selector = 'body > div > div.login-box-body > form > div.row > div.col-xs-12.col-sm-8.col-sm-offset-2 > button'
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, login_button_selector))).click()
    
    # logsへアクセス
    browser.get('http://10.106.1.60/admin/auth/logs')
    browser.fullscreen_window()
    
    return browser  # ブラウザのインスタンスを返す

def delete_log(browser):
    global number
    for i in range(number):
        try:
            # セレクトボックス要素を取得し、'100'を選択
            select_element = WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#app > section.content > div > div > div > div.box-footer.table-footer.clearfix > label > select")))
            select_object = Select(select_element)
            select_object.select_by_visible_text('100')
            time.sleep(5)
            # ページネーションを操作して最後のページに移動
            # 例: 最後のページボタンのセレクタが 'a.last-page' だと仮定
            last_page_button_selector = '#app > section.content > div > div > div > div.box-footer.table-footer.clearfix > ul > li:nth-child(11) > a'
            last_page_button = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, last_page_button_selector)))
            last_page_button.click()
            time.sleep(3)  # ページが完全に読み込まれるのを待つ
            
            # チェックボックスをクリック #CLASS_NAMEを使用
            class_name = 'iCheck-helper'  # 操作したい要素のクラス名
            element = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, class_name)))
            element.click()
            time.sleep(1)
            
            # プルダウン押す（一括操作のプルダウンメニューを開く）
            # ボタンのセレクタ
            button_selector = '#app > section.content > div > div > div > div:nth-child(1) > div.pull-left > div.btn-group.grid-select-all-btn > button'
            pulldown = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, button_selector)))
            pulldown.click()
            time.sleep(1)
            
            #delete_button
            class_name = 'grid-batch-0'  # 操作したい要素のクラス名
            element = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, class_name)))
            element.click()
            
            #confirm button
            button_selector = '.swal2-confirm.swal2-styled'
            confirm_button = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, button_selector)))

            # JavaScriptを使用してクリックイベントを発火させる
            browser.execute_script("arguments[0].click();", confirm_button)
            time.sleep(1)
            browser.get('http://10.106.1.60/admin/auth/logs')   
        except Exception as e:
            print(f"エラーが発生しました: {e}")


def main():
    # Tkinter ウィンドウの初期化
    global input_field  # グローバル変数を関数内で使用する宣言
    window = tk.Tk()
    window.title("数字入力フォーム")

    # 注意書きのラベルを作成
    label = tk.Label(window, text="ループ回数を入力してください。")
    label.pack()  # ラベルの配置

    # 入力フィールドの作成
    input_field = tk.Entry(window)
    input_field.pack()

    # ボタンの作成、クリック時に retrieve_input 関数を実行
    submit_button = tk.Button(window, text="Submit", command=retrieve_input)
    submit_button.pack()

    # ウィンドウの表示
    window.mainloop()

if __name__ == '__main__':
    main()
