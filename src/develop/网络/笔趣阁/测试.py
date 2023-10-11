import requests

header = {
    # "Alt-Svc": 'h3=":443"; ma=86400',
    # "Cache-Control": 'max-age=1',
    # "Cf-Cache-Status": 'DYNAMIC',
    # "Cf-Ray": '7e14a1825df1642c-SJC',
    # "Etag": '"63b7f57f-ac78"',
    # "Nel": '{"success_fraction":0,"report_to":"cf-nel","max_age":604800}',
    # "Report-To": '{"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=dGLT%2BFkv4cLT6mgqJ%2BMrULj6p9cHdjvG2sE%2FNM01Z6CU12gxkTUUUKTfGY1AVhRVsSYtOBWbJ3JFw9ZRMpKUfFVwcmLrcotVKmx3e7UjfoiAOc%2FUWEo3dM70lbAA7C0%2Fxpg%3D"}],"group":"cf-nel","max_age":604800}',
    # ":Authority": "www.biququ.info",
    "Cookie": "cf_clearance=IV9s8h.oR6a3NLD8T7gZT.VQWyoChGpbiyusttdFU2g-1683550053-0-160; bcolor=%23FFFFFF; size=10pt; scrollspeed=7",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
}


def get_req():
    url_titel = f'https://www.biququ.info/html/54103/'
    a = requests.get(url_titel, verify=False, headers=header).content
    print(a)


if __name__ == '__main__':
    get_req()
