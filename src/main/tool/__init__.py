# 密码生成
def random_password():
    """密码生成"""

    from rich.console import Console

    console = Console()
    console.print("\n随机生成密码工具开始执行\n密码最多生成100个256位数的密码!", style="bold red")
    num_security = set(input("生成密码格式1.大写字母2.小写字母3.符号4.阿拉伯数字"))
    num_password = input("需要几个密码？请输入数字>>> ")
    num_password_number = input("需要几位数密码？请输入数字>>> ")
    bool_password = True
    while bool_password:
        try:
            num_password = 100 if int(num_password) > 100 else int(num_password)
            num_password_number = 256 if int(num_password_number) > 256 else int(num_password_number)
            bool_password = False
        except Exception as e:
            print("{}", e)

    from random import choice
    from string import ascii_uppercase, ascii_lowercase, punctuation, digits

    dict_password_option = {"1": ascii_uppercase, "2": ascii_lowercase, "3": punctuation, "4": digits, }
    for _ in range(num_password):
        print(
            ''.join(
                [choice(
                    ''.join([''.join([dict_password_option[k] if k in num_security else '']) for k in
                             dict_password_option.keys()])) for _ in range(num_password_number)]))
    console.print("\nend!", style="bold red")


class BasicTool(object):
    """小工具"""

    # 做个决定
    def random_jue_ding(self):
        """做个决定"""
        import random
        jd_inp = input("决定分类：输入数字 1.单个数量的决定；输入数字 2.循环多次的决定")
        if int(jd_inp) == 1 or int(jd_inp) == 2:
            while True:
                str_inp = input("请输入要做的决定并用空格隔开(退出循环直接回车)：")
                if str_inp == "":
                    break
                list_ = list(filter(None, str_inp.split(' ')))
                # list_ = str_inp.split('')
                if int(jd_inp) == 1:
                    print(random.choice(list_))
                elif int(jd_inp) == 2:
                    counter = input('请输入需要循环整数(退出循环直接回车)：')
                    if counter == "":
                        break
                    hashmap = {}
                    for _ in range(int(counter)):
                        key_int = random.randint(0, len(list_) - 1)
                        if hashmap.get(key_int) is not None:
                            hashmap[key_int] += 1
                        elif hashmap.get(key_int) is None:
                            hashmap[key_int] = 1
                    # print(max(hashmap.values()), max(hashmap, key=hashmap.get))
                    print(list_[max(hashmap, key=hashmap.get)])

    # 百家姓
    def bjx(self):
        """百家姓"""
        import re
        a = '''赵钱孙李，周吴郑王。冯陈褚卫，蒋沈韩杨。朱秦尤许，何吕施张。孔曹严华，金魏陶姜。
戚谢邹喻，柏水窦章。云苏潘葛，奚范彭郎。鲁韦昌马，苗凤花方。俞任袁柳，酆鲍史唐。
费廉岑薛，雷贺倪汤。滕殷罗毕，郝邬安常。乐于时傅，皮卞齐康。伍余元卜，顾孟平黄。
和穆萧尹，姚邵湛汪。祁毛禹狄，米贝明臧。计伏成戴，谈宋茅庞。熊纪舒屈，项祝董梁。
杜阮蓝闵，席季麻强。贾路娄危，江童颜郭。梅盛林刁，钟徐邱骆。高夏蔡田，樊胡凌霍。
虞万支柯，昝管卢莫。经房裘缪，干解应宗。丁宣贲邓，郁单杭洪。包诸左石，崔吉钮龚。
程嵇邢滑，裴陆荣翁。荀羊於惠，甄曲家封。芮羿储靳，汲邴糜松。井段富巫，乌焦巴弓。
牧隗山谷，车侯宓蓬。全郗班仰，秋仲伊宫。宁仇栾暴，甘钭厉戎。祖武符刘，景詹束龙。
叶幸司韶，郜黎蓟薄。印宿白怀，蒲邰从鄂。索咸籍赖，卓蔺屠蒙。池乔阴鬱，胥能苍双。
闻莘党翟，谭贡劳逄。姬申扶堵，冉宰郦雍。郤璩桑桂，濮牛寿通。边扈燕冀，郏浦尚农。
温别庄晏，柴瞿阎充。慕连茹习，宦艾鱼容。向古易慎，戈廖庾终。暨居衡步，都耿满弘。
匡国文寇，广禄阙东。欧殳沃利，蔚越夔隆。师巩厍聂，晁勾敖融。冷訾辛阚，那简饶空。
曾毋沙乜，养鞠须丰。巢关蒯相，查后荆红。游竺权逯，盖益桓公。'''

        fx = '''万俟，司马，上官，欧阳，夏侯，诸葛，闻人，东方，
    赫连，皇甫，尉迟，公羊，澹台，公冶，宗政，濮阳，
    淳于，单于，太叔，申屠，公孙，仲孙，轩辕，令狐，
    钟离，宇文，长孙，慕容，鲜于，闾丘，司徒，司空，
    丌官，司寇，仉督，子车，颛孙，端木，巫马，公西，
    漆雕，乐正，壤驷，公良，拓跋，夹谷，宰父，谷梁，
    晋楚，闫法，汝鄢，涂钦，段干，百里，东郭，南门，
    呼延，归海，羊舌，微生，岳帅，缑亢，况郈，有琴，
    梁丘，左丘，东门，西门，商牟，佘佴，伯赏，南宫，
    墨哈，谯笪，年爱，阳佟，第五，言福'''
        # fx_dict = {k: v for k, v in enumerate(fx.replace("\n", "").split("，"))}
        # print(fx_dict)
        print({k: v for k, v in enumerate(re.sub(r'[，。\n]', '', a))})
        print(dict(enumerate(fx.replace('\n', '').split('，'))))
