select DATA_ID   AS "DATA_ID"
     , DOC_ID    AS "单据内码"
     , ASSET_NO  AS "资产编号"
     , ASSET_NO2 AS "资产编号2"
     , TXT50     AS "资产名称"
     , ANLUE     AS "使用单位"
from RAW_ZCGL.AM_VALUEAD_ASSET_ITEM
where rownum <= 10;

select ASSETID AS "资产内码"
from RAW_ZCGL.CK_WS_ITEM -- 清查底稿行项目
where rownum <= 10;

select *
from RAW_ZCGL.AMSAP_ANLA
where ANLN1 in (select ANLN1 from RAW_ZCGL.AMSAP_ANLA group by ANLN1 having count(1) > 1)
ORDER BY ANLN1;

select count(1) -- 10（异常）
from RAW_ZCGL.AMSAP_ANLA
where XJRYID not in (select F_ID from RAW_LTX.ODS_BC_XJ_PEOPLEINFO)


select count(1) -- 10（异常）
from RAW_LTX.ODS_TWORISKSHELPSENDDETAIL
where XJRYID not in (select F_ID from RAW_LTX.ODS_BC_XJ_PEOPLEINFO)


select count(1) -- 11 异常
from (select ANLN1, ANLN2, TXT50, USEDEPT_NO
      from RAW_ZCGL.AMSAP_ANLA
      group by ANLN1, ANLN2, TXT50, USEDEPT_NO
      having count(1) > 1);

select DISTINCT a.WO_NO
from JWXXT.YJS_WORKORDER_TB a -- 项目
         inner join JWXXT.YJS_WP_WORKORDER_TB b -- 关联
                    on a.WO_ID = b.WO_ID
         inner join jwxxt.YJS_WPINF_TB c -- 工序
                    on b.WPINF_ID = c.WPINF_ID
         inner join JWXXT.YJS_ERP_WORKORDER_TB d --ERP
                    on c.WO_NO = d.WO_NO
         inner join JWXXT.YJS_JWRWWTS_TB e
                    on d.WO_NO = e.ERP_NO
where a.WO_ORDERTIME between to_date('2015-01-01', 'yyyy-MM-dd') and to_date('2023-06-01', 'yyyy-MM-dd')

-- pyinstaller --onefile your_script.py


select DISTINCT a.WO_NO        as "项目号",
                a.WO_DESCRIBE  as "项目名称",
                a.WO_ORDERTIME as "项目下达时间",
                a.WO_SFYS      as "是否预算项目",
                a.WO_XMXZ      as "项目性质",
                a.WO_VERSION   as "版本号",
                a.FUN_PLACE    as "功能位置",
                a.FUN_DESCRIBE as "功能位置描述",
                a.WO_CREATER   as "创建人",
                a.WO_GRPNAME   as "计划员组描述",
                a.PROVIDER_NO  as "工作中心代码",
                a.WO_YWFWDM    as "业务范围",
                a.WO_CBZX_NO   as "成本中心编码",
                a.WO_CBZX      as "成本中心描述",
                a.WO_SFXD      as "是否下达",
                a.FQ_REASON    as "废弃原因",
                a.FQ_USER      as "废弃人",
                a.FQ_TIME      as "废弃时间"
from JWXXT.YJS_WORKORDER_TB a -- 项目

