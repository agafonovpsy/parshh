import requests
from bs4 import BeautifulSoup as bs

headers = {"accept": "*/*", 
"user-agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36 OPR/58.0.3135.79 (Edition Yx)"}
base_url = "https://spb.hh.ru/search/resume?area=2&exp_period=all_time&logic=normal&order_by=publication_time&pos=workplace_organization&text=devim&mark=main_page_last_search_5"

def hh_search (base_url, headers):
	session = requests.session()
	request = session.get(base_url, headers = headers)
	if request.status_code == 200:
	   print ("OK")
	else :
		print ("LOX")
hh_search(base_url, headers)
