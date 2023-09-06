import re
from decimal import Decimal, getcontext


def celsius_to_fahrenheit(celsius):
    return f"{(Decimal(celsius) * Decimal('9') / Decimal('5')) + Decimal('32')}"


def fahrenheit_to_celsius(fahrenheit):
    return f"{(Decimal(fahrenheit) - Decimal('32')) * Decimal('5') / Decimal('9')}"


def fahrenheit_celsius(
        judgment_data, centigrade_unit=None, fahrenheit_unit=None, else_unit=None, numerical_not_unit=None) -> tuple:
    """
    judgment_data = ""  # 处理的数据
    centigrade_unit = ["C", "℃", "c"]  # 摄氏度单位
    fahrenheit_unit = ["F", "℉", "f"]  # 华氏度单位
    else_unit = ['°']  # 其他公用单位
    numerical_not_unit = 1 or 2 or else  # 只匹配到数字没有单位时，当前数据表示为：1=摄氏度 2=华氏度 其余的代表不处理，默认为不处理
    """
    getcontext().prec = 28
    unit = {
        "centigrade_unit_default": ["C", "℃", "c"],
        "fahrenheit_unit_default": ["F", "℉", "f"],
        "else_unit_default": ['°'],
    }

    centigrade_unit = list(set(centigrade_unit + unit["centigrade_unit_default"])) \
        if isinstance(centigrade_unit, list) and centigrade_unit else unit["centigrade_unit_default"]
    fahrenheit_unit = list(set(fahrenheit_unit + unit["fahrenheit_unit_default"])) \
        if isinstance(fahrenheit_unit, list) and fahrenheit_unit else unit["fahrenheit_unit_default"]
    else_unit = list(set(else_unit + unit["else_unit_default"])) \
        if isinstance(else_unit, list) and else_unit else unit["else_unit_default"]

    re_unit = ''.join(centigrade_unit + fahrenheit_unit)
    re_unit_else = ''.join(else_unit)
    scale = re.search(
        f"[-+]?\d+\.\d+[{re_unit_else}]?[{re_unit}]?|[-+]?\d+[{re_unit_else}]?[{re_unit}]?", judgment_data)
    del re_unit

    if scale:
        processing_data = re.sub(f"[{re_unit_else}]+", "", scale.group())
        del re_unit_else
        if processing_data[-1] in centigrade_unit:
            return processing_data[:-1], celsius_to_fahrenheit(processing_data[:-1])
        elif processing_data[-1] in fahrenheit_unit:
            return processing_data[:-1], fahrenheit_to_celsius(processing_data[:-1])

        if numerical_not_unit == "1":
            return processing_data, celsius_to_fahrenheit(processing_data)
        elif numerical_not_unit == "2":
            return processing_data, fahrenheit_to_celsius(processing_data)
        return None, None
    return None, None
