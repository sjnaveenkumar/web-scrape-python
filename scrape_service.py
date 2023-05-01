
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selectorlib import Extractor
from enums import Template

browser_driver = None

def init():
        global browser_driver
        options = webdriver.FirefoxOptions()
        options.headless = True
        browser_driver = webdriver.Firefox(options=options)

def browse_and_extract(url,template_type):
    browser_driver.get(url)
    wait = WebDriverWait(browser_driver, 10)
    try:
        if template_type == Template.TOP_DEALS:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li[role="listitem"] span.a-truncate-cut')))
    except TimeoutException:
        return {'error':{'message':"TIME OUT ERROR"}}
    raw_html = browser_driver.page_source
    e = Extractor.from_yaml_string(get_template(template_type))
    raw_data = e.extract(raw_html)  
    filtered_data = []
    if raw_data['results'] is not None:
        for item in raw_data['results']:
            if item['title'] is None:
                continue
            filtered_data.append(item)
        return {'result':filtered_data}
    return []

def get_template(type:Template):
    template_string = ""
    with open(type.value+'_template.yml', 'r') as f:
        template_string = f.read()
    return template_string