select distinct a.WO_NO                                       as "项目号",
                a.WO_DESCRIBE                                 as "项目名称",
                a.WO_ORDERTIME                                as "项目下达时间",
                CASE
                    WHEN a.WO_SFYS = 0 THEN '非预算'
                    WHEN a.WO_SFYS = 1 THEN '预算'
                    else cast(a.WO_SFYS as VARCHAR) end       as "是否预算项目",
                CASE
                    WHEN a.WO_XMXZ = 1 THEN '月度维修项目'
                    WHEN a.WO_XMXZ = 2 THEN '装置大修项目'
                    WHEN a.WO_XMXZ = 3 THEN '投资类费用性项目'
                    WHEN a.WO_XMXZ = 4 THEN '保运(年度框架合同)'
                    else cast(a.WO_SFYS as VARCHAR) end       as "项目性质",
                d.WO_VERSION                                  as "版本号",
                a.FUN_PLACE                                   as "功能位置",
                a.FUN_DESCRIBE                                as "功能位置描述",
                a.WO_CREATER                                  as "创建人",
                a.WO_GRPNAME                                  as "计划员组描述",
                a.PROVIDER_NO                                 as "工作中心代码",
                a.PROVIDER_NAME                               as "工作中心",
                f.HT_XDRBM                                    AS "供应商简称",
                f.HT_XDRMC                                    AS "供应商编号",
                CASE
                    WHEN f.HT_SJLY = 1 THEN '股份'
                    WHEN f.HT_SJLY = 2 THEN '存续'
                    else cast(f.HT_SJLY as VARCHAR) end       as "项目属性",
                ''                                            AS "备注",         -- 查找
                a.WO_YWFWDM                                   as "业务范围",
                a.WO_CBZX_NO                                  as "成本中心编码",
                a.WO_CBZX                                     as "成本中心描述",
                ''                                            AS "项目进展情况", -- 查找
                CASE
                    WHEN a.WO_SFXD = 0 THEN '下达'
                    WHEN a.WO_SFXD = 1 THEN '未下达'
                    else cast(a.WO_SFYS as VARCHAR) end       as "是否下达",
                a.WO_CONTRACTNO                               as "合同号",
                CASE
                    WHEN a.WO_CONTRACTXZ = 1 THEN '单项合同'
                    WHEN a.WO_CONTRACTXZ = 2 THEN '框架合同'
                    WHEN a.WO_CONTRACTXZ = 3 THEN '保运（年度框架合同）'
                    else cast(a.WO_CONTRACTXZ as VARCHAR) end as "合同性质",
                ''                                            as "是否废弃",     -- 查找
                a.FQ_REASON                                   as "废弃原因",
                a.FQ_USER                                     as "废弃人",
                a.FQ_TIME                                     as "废弃时间"
from JWXXT.YJS_WORKORDER_TB a -- 项目
         inner join JWXXT.YJS_WP_WORKORDER_TB b on a.WO_ID = b.WO_ID -- 关联
         inner join jwxxt.YJS_WPINF_TB c on b.WPINF_ID = c.WPINF_ID -- 工序
         inner join JWXXT.YJS_ERP_WORKORDER_TB d on c.WO_NO = d.WO_NO --ERP
         inner join JWXXT.YJS_JWRWWTS_TB e on d.WO_NO = e.ERP_NO
         inner join JWXXT.YJS_HT_TB f on a.WO_CONTRACTNO = f.HT_BM -- 合同
where a.WO_ORDERTIME between to_date('2015-01-01', 'yyyy-MM-dd') and to_date('2023-06-01', 'yyyy-MM-dd')
  AND a.WO_NO = '10252321220001'


select distinct a.WO_NO         as "项目号",
                a.WO_DESCRIBE   as "项目名称",
--                 e.RWS_NO        AS "任务书编号",
                a.WO_ORDERTIME  as "项目下达时间",
                a.WO_SFYS       as "是否预算项目",
                a.WO_XMXZ       as "项目性质",
                d.WO_VERSION    as "版本号",
                a.FUN_PLACE     as "功能位置",
                a.FUN_DESCRIBE  as "功能位置描述",
                a.WO_CREATER    as "创建人",
                a.WO_GRPNAME    as "计划员组描述",
                a.PROVIDER_NO   as "工作中心代码",
                a.PROVIDER_NAME as "工作中心",
                f.HT_XDRBM      AS "供应商简称",
                f.HT_XDRMC      AS "供应商编号",
                f.HT_SJLY       as "项目属性",
                ''              AS "备注",         -- 查找
                a.WO_YWFWDM     as "业务范围",
                a.WO_CBZX_NO    as "成本中心编码",
                a.WO_CBZX       as "成本中心描述",
                ''              AS "项目进展情况", -- 查找
                a.WO_SFYS       as "是否下达",
                a.WO_CONTRACTNO as "合同号",
                a.WO_CONTRACTXZ as "合同性质",
                ''              as "是否废弃",     -- 查找
                a.FQ_REASON     as "废弃原因",
                a.FQ_USER       as "废弃人",
                a.FQ_TIME       as "废弃时间"
