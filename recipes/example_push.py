import json
import requests
document={'url':"http://example.com",'text':"Ceci est un test","id":'00000','title':'Test'}
doc={'fields':document}
requests.post(data=json.dumps(doc),url= "http://10.100.2.4:8080/document/v1/wiki_article/wiki_article/docid/"+document['id']).json()

