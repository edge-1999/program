import numpy as np
import requests
import pandas as pd
import urllib3

urllib3.disable_warnings()

url = 'https://t-adata.audit.sinopec.com/AData/semantic/classification/searchSemantic'
token = '87335e5fd1683840a26219417b44b7de'
JSESSIONID = '27A205326A6DE8D230B9AB6A0DC7C1F7'
Host = "t-adata.audit.sinopec.com"
user_account = 'pfjzhang12'
user_name = '%E5%BC%A0%E4%BF%8A%E5%B3%B0'
filepath = '/Users/li/Downloads/工作簿1.xlsx'
table_name = 'Sheet4'
data = pd.read_excel(filepath, sheet_name=table_name)
header = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "118",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": f"JSESSIONID={JSESSIONID}; username=root; password=q5/rJ9irfO/t7VfQYDIzhZSbFfko0DuQlPFifshE5G2wxPKWXS4NIpwatcA66IUNGOElpUmoHvPZaqHd2u9dKA==; rememberMe=true",
    "Host": Host,
    "Origin": f"https://{Host}",
    "Referer": f"https://{Host}/AData/xssjzx/?token={token}&clientflag=pc&user_name={user_name}&user_account={user_account}",
    "Sec-Ch-Ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    "Sec-Ch-Ua-Mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

data_pd = []

for i in data.values:
    post_data = {
        "hotkey_": f'ELE_{i[0]}',
        "keyword": f'ELE_{i[0]}',
        "type_": 'ELEMENT',
        "token": token,
        "clientflag": 'pc',
    }
    r = requests.post(url, data=post_data, headers=header, verify=False)
    for j in r.json()['data']:
        if j['technology_name_'] == 'ELE_' + i[0]:
            data_pd.append(['ELE_' + i[0], j['element_type_']])

pd.DataFrame(np.array(data_pd)).to_excel('/Users/li/Downloads/工作簿1_out.xlsx', index=False)
