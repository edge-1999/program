/*
PLANSTORE（实施库、投用库）投资项目(投资)

立项信息(投资)
    MS_XMZLK（技改项目立项）

基础设计委托(投资)
    MS_WTSJ(委托设计)

设计审查(投资)
    U_PRO_WTSJ_BGSC（设计报告审查）

零星技措申请记录(投资)
    PL_LXJC_NOTICE（零星技措申请查询）
    PL_LXJC_DETAIL（零星技措项目明细）
    INVESTCOMPLETE_TECH（限上、限下、一般技改、零星及零购、社区配套项目）

涉密文件申请记录(投资)
    MS_SECRETPROREPORT_SQ（涉密文件申请记录）
    sa_task(审批处理表)
提前实施申请记录(投资)
    PL_FILE （提前实施申请查询）
    sa_task(审批处理表)

设备/物资超概(投资)
    T_CO_XMXX(项目信息)

可研委托(投资)
    MS_WTSJ(委托设计)
    sa_task(审批处理表)

勘察/详设委托(投资)

方案委托(投资)


select commdictionary.FID               AS "字典表主键"
     , commdictionary.DIC_CODE          AS "字典表字典编码"
     , commdictionary.DIC_NAME          AS "字典表字典名称"
     , commdictionary.DIC_TYPE          AS "字典表字典类型"
     , commdictionarydetail.FID         AS "字典详情表主键"
     , commdictionarydetail.DIC_CODE    AS "字典详情表字典编码"
     , commdictionarydetail.DETAIL_NAME AS "字典详情表字典明细名称"
     , commdictionarydetail.FBMCODE     AS "字典详情表字典明细编码"
     , commdictionarydetail.DETAI_EXT1  AS "字典详情表扩展"
from RAW_TZGL.COMM_DICTIONARY commdictionary -- 数据字典主表
         full join RAW_TZGL.COMM_DICTIONARY_DETAIL commdictionarydetail
                    on commdictionary.FID = commdictionarydetail.DIC_CODE
where commdictionary.FISFLAG is null
  and commdictionarydetail.ISFALG = '0'


RAW_TZGL.INVESTCOMPLETE_TECH  -- 限上、限下、一般技改、零星及零购、社区配套项目
RAW_TZGL.PLANSTORE  -- 实施库、投用库
RAW_TZGL.U_PRO_WTSJ_BGSC  -- 设计报告审查
RAW_TZGL.PL_FILE  -- 报告申请
RAW_TZGL.T_CO_XMXX  -- 项目信息
RAW_TZGL.MS_WTSJ  -- 委托设计
RAW_TZGL.MS_XMZLK  -- 技改项目立项
RAW_TZGL.PL_LXJC_NOTICE  -- 零星技措申请查询
RAW_TZGL.PL_LXJC_DETAIL  -- 零星技措项目明细
RAW_TZGL.MS_SECRETPROREPORT_SQ  -- 涉密文件申请记录
RAW_TZGL.SA_TASK  -- 审批处理表


PLANSTORE（实施库、投用库）
*/


SELECT OWNER
     , TABLE_NAME
FROM all_tables
where OWNER = 'RAW_TZGL';
SELECT c.column_name                                             AS "字段",
       cc.comments                                               AS "字段描述",
       c.data_type                                               AS "字段类型",
       CASE WHEN pk.column_name IS NOT NULL THEN 'X' ELSE '' END AS "是否主键",
       c.nullable                                                AS "是否为空",
       c.data_length                                             AS "长度",
       c.data_precision                                          AS "精度"
FROM all_tab_columns c
         LEFT JOIN all_col_comments cc
                   ON c.owner = cc.owner AND c.table_name = cc.table_name AND c.column_name = cc.column_name
         LEFT JOIN (SELECT acc.owner, acc.table_name, acc.column_name
                    FROM all_constraints ac
                             JOIN all_cons_columns acc
                                  ON ac.owner = acc.owner AND ac.constraint_name = acc.constraint_name
                    WHERE ac.constraint_type = 'P') pk
                   ON c.owner = pk.owner AND c.table_name = pk.table_name AND c.column_name = pk.column_name
WHERE c.owner = 'RAW_TZGL'
  AND c.table_name = 'PLANSTORE'
ORDER BY c.column_id;

select TO_CHAR(SYSDATE, 'YYYY-MM-DD HH24:MI:SS') || ' 查询表计数为：1356941' || count(1) AS "数量"
from RAW_TZGL.PLANSTORE;

