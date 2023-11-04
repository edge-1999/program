export KRB5_CONFIG=/Users/Shared/MyWork/Pcitc/data/个人相关/公司账户/hadoop/通用文件/krb5.ini
export KRB5CCNAME=/Users/Shared/MyWork/Pcitc/data/个人相关/公司账户/hadoop/通用文件/krb5cache
function work_pcitc() {
    kinit -kt /Users/Shared/MyWork/Pcitc/data/项目管理/茂名石化审计大数据建设项目/3.实施/2.逻辑专区/3.模型设计开发/audit-big-data-mmsh/_00_lijd016_test/_lijd7016_env/sjfw_lijd7016.keytab sjfw_lijd7016
}
