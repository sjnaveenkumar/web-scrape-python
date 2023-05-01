from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selectorlib import Extractor

browser_driver = None

def init():
    global browser_driver 
    ChromeOptions = webdriver.ChromeOptions()
    ChromeOptions.add_argument('--headless')
    executable_path=ChromeDriverManager().install()
    browser_driver = webdriver.Chrome(executable_path, options=ChromeOptions)


def browse_and_extract(url,template_type):
    browser_driver.get(url)
    raw_html = browser_driver.page_source
    e = Extractor.from_yaml_string(get_template(template_type))
    raw_data = e.extract(raw_html)
    if raw_data is not None:
        filtered_data = [item for item in raw_data['results'] if None not in item.values()]
        return filtered_data
    return []

def get_template(type):
    template_string = ""
    with open(type+'_template.yml', 'r') as f:
        template_string = f.read()
    return template_string