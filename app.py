
from flask import Flask,request
from scrape_service import *
from search import *
from deals import get_deals

app = Flask(__name__)

init()
@app.route('/search')
def search():
    query = request.args.get("query")
    page = request.args.get('page')
    return do_search(query,page)
@app.route('/top-deals')
def top_deals():
    return get_deals()
    

if __name__ == '__main__':
    app.run(port=5050)