select coxmxx.FID                                           AS "主键"
     , coxmxx.VERSION                                       AS "版本"
     , coxmxx.FCREATEDEPTID                                 AS "提交部门标识"
     , coxmxx.FCREATEDEPTNAME                               AS "提交部门"
     , coxmxx.FCREATEPSNID                                  AS "提交人员标识"
     , coxmxx.FCREATEPSNNAME                                AS "提交人员"
     , coxmxx.FCREATEPSNFID                                 AS "提交人员路径标识"
     , coxmxx.FCREATEPSNFNAME                               AS "提交人员路径名称"
     , TO_CHAR(coxmxx.FCREATETIME, 'YYYY-MM-DD HH24:MI:SS') AS "提交时间"
     , coxmxx.FXMID                                         AS "项目标识"
     , coxmxx.FXMMC                                         AS "项目名称"
     , ROUND(coxmxx.FKYPFGSWY * 10000, 2)                   AS "可研批复概算（万元）"
     , coxmxx.FTBDW                                         AS "填报单位"
     , TO_CHAR(coxmxx.FTBRQ, 'YYYY-MM-DD HH24:MI:SS')       AS "填报日期"
     , coxmxx.FCGYYFX                                       AS "超概原因分析"
     , coxmxx.FYCQCSJXG                                     AS "已采取措施及效果"
     , coxmxx.FJYCLCS                                       AS "建议处理措施"
     , TO_CHAR(coxmxx.FJSSJ, 'YYYY-MM-DD HH24:MI:SS')       AS "建设时间"
     , coxmxx.FYXDJH                                        AS "已下达计划"
     , coxmxx.FYDGS                                         AS "原定概算"
     , coxmxx.FSSGS                                         AS "实施概算"
     , coxmxx.FDZFD                                         AS "调整幅度"
     , coxmxx.FJHGKBM                                       AS "计划归口部门"
     , coxmxx.FXMJSNR                                       AS "项目建设内容"
     , coxmxx.FXMYQXG                                       AS "项目预期效果"
     , coxmxx.FXMGSDZYYFXYJHFF                              AS "项目概算调整原因分析依据和方法"
     , coxmxx.FSJXMFZR                                      AS "设计项目负责人"
     , coxmxx.FWBSH                                         AS "WBS号"
     , coxmxx.FHTH                                          AS "合同号"
     , ROUND(coxmxx.FHTJWYA * 10000, 2)                     AS "合同价万元A"
     , coxmxx.FPROCODE                                      AS "项目编码"
--      , coxmxx.FPROTYPE                                      AS "项目类型编码"
     , coxmxx.FPROTYPENAME                                  AS "项目类型编码描述"
from RAW_TZGL.T_CO_XMXX coxmxx

select planstore.FID                    AS "主键"
     , planstore.FPROID                 AS "项目主键"
     , planstore.FPRONAME               AS "选择项目时，根据投资分类过滤"
     , planstore.FPROISSTOCK            AS "项目归属炼油化工存续"
     , planstore.FPROCODE               AS "项目编码"
     , planstore.FPROYEARSCOPE          AS "建设年限"
     , planstore.FTOTALCOST             AS "总投资"
     , planstore.FPLANTOTALCOST         AS "建议投资"
     , planstore.FBATCHCOST             AS "批准投资"
     , planstore.FLXLY                  AS "立项理由"
     , planstore.FAUTHPAPERNO           AS "审批文号"
     , planstore.FLOAN                  AS "贷款"
     , planstore.FACTUALSCHEDULE        AS "实际投用"
--      , planstore.PROSTATUS              AS "状态"
     , commdictionarydetail.DETAIL_NAME AS "状态"
from RAW_TZGL.PLANSTORE planstore
         left join RAW_TZGL.COMM_DICTIONARY_DETAIL commdictionarydetail
                   on planstore.PROSTATUS = commdictionarydetail.FID


-- where (coxmxx.FHTJWYA <> ''
--     OR coxmxx.FHTJWYA IS NOT NULL)
--   AND ROWNUM <= 10;

select count(1)
from RAW_TZGL.T_CO_XMXX coxmxx
         left join RAW_TZGL.PLANSTORE planstore
                   on coxmxx.FXMID = planstore.FPROID

select FXMID AS "项目标识"
     , count(1)
from RAW_TZGL.T_CO_XMXX coxmxx
group by FXMID
having count(1) > 1

