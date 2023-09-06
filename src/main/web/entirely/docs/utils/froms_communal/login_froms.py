from django import forms


# from django.forms import fields, widgets


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        max_length=18, min_length=6,  # 长度限制
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "用户名"}),
        error_messages={
            "max_length": "用户名长度必须小于18位",
            "min_length": "用户名长度必须大于6位",
            "required": "用户名不能为空",
        }  # 报错信息
    )
    role = forms.ChoiceField(
        required=True,
        choices=(("2", "客户"), ("1", "管理员")),
        widget=forms.Select(attrs={"class": "form-control"})
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "密码"}, render_value=True)
    )


class LoginFormModel(forms.ModelForm):
    role = forms.ChoiceField(
        required=True,
        choices=(("2", "客户"), ("1", "管理员")),
        widget=forms.Select(attrs={"class": "form-control"})
    )
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "用户名"})
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "密码"}, render_value=True)
    )
