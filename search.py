from scrape_service import *

def do_search(query,page=0):
    return browse_and_extract("https://www.amazon.in/s?k="+query+"&page="+page,'search')
    