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



def check_stage(data, method):

    notice_id = data.get('notice_id')
    stage = data.get('notice_stage')
    print("**********", notice_id, stage)




# @frappe.whitelist(allow_guest=True)
# def create_filtered_resource(doctype, **data):
    
#     doc = frappe.get_doc({
#         "doctype": "Notice",
#         **data
#         })
#     doc.insert()

    
#     filtered_response = {
#         "name": doc.name

#     }

#     return filtered_response

# @frappe.whitelist(allow_guest=True)
# def create_filtered_resource(doctype, **data):
    
#     doc = frappe.get_doc({
#         "doctype": "Notice",
#         "notice_id": data.get("notice_id"),
#         "notice_type": data.get("notice_type"),
#         "demand_amount": data.get("demand_amount"),
#         "pre_deposit_and_contingent_liability": data.get("pre_deposit_and_contingent_liability")
#     })

  
#     doc.insert()

    
#     frappe.db.commit()

   
#     filtered_response = {
#         "name": doc.name
#     }

#     return filtered_response



@frappe.whitelist(allow_guest=True)
def create_and_update_notice(**data):
    created = False

    if data.get("name"):
        doc = frappe.get_doc("Notice", data.get("name"))
    elif data.get("name"):
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
        "ref_no": data.get("name"),
        "notice_id": data.get("notice_id"),
        "notice_type": data.get("notice_type"),
        "demand_amount": data.get("demand_amount"),
        "pre_deposit_and_contingent_liability": data.get("pre_deposit_and_contingent_liability"),
        "disputed_amount": data.get("disputed_amount"),
        "table_okzc": data.get("table_okzc"),
        "contingent_liabilities": data.get("contingent_liabilities"),
    })

    doc.save()
    frappe.db.commit()

    status_code = 201 if created else 200

    filtered_response = {
        "name": doc.name,
        "status_code": status_code
    }

    return filtered_response


# @frappe.whitelist(allow_guest=True)
# def create_and_update_notice(doctype, **data):
#     created = False

#     if data.get("name"):
#         doc = frappe.get_doc("Notice", data.get("name"))
#     elif data.get("ref_no"):
#         existing_doc = frappe.db.exists("Notice", {"name": data.get("name")})
#         if existing_doc:
#             doc = frappe.get_doc("Notice", existing_doc)
#         else:
#             doc = frappe.get_doc({"doctype": "Notice"})
#             created = True
#     else:
#         existing_doc = frappe.db.exists("Notice", {"notice_id": data.get("notice_id")})
#         if existing_doc:
#             doc = frappe.get_doc("Notice", existing_doc)
#             notice_stage = doc.notice_stage
#             if notice_stage == data.get("stage_name"):
#                 frappe.throw(f"This notice ID already exists with the same stage name: {stage_name}")
#         else:
#             doc = frappe.get_doc({"doctype": "Notice"})
#             created = True

#     doc.update({
#         "ref_no": data.get("ref_no"),
#         "notice_id": data.get("notice_id"),
#         "notice_type": data.get("notice_type"),
#         "demand_amount": data.get("demand_amount"),
#         "pre_deposit_and_contingent_liability": data.get("pre_deposit_and_contingent_liability"),
#         "stage_name": data.get("stage_name")  
#     })

#     doc.save()
#     frappe.db.commit()

#     status_code = 201 if created else 200

#     filtered_response = {
#         "name": doc.name,
#         "status_code": status_code
#     }

#     return filtered_response





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

	