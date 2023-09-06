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

// $VAR_G0DW_CL_DATE_A0_A0 跳转条件变量
// $G0XZ_KS_DATE_A0_A0 审计期间变量
function calc() {
    var vId = $VAR_G0DW_CL_DATE_A0_A0;
    var vData = $G0XZ_KS_DATE_A0_A0;
    var isNull = function (str) {
        if (str == '') return true;
        var regu = '^[ ]+$';
        var re = new RegExp(regu);
        return re.test(str);
    };
    // 判断&&前面的值，假前真后
    if ((vId == null || vId == '') && (!vData || vData.length < 2 || isNull(vData.join('')))) {
        var vDate = new Date()
        vDate.setMonth(vDate.getMonth() - 0);
        return vDate.format('yyyy-MM-dd');
    } else {
        return '';
    }
}

function calc() {
    var SJQJ_START = new Date()
    SJQJ_ENG = SJQJ_START.setMonth(SJQJ_START.getMonth() - 0);
    return [SJQJ_START.format('yyyy-MM-dd'), SJQJ_ENG.format('yyyy-MM-dd')];
}

function calc() {
    var SJQJ_START = new Date();
    SJQJ_START.setTime(SJQJ_START.getTime() - 365 * 3600 * 1000 * 24 * 3);
    var STATUS = SJQJ_START.format('yyyyMMdd');
    var SJQJ_END = new Date();
    var END = SJQJ_END.format('yyyyMMdd');
    return [STATUS, END];
}
function calc() {
    var SJQJ_START = new Date();
    SJQJ_START.setTime(SJQJ_START.getTime() - 365 * 3600 * 1000 * 24 * 3);
    var STATUS = SJQJ_START.format('yyyyMMdd');
    var SJQJ_END = new Date();
    var END = SJQJ_END.format('yyyyMMdd');
    return [STATUS, END];
}
function calc() {
    var SJQJ_START = new Date();
    SJQJ_START.setTime(SJQJ_START.getTime() - 86400000 * 365 * 3);
    var STATUS = SJQJ_START.format('yyyyMMdd');
    var SJQJ_END = new Date();
    var END = SJQJ_END.format('yyyyMMdd');
    return [STATUS, END];
}
