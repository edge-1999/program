def data_handle(input_data):
    import pandas as pd
    import numpy as np
    from adata_py.util.db.clickhouse_db_utils import ClickHouseDBUtils
    ch = ClickHouseDBUtils()
    pd.set_option('display.max_columns', None)  # 不应该加
    # input_data_df = input_data_df.loc[input_data_df['ELE_Q_G0GZLSH'] == '1500562130']
    input_data_df = pd.DataFrame(input_data)
    if len(input_data_df) != 0 and 'ELE_Q_G0GZLSH' in input_data_df:
        gzlsh = ''
        SQL_T2 = ''
        for i in range(len(input_data_df)):
            if input_data_df.iloc[i]['ELE_Q_G0GZLSH'] != '':
                if i < len(input_data_df) - 1:
                    gzlsh = gzlsh + "'" + input_data_df.iloc[i]['ELE_Q_G0GZLSH'] + "',"
                elif i == len(input_data_df) - 1:
                    gzlsh = gzlsh + "'" + input_data_df.iloc[i]['ELE_Q_G0GZLSH'] + "'"
                    gzlsh = '(' + gzlsh + ')'
        SQL_T2 = "SELECT ELE_Q_G0OI_EBELN,ELE_Q_G0OI_EBELP,ELE_Q_G0LOGSYS_ERP,ELE_Q_G0WBNBDXH,ELE_Q_G0GZLSH FROM WAR_Q_HTLYDQWJS_CJ1_T2_ACTIVATION WHERE ELE_Q_G0GZLSH IN "
        SQL_T2 = SQL_T2 + gzlsh + " AND ELE_Q_G0OI_EBELN <> '' "
        # AND ELE_Q_G0GSDM = '1590' "
        data_ld_T2 = ch.fetchall(SQL_T2)
        data_df_T2 = pd.DataFrame(data_ld_T2)
        # WHERE ELE_Q_G0GZLSH in ('1500562130')"
        if len(data_df_T2) != 0:
            input_data_df = pd.merge(input_data_df, data_df_T2, how='left', left_on='ELE_Q_G0GZLSH',
                                     right_on='ELE_Q_G0GZLSH')
            input_data_df = input_data_df.dropna(subset=['ELE_Q_G0OI_EBELN'])
            print('----')
    if 'ELE_Q_G0OI_EBELN' in input_data_df and len(input_data_df) != 0:
        EBELN = ''
        SQL_T3 = ''
        for i in range(len(input_data_df)):
            if input_data_df.iloc[i]['ELE_Q_G0OI_EBELN'] != '':
                if i < len(input_data_df) - 1:
                    EBELN = EBELN + "'" + input_data_df.iloc[i]['ELE_Q_G0OI_EBELN'] + "',"
                elif i == len(input_data_df) - 1:
                    EBELN = EBELN + "'" + input_data_df.iloc[i]['ELE_Q_G0OI_EBELN'] + "'"
                    EBELN = '(' + EBELN + ')'
        SQL_T3 = "SELECT ELE_Q_G0OI_EBELN,ELE_Q_G0OI_EBELP,ELE_Q_G0LOGSYS_ERP,ELE_Q_G0LBLNI FROM WAR_Q_HTLYDQWJS_CJ1_T3_FIX_ACTIVATION WHERE ELE_Q_G0OI_EBELN IN "
        SQL_T3 = SQL_T3 + EBELN + " AND ELE_Q_G0OI_EBELN <> '' AND ELE_Q_G0OI_EBELP <> ''  AND  ELE_Q_G0LOGSYS_ERP <> '' "
        # AND ELE_Q_G0GSDM = '1590' "
        # WHERE ELE_Q_G0OI_EBELN IN ('2500063043','2700012243') and ELE_Q_G0LOGSYS_ERP in ('PR3CLNT800')"
        data_ld_T3 = ch.fetchall(SQL_T3)
        data_df_T3 = pd.DataFrame(data_ld_T3)
        if len(data_df_T3) != 0:
            data_df_T3.rename(columns={'ELE_Q_G0LBLNI': 'ELE_Q_LBLNI'}, inplace=True)
            # input_data_df = input_data_df.loc[input_data_df['ELE_Q_G0GZLSH'] == '1500562130']
            input_data_df = pd.merge(input_data_df, data_df_T3, how='left',
                                     on=['ELE_Q_G0OI_EBELN', 'ELE_Q_G0OI_EBELP', 'ELE_Q_G0LOGSYS_ERP'])
            '''
            input_data_df = input_data_df[['ELE_Q_LBLNI']].apply(lambda x: x.str.strip()).replace('', np.nan)
            input_data_df = input_data_df.dropna(axis=0,how='any',subset=['ELE_Q_LBLNI'])
            input_data_df = input_data_df[['ELE_Q_G0OI_EBELN']].apply(lambda x: x.str.strip()).replace('', np.nan)
            input_data_df = input_data_df.dropna(axis=0,how='any',subset=['ELE_Q_G0OI_EBELN'])'''

    out_data = input_data_df.to_dict(orient='records')
    return out_data