from JWXXT.YJS_WORKORDER_TB a -- 项目
         inner join JWXXT.YJS_WP_WORKORDER_TB b on a.WO_ID = b.WO_ID -- 关联
         inner join jwxxt.YJS_WPINF_TB c on b.WPINF_ID = c.WPINF_ID -- 工序
         inner join JWXXT.YJS_ERP_WORKORDER_TB d on c.WO_NO = d.WO_NO --ERP
--          inner join JWXXT.YJS_JWRWWTS_TB e on d.WO_NO = e.ERP_NO
         inner join JWXXT.YJS_HT_TB f on a.WO_CONTRACTNO = f.HT_BM -- 合同
where a.WO_ORDERTIME between to_date('2015-01-01', 'yyyy-MM-dd') and to_date('2023-06-01', 'yyyy-MM-dd')
  AND a.WO_NO = '10252321220001'


select *
from (select a.ERP_NO                                                   AS "工单号"
           , a.RWS_NO                                                   AS "任务单号"
           , (select ttt1.tache_name
              from JWXXT.AUTH_ORGANIZATION_TB ttt1
              WHERE module_id = 445
                and t.tache_no = a.U_STATE)                             AS "审核状态"
           , (select max(ry1.HIS_RECIVEUSERNAME)
              from JWXXT.FLOW_SPHISTORY_VW ry1
              where ry1.MODULE_ID = 445
                and ry1.HIS_CODES = a.RWS_ID
                and ry1.HIS_CHKTIME = (select max(ry2.HIS_CHKTIME)
                                       FROM JWXXT.FLOW_SPHISTORY_VW ry2
                                       Where 1 = 1
                                         and ry2.MODULE_ID = 445
                                         and ry2.HIS_CODES = a.RWS_ID)) AS "接收人"   -- 查找
           , (select max(tm1.HIS_CHKTIME)
              FROM JWXXT.FLOW_SPHISTORY_VW tm1
              Where 1 = 1
                and tm1.MODULE_ID = 445
                and tm1.HIS_CODES = a.RWS_ID)                           AS "接收时间" -- 查找
           , (select b.u_name
              from JWXXT.AUTH_ORGANIZATION_TB b
              where b.org_id
                        in (select c.org_id_superior
                            from JWXXT.AUTH_ORGANIZATION_TB c
                            where c.u_name_full = a.ORG_NAME))          AS "单位名称"
           , a.ORG_NAME                                                 AS "项目单位"
           , a.XM_NAME                                                  AS "项目名称"
           , a.ZY_TYPE                                                  AS "作业类型"
           , a.SGDW                                                     AS "施工单位"
           , a.BBH                                                      AS "版本号"
           , a.JF_XMFZR                                                 AS "甲方项目负责人"
           , a.YF_XMFZR                                                 AS "乙方项目负责人"
           , a.PLAN_ZFY                                                 AS "总计划费用(元)"
           , a.PLAN_WWFY                                                AS "外委计划费用（元)"
           , a.PLAN_CLFY                                                AS "材料计划费用(元）"
           , a.HT_NAME                                                  AS "合同名称"
           , a.HT_FY                                                    AS "合同金额"
           , a.HT_NO                                                    AS "合同号"
           , a.EQUIP_WH                                                 AS "设备位号"
           , a.EQUIP_CODE                                               AS "设备代码"
           , a.EQUIP_NAME                                               AS "设备名称"
           , a.PLAN_BEGINTIME                                           AS "计划开始检修时间"
           , a.PLAN_ENDTIME                                             AS "计划结束检修时间"
           , a.JSDW_FZR                                                 AS "建设单位负责人"
      from JWXXT.YJS_JWRWWTS_TB a) a
where a."接收时间" between to_date('2018-01-01', 'yyyy-MM-dd') and to_date('2023-09-01', 'yyyy-MM-dd');

select TACHE_NAME, TACHE_NO
from RAW_JWXFY.FLOW_TACHE_TB
WHERE MODULE_ID = 445

