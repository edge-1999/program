class ValidateCreditCode(object):
    def __init__(self, social_credit_code):
        self.error_message = []
        self.valid_char = '0123456789ABCDEFGHJKLMNPQRTUWXY'  # [0-9A-HJ-NP-RT-UW-Y]+
        self.valid_char_not = 'IOZSV'
        self.social_credit_code = social_credit_code.upper()
        self.check_mark_handle = self.handle_social_credit_code
        self.check_mark_length = self.check_length
        self.modulus = 31
        self.registration_management_department_code_1 = {
            '1': '机构编制', '2': '外交', '3': '司法行政', '4': '文化', '5': '民政', '6': '旅游',
            '7': '宗教', '8': '工会', '9': '工商|市场监管', 'A': '中央军委改革和编制办公室', 'N': '农业', 'Y': '其他'}
        self.registration_management_department_code_type_2 = {
            '1': {'1': '机关', '2': '事业单位', '3': '编办直接管理机构编制的群众团体', '9': '其他'},
            '2': {'1': '外国常驻新闻机构', '9': '其他'},
            '3': {'1': '律师执业机构', '2': '公证处', '3': '基层法律服务所', '4': '司法鉴定机构', '5': '仲裁委员会',
                  '9': '其他'},
            '4': {'1': '外国在华文化中心', '9': '其他'},
            '5': {'1': '社会团体', '2': '民办非企业单位', '3': '基金会', '9': '其他'},
            '6': {'1': '外国旅游部门常驻代表机构', '2': '港澳台地区旅游部门常驻内地（大陆）代表机构', '9': '其他'},
            '7': {'1': '宗教活动场所', '2': '宗教院校', '9': '其他'},
            '8': {'1': '基层工会', '9': '其他'},
            '9': {'1': '企业', '2': '个体工商户', '3': '农民专业合作社'},
            'A': {'1': '军队事业单位', '9': '其他'},
            'N': {'1': '组级集体经济组织', '2': '村级集体经济组织', '3': '乡镇级集体经济组织', '9': '其他'},
            'Y': {'1': '统一'}
        }
        self.top_two = self.check_top_two
        self.wi = [1, 3, 9, 27, 19, 26, 16, 17, 20, 29, 25, 13, 8, 24, 10, 30, 28]
        self.cores_value = {
            '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10,
            'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'J': 18, 'K': 19, 'L': 20,
            'M': 21, 'N': 22, 'P': 23, 'Q': 24, 'R': 25, 'T': 26, 'U': 27, 'W': 28, 'X': 29, 'Y': 30
        }
        self.check_mark_eighteen = self.check_eighteen

    @property
    def handle_social_credit_code(self):
        import re

        self.social_credit_code = ''.join(re.findall(r'[{}]+'.format(self.valid_char), self.social_credit_code))
        return True

    @property
    def check_length(self):
        if len(self.social_credit_code) == 18:
            return True
        else:
            self.error_message.append('字符串长度不等于18位')
            return False

    @property
    def check_top_two(self):
        top_two = []
        for k, v in self.registration_management_department_code_type_2.items():
            for k_s, _ in v.items():
                top_two.append('{}{}'.format(k, k_s))
        return '|'.join(top_two)

    @property
    def check_eighteen(self):
        ci = []
        for v in self.social_credit_code[0:17]:
            j = self.cores_value.get(v)
            ci.append(j)
        ci_wi = []
        for i in range(len(ci)):
            ci_wi.append(ci[i] * self.wi[i])
        ci_wi_sum = sum(ci_wi)
        c18 = self.modulus - ci_wi_sum % self.modulus
        if c18 == self.modulus:
            c18 = 0
        check_code = None
        for k, v in self.cores_value.items():
            if v == c18:
                check_code = k
                break
        if check_code == self.social_credit_code[17]:
            return True
        return False


def validate_credit_code(code):
    # 检查长度是否为18位
    if len(code) != 18:
        return False

    # 基本字符验证
    for char in code:
        if not char.isalnum():
            return False

    # 加权因子
    weights = [1, 3, 9, 27, 19, 26, 16, 17, 20, 29, 25, 13, 8, 24, 10, 30, 28]

    # 校验码字符集
    check_codes = "0123456789ABCDEFGHJKLMNPQRTUWXY"

    # 计算校验位
    total = 0
    for i in range(17):
        char = code[i]
        weight = weights[i]
        if '0' <= char <= '9':
            total += (ord(char) - ord('0')) * weight
        else:
            total += (ord(char) - ord('A') + 10) * weight

    check_code_index = total % 31

    # 验证校验位
    if code[17] != check_codes[check_code_index]:
        return False

    return True
