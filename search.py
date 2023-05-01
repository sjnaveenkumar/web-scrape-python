from scrape_service import browse_and_extract
from enums import Template

def do_search(query,page=1):
    return browse_and_extract("https://www.amazon.in/s?k="+query+"&page="+page,Template.SEARCH)
    