from scrape_service import browse_and_extract
from enums import Template

def get_deals():
    return browse_and_extract('https://www.amazon.in/',Template.TOP_DEALS)
    