import frappe
from frappe import _

@frappe.whitelist()
def test_function():
    json_string = '{"name": "John", "age": 30}'
    data = frappe.json.loads(json_string)
    print(data)
    return data, type(data)




@frappe.whitelist(allow_guest=True)
def get_master_data():
    try:
       
        entity_data = frappe.get_all('Entity Master', fields=['*'])

        
        department_data = frappe.get_all('Department Master', fields=['*'])

        
        issuing_authority_data = frappe.get_all('Issuing Authority Master', fields=['*'])

        
        user_data = frappe.get_all('User', fields=['name', 'email', 'role_profile_name'])

        gst_form_data = frappe.get_all('GST Form Master', 'form_name')


        frappe.local.response['http_status_code'] = 200
        return {
            'status': 'success',
            'message': 'Data fetched successfully',
            'data': {
                'entity_master': entity_data,
                'department_master': department_data,
                'issuing_authority_master': issuing_authority_data,
                'user_data': user_data,
                'gst_form_data': gst_form_data
            }
        }

    except Exception as e:
      
        frappe.local.response['http_status_code'] = 500
        return {
            'status': 'failure',
            'message': f'Error fetching data: {str(e)}'
        }







# @frappe.whitelist()
# def get_master_data():
    
#     entity_data = frappe.get_all('Entity Master', fields=['*'])


#     department_data = frappe.get_all('Department Master', fields=['*'])

    
#     issuing_authority_data = frappe.get_all('Issuing Authority Master', fields=['*'])


#     user_data = frappe.get_all('User', fields=['name', 'email', 'role_profile_name'])

  
#     return {
#         'entity_master': entity_data,
#         'department_master': department_data,
#         'issuing_authority_master': issuing_authority_data,
#         'user_data': user_data
#     }










# @frappe.whitelist()
# def get_notice_with_child_tables(notice_name):
    
#     notice_doc = frappe.get_doc('Notice', notice_name)

    
#     return {
#         "notice": notice_doc.as_dict(),
#         "notice_demand_amount": notice_doc.get("notice_demand_amount"),
#         "notice_pre_deposit_and_contingent_liability_amount": notice_doc.get("notice_pre_deposit_and_contingent_liability_amount"),
#         "notice_disputed_amount": notice_doc.get("notice_disputed_amount"),
#         "notice_admitted_amount": notice_doc.get("notice_admitted_amount")
#     }

# @frappe.whitelist()
# def all_notice():

	