from urllib.parse import urlencode, unquote, quote, urlsplit


class UrlEnDeCode(object):
    def __init__(self, data):
        self.data = data

    @property
    def url_encode_dict(self):
        return urlencode(self.data)

    @property
    def url_unquote_dict(self):
        return unquote(self.data)

    @property
    def url_quote_str(self):
        return quote(self.data, safe=':/?&=')

    @property
    def url_unquote_str(self):
        return unquote(self.data)

    def url_split(self):
        parsed_url = urlsplit(self.data)
        print("Scheme:", parsed_url.scheme)
        print("Netloc:", parsed_url.netloc)
        print("Path:", parsed_url.path)
        print("Query:", parsed_url.query)
