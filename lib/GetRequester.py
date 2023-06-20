import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response=requests.get(self.url)
        return response.content
        

    def load_json(self):
        python_list=[]
        programs=json.loads(self.get_response_body())
        for program in programs:
            python_list.append(program)
        return python_list