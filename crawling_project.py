from selenium import webdriver
import pathlib
import datetime
import time


def get_info(browser, file):
    # Take all main article
    selector = "#container > section.fc.top-section.common-section.grid-1.regular-mode > article"
    main_article = browser.find_element_by_css_selector(selector)
    title = main_article.find_element_by_css_selector("h3 div span").text
    image = main_article.find_element_by_css_selector("div picture img").get_attribute('src')
    description = main_article.find_element_by_css_selector("article > a > p").text
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    final_str = st+"\n"+title+"\n"+description+"\n"+image+"\n\n"
    file.write(final_str)

    selector = "#container > section:nth-child(9) > section > section:nth-child(1) > ul > li"
    list = browser.find_elements_by_css_selector(selector)
    for item in list:
        title = item.find_element_by_css_selector("h3 div span").text
        image = item.find_element_by_css_selector("div picture img").get_attribute('src')
        description = item.find_element_by_css_selector("article > a > p").text
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        final_str = st + "\n" + title + "\n" + description + "\n" + image + "\n\n"
        file.write(final_str)


if __name__ == '__main__':
    browser = webdriver.Chrome("C:\webdrivers\chromedriver.exe")
    browser.implicitly_wait(1)
    browser.maximize_window()
    browser.get("http://www.walla.co.il")
    file = pathlib.Path("crawling.txt")
    if file.exists():
        with open('crawling.txt', 'a', encoding='utf-8') as crawling_file:
            get_info(browser, crawling_file)
    else:
        with open('crawling.txt', 'a', encoding='utf-8') as crawling_file:
            get_info(browser, crawling_file)
    browser.close()

