select custom_table_1660014221571."G0GSDM"         "custom_table_1660014221571_g0gsdm",
       custom_table_1660014221571."G0OI_EBELN"     "custom_table_1660014221571_g0oi_ebeln",
       custom_table_1660014221571."G0ZINTYP"       "custom_table_1660014221571_g0zintyp",
       sum(custom_table_1660014221571."K0CGDDSL0") "RKD_custom_table_1660014221571_k0cgddsl0_EV",
       avg(custom_table_1660014221571."K0CGJJ1")   "RKD_custom_table_1660014221571_k0cgjj1_V8",
       sum(custom_table_1660014221571."K0DDHSJE0") "RKD_custom_table_1660014221571_k0ddhsje0_TA",
       COUNT(1)                                    "RKD_B03_A2_Q1_A1_COUNTER_WZ"
from () custom_table_1660014221571
group by custom_table_1660014221571."G0GSDM", custom_table_1660014221571."G0OI_EBELN",
         custom_table_1660014221571."G0ZINTYP"
having sum(custom_table_1660014221571."K0DDHSJE0") is not null
order by custom_table_1660014221571."G0GSDM" ASC, custom_table_1660014221571."G0OI_EBELN" ASC,
         custom_table_1660014221571."G0ZINTYP" ASC