select coxmxx.FID                                           AS "主键"
     , coxmxx.VERSION                                       AS "版本"
     , coxmxx.FCREATEDEPTID                                 AS "提交部门标识"
     , coxmxx.FCREATEDEPTNAME                               AS "提交部门"
     , coxmxx.FCREATEPSNID                                  AS "提交人员标识"
     , coxmxx.FCREATEPSNNAME                                AS "提交人员"
     , coxmxx.FCREATEPSNFID                                 AS "提交人员路径标识"
     , coxmxx.FCREATEPSNFNAME                               AS "提交人员路径名称"
     , TO_CHAR(coxmxx.FCREATETIME, 'YYYY-MM-DD HH24:MI:SS') AS "提交时间"
     , coxmxx.FXMID                                         AS "项目标识"
     , coxmxx.FXMMC                                         AS "项目名称"
     , ROUND(coxmxx.FKYPFGSWY * 10000, 2)                   AS "可研批复概算（万元）"
     , coxmxx.FTBDW                                         AS "填报单位"
     , TO_CHAR(coxmxx.FTBRQ, 'YYYY-MM-DD HH24:MI:SS')       AS "填报日期"
     , coxmxx.FCGYYFX                                       AS "超概原因分析"
     , coxmxx.FYCQCSJXG                                     AS "已采取措施及效果"
     , coxmxx.FJYCLCS                                       AS "建议处理措施"
     , TO_CHAR(coxmxx.FJSSJ, 'YYYY-MM-DD HH24:MI:SS')       AS "建设时间"
     , coxmxx.FYXDJH                                        AS "已下达计划"
     , coxmxx.FYDGS                                         AS "原定概算"
     , coxmxx.FSSGS                                         AS "实施概算"
     , coxmxx.FDZFD                                         AS "调整幅度"
     , coxmxx.FJHGKBM                                       AS "计划归口部门"
     , coxmxx.FXMJSNR                                       AS "项目建设内容"
     , coxmxx.FXMYQXG                                       AS "项目预期效果"
     , coxmxx.FXMGSDZYYFXYJHFF                              AS "项目概算调整原因分析依据和方法"
     , coxmxx.FSJXMFZR                                      AS "设计项目负责人"
     , coxmxx.FWBSH                                         AS "WBS号"
     , coxmxx.FHTH                                          AS "合同号"
     , ROUND(coxmxx.FHTJWYA * 10000, 2)                     AS "合同价万元A"
     , coxmxx.FPROCODE                                      AS "项目编码"
--      , coxmxx.FPROTYPE                                      AS "项目类型编码"
     , coxmxx.FPROTYPENAME                                  AS "项目类型编码描述"
from RAW_TZGL.T_CO_XMXX coxmxx
where coxmxx.FXMID = 'E5199A7C3CD445E9AD800D1DFD6DA5FF'

select FXMID    AS "项目标识"
     , FWBSH    AS "WBS号"
     , FPROCODE AS "项目编码"
from RAW_TZGL.T_CO_XMXX coxmxx
group by FXMID



select planstore.FPROID
from RAW_TZGL.PLANSTORE planstore
group by planstore.FPROID
having count(1) > 1


select planstore.FPROID                                     AS "项目主键"
     , planstore.FPRONAME                                   AS "选择项目时，根据投资分类过滤"
     , planstore.FPROISSTOCK                                AS "项目归属炼油化工存续"
     , planstore.FPROCODE                                   AS "项目编码"
     , planstore.FPROYEARSCOPE                              AS "建设年限"
     , planstore.FTOTALCOST                                 AS "总投资"
     , planstore.FPLANTOTALCOST                             AS "建议投资"
     , planstore.FBATCHCOST                                 AS "批准投资"
     , planstore.FLXLY                                      AS "立项理由"
     , planstore.FAUTHPAPERNO                               AS "审批文号"
     , planstore.FLOAN                                      AS "贷款"
     , planstore.FACTUALSCHEDULE                            AS "实际投用"