select t.tache_name, t.tache_no
from flow_tache_tb t
where module_id = 445
order by t.tache_no where ttt1.org_id
          in (select c.org_id_superior
              from JWXXT.AUTH_ORGANIZATION_TB c
              where c.u_name_full = a.ORG_NAME)


-- where a.PLAN_BEGINTIME between to_date('2018-01-01', 'yyyy-MM-dd') and to_date('2023-09-01', 'yyyy-MM-dd')
--   AND a.WO_NO = '10252321220001';

-- (select max(HIS_CHKTIME)
--  FROM JWXXT.FLOW_SPHISTORY_VW
--  Where 1 = 1
--    and MODULE_ID = 445
--    and HIS_CODES = a.RWS_ID)
--
-- (
-- select max(ry1.HIS_RECIVEUSERNAME)
-- from JWXXT.FLOW_SPHISTORY_VW ry1
-- where ry1.MODULE_ID = 445
--   and ry1.HIS_CODES = a.RWS_ID
--   and ry1.HIS_CHKTIME = (select max(ry2.HIS_CHKTIME)
--                          FROM FLOW_SPHISTORY_VW ry2
--                          Where 1 = 1
--                            and ry2.MODULE_ID = 445
--                            and ry2.HIS_CODES = a.RWS_ID)
--     )


select *
from (select (select ttt1.TACHE_NAME
              from JWXXT.FLOW_TACHE_TB ttt1
              WHERE ttt1.MODULE_ID = 445
                and ttt1.TACHE_NO = a.U_STATE)                          AS "审核状态"
           , (select max(ry1.HIS_RECIVEUSERNAME)
              from JWXXT.FLOW_SPHISTORY_VW ry1
              where ry1.MODULE_ID = 445
                and ry1.HIS_CODES = a.RWS_ID
                and ry1.HIS_CHKTIME = (select max(ry2.HIS_CHKTIME)
                                       FROM JWXXT.FLOW_SPHISTORY_VW ry2
                                       Where 1 = 1
                                         and ry2.MODULE_ID = 445
                                         and ry2.HIS_CODES = a.RWS_ID)) AS "接收人"   -- 查找
           , (select max(tm1.HIS_CHKTIME)
              FROM JWXXT.FLOW_SPHISTORY_VW tm1
              Where 1 = 1
                and tm1.MODULE_ID = 445
                and tm1.HIS_CODES = a.RWS_ID)                           AS "接收时间" -- 查找
           , a.ERP_NO                                                   AS "工单号"
           , a.RWS_NO                                                   AS "任务单号"
           , (select b.u_name
              from JWXXT.AUTH_ORGANIZATION_TB b
              where b.org_id
                        in (select c.org_id_superior
                            from JWXXT.AUTH_ORGANIZATION_TB c
                            where c.u_name_full = a.ORG_NAME))          AS "单位名称"
           , a.ORG_NAME                                                 AS "项目单位"
           , a.XM_NAME                                                  AS "项目名称"
           , a.ZY_TYPE                                                  AS "作业类型"
           , a.SGDW                                                     AS "施工单位"
           , a.BBH                                                      AS "版本号"
           , a.JF_XMFZR                                                 AS "甲方项目负责人"
           , a.YF_XMFZR                                                 AS "乙方项目负责人"
           , a.PLAN_ZFY                                                 AS "总计划费用(元)"
           , a.PLAN_WWFY                                                AS "外委计划费用（元)"
           , a.PLAN_CLFY                                                AS "材料计划费用(元）"
           , a.HT_NAME                                                  AS "合同名称"
           , a.HT_FY                                                    AS "合同金额"
           , a.HT_NO                                                    AS "合同号"
           , a.EQUIP_WH                                                 AS "设备位号"
           , a.EQUIP_CODE                                               AS "设备代码"
           , a.EQUIP_NAME                                               AS "设备名称"
           , a.PLAN_BEGINTIME                                           AS "计划开始检修时间"
           , a.PLAN_ENDTIME                                             AS "计划结束检修时间"
           , a.JSDW_FZR                                                 AS "建设单位负责人"
      from JWXXT.YJS_JWRWWTS_TB a)
where "接收时间" between to_date('2018-01-01', 'yyyy-MM-dd') and to_date('2023-09-01', 'yyyy-MM-dd')



