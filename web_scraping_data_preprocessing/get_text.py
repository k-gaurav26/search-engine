import time
from selenium import webdriver

from bs4 import BeautifulSoup
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# s=Service(r"C:\Users\gaura\Downloads\black box\chromedriver_win32") ---------------- error
s=Service(r"C:\Users\gaura\Downloads\black box\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=s)

with open(r"F:\Search engine on DSA problems\web_scraping_data_preprocessing\urls.txt", "r") as f:
    all_urls = f.read()
    urls = all_urls.split()

k = 0

for question in urls:
    driver.get(question)
    time.sleep(8)
    html = driver.page_source
    q_soup = BeautifulSoup(html, 'html.parser')

    q_text = q_soup.find("div", {"id": "problem-statement"})

    second_X = q_soup.select(selector="math")

    for ele in second_X:
        ele.decompose()

    final_text = q_text.getText().split("Constraints")  # to remove contents after the "Constraints" Section of CodeChef

    with open("text"+str(k)+".txt", "w+", encoding="utf-8") as f:
        f.write(final_text[0])
        f.close()
    k += 1
    # if k >= 2:
    #     break
    