--      , planstore.PROSTATUS              AS "状态"
     , commdictionarydetail.DETAIL_NAME                     AS "项目状态"
     , coxmxx.FID                                           AS "主键"
     , coxmxx.VERSION                                       AS "版本"
     , coxmxx.FCREATEDEPTID                                 AS "提交部门标识"
     , coxmxx.FCREATEDEPTNAME                               AS "提交部门"
     , coxmxx.FCREATEPSNID                                  AS "提交人员标识"
     , coxmxx.FCREATEPSNNAME                                AS "提交人员"
     , coxmxx.FCREATEPSNFID                                 AS "提交人员路径标识"
     , coxmxx.FCREATEPSNFNAME                               AS "提交人员路径名称"
     , TO_CHAR(coxmxx.FCREATETIME, 'YYYY-MM-DD HH24:MI:SS') AS "提交时间"
     , coxmxx.FXMID                                         AS "项目标识"
     , coxmxx.FXMMC                                         AS "项目名称"
     , ROUND(coxmxx.FKYPFGSWY * 10000, 2)                   AS "可研批复概算（万元）"
     , coxmxx.FTBDW                                         AS "填报单位"
     , TO_CHAR(coxmxx.FTBRQ, 'YYYY-MM-DD HH24:MI:SS')       AS "填报日期"
     , coxmxx.FCGYYFX                                       AS "超概原因分析"
     , coxmxx.FYCQCSJXG                                     AS "已采取措施及效果"
     , coxmxx.FJYCLCS                                       AS "建议处理措施"
     , TO_CHAR(coxmxx.FJSSJ, 'YYYY-MM-DD HH24:MI:SS')       AS "建设时间"
     , coxmxx.FYXDJH                                        AS "已下达计划"
     , coxmxx.FYDGS                                         AS "原定概算"
     , coxmxx.FSSGS                                         AS "实施概算"
     , coxmxx.FDZFD                                         AS "调整幅度"
     , coxmxx.FJHGKBM                                       AS "计划归口部门"
     , coxmxx.FXMJSNR                                       AS "项目建设内容"
     , coxmxx.FXMYQXG                                       AS "项目预期效果"
     , coxmxx.FXMGSDZYYFXYJHFF                              AS "项目概算调整原因分析依据和方法"
     , coxmxx.FSJXMFZR                                      AS "设计项目负责人"
     , coxmxx.FWBSH                                         AS "WBS号"
     , coxmxx.FHTH                                          AS "合同号"
     , ROUND(coxmxx.FHTJWYA * 10000, 2)                     AS "合同价万元A"
     , coxmxx.FPROCODE                                      AS "项目编码"
--      , coxmxx.FPROTYPE                                      AS "项目类型编码"
     , coxmxx.FPROTYPENAME                                  AS "项目类型编码描述"
from RAW_TZGL.PLANSTORE planstore
         left join RAW_TZGL.COMM_DICTIONARY_DETAIL commdictionarydetail
                   on planstore.PROSTATUS = commdictionarydetail.FID
         left join RAW_TZGL.T_CO_XMXX coxmxx on planstore.FPROID = coxmxx.FXMID
where planstore.FPROID in (select planstore.FPROID
                           from RAW_TZGL.PLANSTORE planstore
                           group by planstore.FPROID
                           having count(1) > 1)


select FPROID, coount(1)
from RAW_TZGL.MS_WTSJ mswtsj
group by FPROID
having count(1) > 1

select FXMID, count(1)
from RAW_TZGL.MS_WTSJ mswtsj
group by FXMID
having count(1) > 1

select *
from RAW_TZGL.MS_XMZLK
where FID not in (select FPROID from RAW_TZGL.PLANSTORE planstore)


select count(1)
from RAW_TZGL.T_CO_XMXX coxmxx
where coxmxx.FXMID not in (select FID
                               from RAW_TZGL.MS_XMZLK)


select count(1)
from RAW_TZGL.MS_WTSJ mswtsj
where FXMID not in (select FID from RAW_TZGL.MS_XMZLK)


select PROCODE, count(1)
from RAW_TZGL.MS_XMZLK
group by PROCODE
having count(1) > 1

select *
from RAW_TZGL.MS_XMZLK
where PROCODE = 'MPAC1900063D86'


select FMC           AS "项目名称"
     , FXZ           AS "项目属性"
     , PROCODE       AS "项目编码"
     , FFL           AS "项目分类"
     , PROSTATUS     AS "项目状态"
     , PROPLANSTATUS AS "计划状态"
     , PROPHASE      AS "项目阶段"
     , DEL_FLAG      AS "是否删除"
from RAW_TZGL.MS_XMZLK
where PROCODE = 'MPAC1900063D86'

select *
from RAW_TZGL.PLANSTORE
where FPROCODE='MPAC1900063D86'



