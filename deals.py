from scrape_service import *

def get_deals():
    return browse_and_extract('https://www.amazon.in/','top_deals')
    