import frappe
from frappe import _
from frappe.model.document import Document
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

        stage_data = frappe.db.get_all('Stage Master', 'stage_name')


        frappe.local.response['http_status_code'] = 200
        return {
            'status': 'success',
            'message': 'Data fetched successfully',
            'data': {
                'entity_master': entity_data,
                'department_master': department_data,
                'issuing_authority_master': issuing_authority_data,
                'user_data': user_data,
                'gst_form_data': gst_form_data,
                'stage_data': stage_data
            }
        }

    except Exception as e:
      
        frappe.local.response['http_status_code'] = 500
        return {
            'status': 'failure',
            'message': f'Error fetching data: {str(e)}'
        }






# def check_stage(data, method):
#     name = data.get('name')
#     notice_id = data.get('notice_id')
#     stage = data.get('notice_stage')
#     print("***************", name, notice_id, stage)


#     # if not notice_id:
#     #     print("Notice ID is not provided.")
#     #     return

    
#     exists = frappe.db.exists("Notice", {"notice_stage": stage})
#     if exists:
#         frappe.throw("Stage already exists for this Notice ID.")
#     else:
#         pass
#     print("***********************************", record)

    
    # if record and record.notice_stage == stage:

    #     print(f"Stage is same: {notice_id}, Stage: {stage}")
        
    #     frappe.throw("Stage already exists for this Notice ID.")
    # else:
    #     print(f"Record Created: {notice_id}, Stage: {stage}")

@frappe.whitelist()
def create_and_update_notice(**data):
    created = False

    if data.get("name"):
        existing_doc = frappe.db.exists("Notice", {"name": data.get("name")})
        if existing_doc:
            doc = frappe.get_doc("Notice", existing_doc)
        else:
            doc = frappe.get_doc({"doctype": "Notice"})
            created = True
    else:
        doc = frappe.get_doc({"doctype": "Notice"})
        created = True

  
    doc.update({
        "name": data.get("name"),
        "notice_id": data.get("notice_id") if data.get("notice_id") else doc.notice_id,  
        "notice_type": data.get("notice_type") or doc.notice_type,  
        "demand_amount": data.get("demand_amount") or doc.demand_amount,
        "pre_deposit_and_contingent_liability": data.get("pre_deposit_and_contingent_liability") or doc.pre_deposit_and_contingent_liability,
        "disputed_amount": data.get("disputed_amount") or doc.disputed_amount,
        "table_okzc": data.get("table_okzc") or doc.table_okzc,
        "contingent_liabilities": data.get("contingent_liabilities") or doc.contingent_liabilities,
    })


    doc.save()
    frappe.db.commit()

    
    status_code = 201 if created else 200


    filtered_response = {
        "name": doc.name,
        "status_code": status_code
    }

    return filtered_response



