import requests
import json
import pandas as pd

api_key = "*****" # API KEY
base_url = "https://api.odcloud.kr/api/nts-businessman/v1/"

def validate(b_data):
    params = { "businesses": [] }
    
    for i in b_data:
        params["businesses"].append({ "b_no": i[0], "p_nm": i[1], "start_dt": i[2], "b_nm": i[3] })
    
    r = requests.post(base_url+"validate?serviceKey="+api_key, json=params)
    data = json.loads(r.text)
    if(data['status_code'] == "OK"):
        return data['data']
    else:
        return "Error"

def status(b_no):
    params = { "b_no": b_no }
    
    r = requests.post(base_url+"status?serviceKey="+api_key, json=params)
    data = json.loads(r.text)
    if(data['status_code'] == "OK"):
        return data['data']
    else:
        return "Error"
    

print( validate( [ ["사업자등록번호", "대표자명", "개업일자", "상호명"] ] ))

print( status( [ "사업자등록번호"] ) )