select xmmain.FID                                                     AS "项目标识"
     , CASE
           WHEN length(msxmzlk.PROCODE) > 1 THEN msxmzlk.PROCODE
           WHEN length(planstore.FPROCODE) > 1 THEN planstore.FPROCODE
           ELSE '' END                                                AS "项目编号"
     , COALESCE(msxmzlk.FMC, planstore.FPRONAME)                      AS "项目名称"
     , COALESCE(msxmzlk.VERSION, planstore.VERSION)                   AS "版本"
     , COALESCE(msxmzlk.PROSTATUS, planstore.PROSTATUS)               AS "项目状态"  -- 关联语义元素 -字典表
     , CASE
           WHEN length(msxmzlk.FJSNX) >= 4 THEN SUBSTR(TO_CHAR(msxmzlk.FJSNX), 1, 4)
           WHEN length(planstore.FPROYEARSCOPE) >= 4 THEN SUBSTR(TO_CHAR(planstore.FPROYEARSCOPE), 1, 4)
           ELSE '' END                                                AS "建设年限"
     , ROUND(COALESCE(msxmzlk.FZTZ, planstore.FTOTALCOST) * 10000, 2) AS "总投资"
     , msxmzlk.FXZ                                                    AS "项目属性"  -- 不知道码值描述
     , msxmzlk.FFL                                                    AS "项目分类"  -- 不知道码值描述
     , msxmzlk.PROPLANSTATUS                                          AS "计划状态"
     , msxmzlk.FSQDW                                                  AS "申请单位"
     , msxmzlk.PQXMFATCR                                              AS "项目方案提出人"
     , msxmzlk.PQZGBMFAFZR                                            AS "主管方案负责人"
     , msxmzlk.PQGSZYZGMBFZR                                          AS "主管部门负责人"
     , msxmzlk.FPLANTIME                                              AS "计划时间"
     , msxmzlk.FDOTIME                                                AS "完成时间"
     , msxmzlk.FFYFL                                                  AS "费用分类"
     , msxmzlk.PROPHASE                                               AS "项目阶段"  -- 关联语义元素 -字典表
     , msxmzlk.FFATCR                                                 AS "方案提出人"
     , msxmzlk.FFAFZR                                                 AS "方案负责人"
     , msxmzlk.FEJDWFAFZR                                             AS "二级单位负责人"
     , msxmzlk.FTBSJ                                                  AS "填报时间"
     , msxmzlk.DEL_FLAG                                               AS "是否删除"
     , msxmzlk.FCREATEOGNID                                           AS "创建组织ID"
     , msxmzlk.FCREATEOGNNAME                                         AS "提交机构名称"
     , msxmzlk.FCREATEDEPTID                                          AS "提交部门ID"
     , msxmzlk.FCREATEDEPTNAME                                        AS "提交部门"
     , msxmzlk.FCREATEPOSID                                           AS "提交岗位ID"
     , msxmzlk.FCREATEPOSNAME                                         AS "提交岗位名"
     , msxmzlk.FCREATEPSNID                                           AS "提交人员ID"
     , msxmzlk.FCREATEPSNNAME                                         AS "提交人员"
     , msxmzlk.FCREATEPSNFID                                          AS "提交人员全ID"
     , msxmzlk.FCREATEPSNFNAME                                        AS "提交人全名"
     , msxmzlk.FCREATETIME                                            AS "提交时间"
     , COALESCE(msxmzlk.PROLSSTOCK, planstore.FPROISSTOCK)            AS "项目归属"  -- 关联语义元素 -字典表
     , msxmzlk.ZBCODE                                                 AS "总部编码"
     , msxmzlk.UPBELONGLOCA                                           AS "项目属地"
     , msxmzlk.UPBUILDSTART                                           AS "建设开始日期"
     , msxmzlk.UPBUILDEND                                             AS "建设结束日期"
     , msxmzlk.UPLENGTH                                               AS "建设周期"
     , ROUND(msxmzlk.JSTZ * 10000, 2)                                 AS "建设投资"
     , planstore.FXZ                                                  AS "建设性质"  -- 关联语义元素 -字典表
     , ROUND(planstore.FPLANTOTALCOST * 10000, 2)                     AS "建议投资"
     , ROUND(planstore.FBATCHCOST * 10000, 2)                         AS "批准投资"
     , planstore.FDUTYCOMPANY                                         AS "责任单位"
     , planstore.FDUTYLEADER                                          AS "责任领导"
     , planstore.FDUTYDEPT                                            AS "责任部门"
     , CASE WHEN msxmzlk.FID is not null THEN '是' else '' end        AS "是否立项"
from (select FPROID AS "FID" from RAW_TZGL.PLANSTORE union select FID AS "FID" from RAW_TZGL.MS_XMZLK) xmmain
         left join RAW_TZGL.MS_XMZLK msxmzlk on xmmain.FID = msxmzlk.FID
         left join RAW_TZGL.PLANSTORE planstore on xmmain.FID = planstore.FPROID
