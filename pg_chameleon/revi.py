def get_dest_table(table):
    table_mapping = {
        "orders_orderingsettings_prompt_to_catering_inquery_catering_f12f": "orders_orderingsettings_prompt_to_catering_inquery_cateringf12f",
        "employee_7_shifts_sevenshiftsemployeesettings_internal_busindf99": "employee_7_shifts_sevenshiftsemployeesettings_internal_busidf99",
        "employee_7_shifts_sevenshiftslocationsettings_disconnected_b5f66": "employee_7_shifts_sevenshiftslocationsettings_disconnected_5f66",
    }
    table = table_mapping.get(table, table)
    return table
