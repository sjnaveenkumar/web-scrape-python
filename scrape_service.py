from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selectorlib import Extractor
import time,random

browser_driver = None

def init():
    global browser_driver
    options = webdriver.FirefoxOptions()
    options.headless = True
    browser_driver = webdriver.Firefox(options=options)


def browse_and_extract(url,template_type):
    browser_driver.get(url)
    raw_html = browser_driver.page_source
    e = Extractor.from_yaml_string(get_template(template_type))
    raw_data = e.extract(raw_html)
    filtered_data = []
    if raw_data['results'] is not None:
        for item in raw_data['results']:
            if item['title'] is None:
                item['title'] = ''
            if item['image'] is None:
                item['image'] = ''
            if item['deal'] is None:
                item['deal'] = ''
            if item['link'] is None:
                item['link'] = ''
            filtered_data.append(item)
        return filtered_data
    return []

def get_template(type):
    template_string = ""
    with open(type+'_template.yml', 'r') as f:
        template_string = f.read()
    return template_string