APPLICATIONS_PATH = [
    'applications/learning/natural_science/biology',
    'applications/learning/natural_science/astronomy',
    'applications/provenance/system_settings',
    'applications/provenance/system_function',
    'applications/transaction/economy_industry',
    'applications/transaction/geography_politics',
    'applications/transaction/social_culture/ethnic_population',
]

ZDY_APP_LIST = [
    # 跨域请求
    "corsheaders", "django.contrib.staticfiles", "rest_framework",  # 跨域请求
    # 起源域
    "standard_encoding",  # 标准编码
    "account_management",  # 用户管理
    "menu_management",  # 菜单管理
    "daily_records",  # 日常记录
    "password_records",  # 密码记录
    # 事物域
    "biology",  # 生物学
    "cosmology",  # 天文学
    # 业务域
    "country",  # 国家
    "district",  # 城镇
    "organizations",  # 企业与组织
    "products",  # 产品与服务
    "personal_Information",  # 个人信息
    "ethnic_classification_characteristics",  # 民族分类与特征
]

ZDY_MIDDLEWARES = [
    'docs.utils.middlewares_communal.middlewares.PasswordChangeMiddleware',
    'simplepro.middlewares.SimpleMiddleware',
    # 'simplepro_demo.middlewares.PasswordChangeMiddleware'  # 该中间件用于屏蔽普通用户修改密码功能
]  # 插件中间件

Web_FRAME_OPTIONS = ['DENY', 'SAME' + 'ORIGIN', 'ALLOW-FROM']  # 安全等级从高到低 不允许嵌套｜同一个域名嵌套｜在所有嵌套中显示

IP_ADD_STRING__ = ['*']  # 设置IP访问
FXG_STR = '/'
ADMIN_URL_ZDY = 'admin/'
Templates_PATHNAME_STRING = 'templates'
STATIC_URL_NOT_ZDY = 'docs/static'
# STATIC_URL_NOT_ZDY = 'docs/vue/dist/static'
STATIC_URL_NOT_ZDY_BZ = "/docs/static/"
# STATIC_URL_NOT_ZDY_BZ = "/docs/vue/dist/static/"
MEDIA_URL_NOT_ZDY = 'media'
ZDY_LOGGING_PATH_NAME = 'Log'
ZDY_LOGGING_PATH_Error_NAME = 'Error.log'
ZDY_LOGGING_PATH_INFO_NAME = 'Info.log'
ZDY_LOGGING_PATH_LOG_NAME = 'Log.log'

# SECRET_KEY__ = 'Django-insecure-ag4c!o@V{}_LSY@1999^09|29&{}_{}_{}'
# .format(django.__version__, os.name, sys.platform, platform.platform())
SECRET_KEY__ = 'Django-insecure-ag4c!o@V{}_LSY@1999^09|29&{}_{}_{}'

# session 设置
# SESSION_COOKIE_NAME = "key"  # Session的cookie保存在浏览器上时的key
# SESSION_COOKIE_PATH = "/"  # Session的cookie保存的路径（默认）
# SESSION_COOKIE_DOMAIN = None  # Session的cookie保存的域名（默认）
# SESSION_COOKIE_SECURE = False  # 是否Https传输cookie（默认）
# SESSION_COOKIE_HTTPONLY = True  # 是否Session的cookie只支持http传输（默认）
# SESSION_COOKIE_AGE = 3600  # Session的cookie失效日期（2周）（数字为秒数）（默认）
# SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # 是否关闭浏览器使得Session过期（默认）
# SESSION_SAVE_EVERY_REQUEST = True  # 是否每次请求都保存Session，默认修改之后才保存（默认）
# ESSION_SAVE_EVERY_REQUEST = True 和 SESSION_EXPIRE_AT_BROWSER_CLOSE = True 需同时设置，否则会导致过期时间无法生效

options_date = """
   {
         disabledDate(time) {
           return time.getTime() > Date.now();
         },
         shortcuts: [{
           text: '今天',
           onClick(picker) {
             picker.$emit('pick', new Date());
           }
         }, {
           text: '昨天',
           onClick(picker) {
             const date = new Date();
             date.setTime(date.getTime() - 3600 * 1000 * 24);
             picker.$emit('pick', date);
           }
         }, {
           text: '一周前',
           onClick(picker) {
             const date = new Date();
             date.setTime(date.getTime() - 3600 * 1000 * 24 * 7);
             picker.$emit('pick', date);
           }
         }]
       }
   """
