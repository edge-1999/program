import numpy as np
import requests
import pandas as pd
import urllib3

urllib3.disable_warnings()

token = '87335e5fd1683840a26219417b44b7de'
Host = "t-adata.audit.sinopec.com"
user_account = 'pfjzhang12'
user_name = '%E5%BC%A0%E4%BF%8A%E5%B3%B0'
f_id = 'b08be28cbe03416ebabc998dccad5c01'
f_project_id_ = 'b08be28cbe03416ebabc998dccad5c01'
data_ys = []

header = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "156",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "JSESSIONID=C04EDF0A21DD458A48CD3ED884CE3AA2; _ssoLoginFailed=aHR0cHM6Ly9pMy5zaW5vcGVjLmNvbS9EZXNrdG9wTW9kdWxlcy9TU09BcHAvU1NPTG9naW4uYXNweD9pbnM9YzA4Njc2OTAtZTdkMC00OGRkLWE3ZDItNTIxYjk2Zjg5ZGQ4JnN5cz02MmU3ODIyNS1jNDQzLTQ5MmUtYWU3Zi05MTlmYjMwYmNkYmEmY3VzUGFnZT1odHRwczolMkYlMkZhdWRpdC5zaW5vcGVjLmNvbSUyRkRlc2t0b3BNb2R1bGVzJTJGSW50ZWdyYXRlZE9mZmljZSUyRlN5c1dlYlZpZXclMkZpbmRleC5odG1sJTIzJTJGc3RhdGlzdGljcyY=",
    "Host": Host,
    "Origin": f"https://{Host}",
    "Referer": f"https://{Host}/AData/xssjzx/?token={token}&clientflag=pc&user_name={user_name}&user_account={user_account}",
    # "Sec-Ch-Ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    "Sec-Ch-Ua-Mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}


def post_req(id, project_id_, type):
    if type == "FOLDER":
        return requests.post(
            'https://t-adata.audit.sinopec.com/AData/semantic/classification/getSemanticClassification', data={
                "id": f'{id}',
                "project_id_": f'{project_id_}',
                "type": 'FOLDER',
                "treeClass": '',
                "token": token,
                "clientflag": 'pc',
            }, headers=header, verify=False).json()
    elif type == "MODULE":
        return requests.post(
            'https://t-adata.audit.sinopec.com/AData/semantic/classification/getSemanticClassification', data={
                "id": f'{id}',
                "project_id_": f'{project_id_}',
                "type": 'MODULE',
                "treeClass": '',
                "token": token,
                "clientflag": 'pc',
            }, headers=header, verify=False).json()
    return None


def get_req_pd(id, type):
    url_pd = f'https://t-adata.audit.sinopec.com/AData/dataSourceReference/getReferenceInfoBySemanticElementId?token=87335e5fd1683840a26219417b44b7de&clientflag=pc&id={id}&currPage=1&pageSize=15&refType={type}'
    if type == "CANVAS_REFS":
        return requests.get(url_pd, verify=False).json().get('data')

    elif type == "SEMANTIC_MODEL_REFS":
        return requests.get(url_pd, verify=False).json().get('data')

    elif type == "SEMANTIC_BASIS_REFS":
        return requests.get(url_pd, verify=False).json().get('data')

    return None


def run_data(data):
    if data.get('data'):
        for i in data['data']:
            if i["type_"] == "FOLDER":
                run_data(post_req(i["id_"], i["id_"], i["type_"]))
            elif i["type_"] == "MODULE":
                run_data(post_req(i["id_"], i["id_"], i["type_"]))
            elif i["type_"] == "SEMANTIC_ELEMENT":
                if get_req_pd(i["id_"], 'CANVAS_REFS') != [] or \
                        get_req_pd(i["id_"], 'SEMANTIC_MODEL_REFS') != [] or get_req_pd(i["id_"],
                                                                                        'SEMANTIC_BASIS_REFS') != []:
                    pass
                else:
                    print(f'{i["id_"]}:{i["technology_name_"]}:{i["name_"]}')
                    data_ys.append([f'{i["id_"]}:{i["technology_name_"]}:{i["name_"]}'])
            # time.sleep(0.5)

    else:
        return


run_data(post_req(f_id, f_project_id_, 'FOLDER'))
