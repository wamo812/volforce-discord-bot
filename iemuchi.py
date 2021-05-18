from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json , requests , os , values


#色々定数
MAIL = os.environ.get('SDVX_MAIL') #ログインメールアドレス
PASSWORD = os.environ.get('SDVX_PASSWORD') #ログインメールパスワード
DRIVER_PATH = os.path.dirname(os.path.abspath(__file__)) + '/chromedriver' #chromedriverのパス
USER_PAGE_URL_PREFIX = 'https://p.eagate.573.jp/game/sdvx/vi/playdata/rival/profile.html?rival_id=' #ユーザデータページのURLのID除いた箇所のプレフィックス

#ブラウザ起動
options = Options()
options.add_argument('--headless') #ヘッドレス解除したい場合はこの行をコメントアウト（動き見れてオモロイ）
driver = webdriver.Chrome(executable_path=DRIVER_PATH,options=options)

def main():
    login()
    for id in values.ID_LIST:
        send_volforce(id)
    driver.close() #ﾇｫ送信後にブラウザ自動で閉じたくない場合はこの行をコメントアウト


#IDからユーザページへのURLを作成
def create_user_page_url_from_id(id):
    return USER_PAGE_URL_PREFIX + id

#ログイン
def login():
    driver.get(create_user_page_url_from_id(values.ID_LIST[0]))
    driver.find_element_by_id('login_btn').click()
    driver.find_element_by_id('id_userId').send_keys(MAIL)
    driver.find_element_by_id('id_password').send_keys(PASSWORD)
    driver.find_element_by_class_name('submit').click()

#idからﾇｫをdiscordに送信
def send_volforce(id):
    driver.get(create_user_page_url_from_id(id))

    player_name = driver.find_element_by_xpath('//*[@id="player_name"]/p[2]').text
    card_url = driver.find_element_by_xpath('//*[@id="apcard"]/p/img').get_attribute('src')
    volforce = driver.find_element_by_id('force_point').text
    title = driver.find_element_by_xpath('//*[@id="player_name"]/p[1]').text

    main_content = {
        'username': player_name + '(' + title + ')',
        'avatar_url': card_url,
        'content': 'ﾇｫ：' + volforce
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(values.WEBHOOK_URL, json.dumps(main_content), headers=headers)

#main実行
if __name__ == "__main__":
    main()