select distinct a.WO_NO         as "项目号",
                e.ERP_NO        as "工单号",
                a.WO_DESCRIBE   as "项目名称",
                a.WO_ORDERTIME  as "项目下达时间",
                a.WO_SFYS       as "是否预算项目",
                a.WO_XMXZ       as "项目性质",
                d.WO_VERSION    as "版本号",
                a.FUN_PLACE     as "功能位置",
                a.FUN_DESCRIBE  as "功能位置描述",
                a.WO_CREATER    as "创建人",
                a.WO_GRPNAME    as "计划员组描述",
                a.PROVIDER_NO   as "工作中心代码",
                a.PROVIDER_NAME as "工作中心",
                f.HT_XDRBM      as "供应商简称",
                f.HT_XDRMC      as "供应商编号",
                f.HT_SJLY       as "项目属性",
                ''              AS "备注",         -- 查找
                a.WO_YWFWDM     as "业务范围",
                a.WO_CBZX_NO    as "成本中心编码",
                a.WO_CBZX       as "成本中心描述",
                ''              AS "项目进展情况", -- 查找
                a.WO_SFYS       as "是否下达",
                a.WO_CONTRACTNO as "合同号",
                a.WO_CONTRACTXZ as "合同性质",
                ''              as "是否废弃",     -- 查找
                a.FQ_REASON     as "废弃原因",
                a.FQ_USER       as "废弃人",
                a.FQ_TIME       as "废弃时间"
from JWXXT.YJS_WORKORDER_TB a -- 项目
         inner join JWXXT.YJS_WP_WORKORDER_TB b on a.WO_ID = b.WO_ID -- 关联
         inner join jwxxt.YJS_WPINF_TB c on b.WPINF_ID = c.WPINF_ID -- 工序
         inner join JWXXT.YJS_ERP_WORKORDER_TB d on c.WO_NO = d.WO_NO --ERP
         inner join JWXXT.YJS_JWRWWTS_TB e on d.WO_NO = e.ERP_NO
         inner join JWXXT.YJS_HT_TB f on a.WO_CONTRACTNO = f.HT_BM -- 合同
where a.WO_ORDERTIME between to_date('2018-01-01', 'yyyy-MM-dd') and to_date('2023-06-01', 'yyyy-MM-dd')


SELECT DB_NAME()                                                AS DatabaseName,
       sch.name                                                 AS SchemaName,
       tbl.name                                                 AS TableName,
       col.name                                                 AS ColumnName,
       ep.value                                                 AS ColumnDescription,
       tp.name                                                  AS DataType,
       col.max_length                                           AS MaxLength,
       col.precision                                            AS PrecisionValue,
       CASE WHEN idx.is_primary_key = 1 THEN '是' ELSE '否' END AS IsPrimaryKey,
       CASE WHEN col.is_nullable = 1 THEN '是' ELSE '否' END    AS IsNullable,
       CASE WHEN idx.is_unique = 1 THEN '是' ELSE '否' END      AS IsUnique
FROM sys.tables tbl
         INNER JOIN sys.schemas sch ON tbl.schema_id = sch.schema_id
         INNER JOIN sys.columns col ON tbl.object_id = col.object_id
         LEFT JOIN sys.extended_properties ep
                   ON tbl.object_id = ep.major_id AND col.column_id = ep.minor_id AND ep.name = 'MS_Description'
         INNER JOIN sys.types tp ON col.user_type_id = tp.user_type_id
         LEFT JOIN sys.index_columns ic ON tbl.object_id = ic.object_id AND col.column_id = ic.column_id
         LEFT JOIN sys.indexes idx ON ic.object_id = idx.object_id AND ic.index_id = idx.index_id
WHERE
--     tbl.is_ms_shipped = 0 -- 排除系统表
-- tbl.name = 'sys_items'
ORDER BY SchemaName, TableName, col.column_id;

SELECT c.owner,
       c.table_name                                              AS "表名称",
       c.column_name                                             AS "字段",
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
-- WHERE c.owner = 'RAW_LTX'
--   AND c.table_name = 'ODS_PERSONINFOMATIONEXPAND'
ORDER BY c.owner, c.table_name, c.column_id;

