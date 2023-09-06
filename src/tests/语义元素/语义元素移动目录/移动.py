import numpy as np
import requests
import pandas as pd
import urllib3

urllib3.disable_warnings()

token = '87335e5fd1683840a26219417b44b7de'
JSESSIONID = '7235FF5A2F81885C9B3371E0D41C1436'
Host = "t-adata.audit.sinopec.com"
user_account = 'pfjzhang12'
user_name = '%E5%BC%A0%E4%BF%8A%E5%B3%B0'

# f_id = 'b08be28cbe03416ebabc998dccad5c01'
# f_project_id_ = 'b08be28cbe03416ebabc998dccad5c01'
# element_type_ = {
#     "ELEMENT_DYNAMIC_DICTIONARY": "01bf9c02e30f40798452edaed71f226f",  # 主数据动态
#     "ELEMENT_DICTIONARY": "294de4b96e1346e4aba651bcb7e3a764",  # 主数据静态
#     "ELEMENT_TIME": "0a3367557258407aa7a38ef8f7b880a3",  # 时间
#     "ELEMENT_CHARACTER": "9e2aaecde2ac468da04fbaf0e9c4dba7",  # 字符串
#     "ELEMENT_METRICS": "c4e5cbe27da74669a74b7c1c4102fe83",  # 度量
# }

f_id = 'd98cdc65b9d54b3a867d7762ab1b12b8'
f_project_id_ = 'd98cdc65b9d54b3a867d7762ab1b12b8'
element_type_ = {
    "ELEMENT_DYNAMIC_DICTIONARY": "ed61a101c2534c3c8a075b9d51fa1284",  # 主数据动态
    "ELEMENT_DICTIONARY": "b4a199ea99864b939e9ff94b97e9ede1",  # 主数据静态
    "ELEMENT_TIME": "4ca4ea9ec5ad4384b9ac9c8d95141118",  # 时间
    "ELEMENT_CHARACTER": "063ae204b1cf4ed0986d52ac53e58611",  # 字符串
    "ELEMENT_METRICS": "083e59f2aa094b549ed11ecafab3ed19",  # 度量
}
header = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "118",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": f"JSESSIONID={JSESSIONID}; _ssoLoginFailed=aHR0cHM6Ly9pMy5zaW5vcGVjLmNvbS9EZXNrdG9wTW9kdWxlcy9TU09BcHAvU1NPTG9naW4uYXNweD9pbnM9YzA4Njc2OTAtZTdkMC00OGRkLWE3ZDItNTIxYjk2Zjg5ZGQ4JnN5cz02MmU3ODIyNS1jNDQzLTQ5MmUtYWU3Zi05MTlmYjMwYmNkYmEmY3VzUGFnZT1odHRwczolMkYlMkZhdWRpdC5zaW5vcGVjLmNvbSUyRkRlc2t0b3BNb2R1bGVzJTJGSW50ZWdyYXRlZE9mZmljZSUyRlN5c1dlYlZpZXclMkY/dmVyPTE0LjAlMjMlMkZzdGF0aXN0aWNz",
    "Host": Host,
    "Origin": f"https://{Host}",
    "Referer": f"https://{Host}/AData/xssjzx/?token={token}&clientflag=pc&user_name={user_name}&user_account={user_account}",
    "Sec-Ch-Ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    "Sec-Ch-Ua-Mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}


def search_semantic(id_):
    r = requests.post(
        'https://t-adata.audit.sinopec.com/AData/semantic/classification/searchSemantic', data={
            "hotkey_": id_,
            "keyword": id_,
            "type_": 'ELEMENT',
            "token": token,
            "clientflag": 'pc',
        },
        headers=header, verify=False).json().get('data')[0]
    if r is not None:
        return element_type_.get(r.get('element_type_'))
    return


def drag_semantic(drag_in_id, curr_move_id):
    r = requests.post(
        'https://t-adata.audit.sinopec.com/AData/semantic/classification/dragSemanticClassification', data={
            "dragInId": drag_in_id,  # 目录ID
            "currMoveId": curr_move_id,  # 语义元素ID
            "type": 'SEMANTIC_ELEMENT',
            "treeClass": "",
            "token": token,
            "clientflag": 'pc',
        },
        headers=header, verify=False)
    app_code = r.json()
    if r.status_code == 200 and app_code.get('appCode') == "1":
        # print(f'{curr_move_id}->{drag_in_id} ok!')
        return

    print(f'{curr_move_id}->{drag_in_id} 失败!')
    return


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
                drag_in_id = search_semantic(i["id_"])
                input(f'{i["id_"]}:{i["technology_name_"]}:{i["name_"]}->{drag_in_id}')
                if drag_in_id:
                    drag_semantic(drag_in_id, i["id_"])
                # if get_req_pd(i["id_"], 'CANVAS_REFS') != [] or \
                #         get_req_pd(i["id_"], 'SEMANTIC_MODEL_REFS') != [] or get_req_pd(i["id_"],
                #                                                                         'SEMANTIC_BASIS_REFS') != []:
                #     pass
                # else:
                #     print(f'{i["id_"]}:{i["technology_name_"]}:{i["name_"]}')

            # time.sleep(0.5)

    else:
        return


run_data(post_req(f_id, f_project_id_, 'MODULE'))