options_date_date = """
{
    shortcuts: [{
        text: '今天',
        onClick(picker) {
            picker.$emit('pick', new Date());
        }
    }, {
        text: '昨天',
        onClick(picker) {
            const date = new Date();
            date.setTime(date.getTime() - 3600 * 1000 * 24);
            picker.$emit('pick', date);
        }
    }, {
        text: '一周前',
        onClick(picker) {
            const date = new Date();
            date.setTime(date.getTime() - 3600 * 1000 * 24 * 7);
            picker.$emit('pick', date);
        }
    }]
}
"""
MYSQL_ENGINE = {
    "DATABASE": "MYSQL",
    "MYSQL_HOST": "0.0.0.0",
    "MYSQL_PORT": 3306,
    "MYSQL_USER": "root",
    "MYSQL_PASSWORD": "li19990929..",
    "MYSQL_DATABASE": "Django1",
    "MYSQL_CHARSET": "utf8",
}
# Mysql_DB = OperationMysqlData(MYSQL_ENGINE)


MEDITOR_DEFAULT_CONFIG = {
    'width': '90%',
    'height': 500,
    'toolbar': ["undo", "redo", "|",
                "bold", "del", "italic", "quote", "ucwords", "uppercase", "lowercase", "|",
                "h1", "h2", "h3", "h5", "h6", "|",
                "list-ul", "list-ol", "hr", "|",
                "link", "reference-link", "image", "code", "preformatted-text", "code-block", "table", "datetime",
                "emoji", "html-entities", "pagebreak", "goto-line", "|",
                "help", "info",
                "||", "preview", "watch", "fullscreen"],
    'upload_image_formats': ["jpg", "JPG", "jpeg", "JPEG", "gif", "GIF", "png",
                             "PNG", "bmp", "BMP", "webp", "WEBP"],
    'image_floder': 'editor',
    'theme': 'default',  # dark / default
    'preview_theme': 'default',  # dark / default
    'editor_theme': 'default',  # pastel-on-dark / default
    'toolbar_autofixed': True,
    'search_replace': True,
    'emoji': True,
    'tex': True,
    'flow_chart': True,
    'sequence': True,
    'language': 'zh'  # zh / en
}
UEDITOR_DEFAULT_CONFIG = {
    'UEDITOR_HOME_URL': '/static/admin/ueditor/',
    'toolbars': [[
        'fullscreen', 'source', '|', 'undo', 'redo', '|',
        'bold', 'italic', 'underline', 'fontborder', 'strikethrough', 'superscript', 'subscript', 'removeformat',
        'formatmatch', 'autotypeset', 'blockquote', 'pasteplain', '|', 'forecolor', 'backcolor', 'insertorderedlist',
        'insertunorderedlist', 'selectall', 'cleardoc', '|',
        'rowspacingtop', 'rowspacingbottom', 'lineheight', '|',
        'customstyle', 'paragraph', 'fontfamily', 'fontsize', '|',
        'directionalityltr', 'directionalityrtl', 'indent', '|',
        'justifyleft', 'justifycenter', 'justifyright', 'justifyjustify', '|', 'touppercase', 'tolowercase', '|',
        'link', 'unlink', 'anchor', '|', 'imagenone', 'imageleft', 'imageright', 'imagecenter', '|',
        'simpleupload', 'insertimage', 'emotion', 'scrawl', 'insertvideo', 'music', 'attachment', 'map', 'gmap',
        'insertframe', 'insertcode', 'webapp', 'pagebreak', 'template', 'background', '|',
        'horizontal', 'date', 'time', 'spechars', 'snapscreen', 'wordimage', '|',
        'inserttable', 'deletetable', 'insertparagraphbeforetable', 'insertrow', 'deleterow', 'insertcol', 'deletecol',
        'mergecells', 'mergeright', 'mergedown', 'splittocells', 'splittorows', 'splittocols', 'charts', '|',
        'print', 'preview', 'searchreplace', 'drafts', 'help'
    ]]
}
