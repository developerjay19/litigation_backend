import frappe
from frappe import _
from frappe.model.document import Document
from http import HTTPStatus
import base64
from frappe.utils.file_manager import save_file


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

   
#     exists = frappe.db.sql(""" SELECT notice_id, notice_stage FROM `tabNotice` WHERE notice_id=%s AND notice_stage=%s AND name!=%s """, (notice_id, stage, name), as_dict=1)

#     print("*****************", exists)
    
#     if exists:
#         frappe.throw("Stage already exists for this Notice ID.")
#     else:
#         pass
#     print("***********************************", exists)

    

def check_stage(data, method):
    name = data.get('name')  
    notice_id = data.get('notice_id')
    stage = data.get('stage')
    print("***************", name, notice_id, stage)

   
    exists = frappe.db.sql(""" SELECT notice_id, stage FROM `tabNotice` WHERE notice_id=%s AND stage=%s AND name!=%s """, (notice_id, stage, name), as_dict=1)

    print("*****************", exists)
    
    if exists:
        frappe.throw("Stage already exists for this Notice ID.")
    else:
        pass
    print("***********************************", exists)



# @frappe.whitelist()
# def create_and_update_notice(**data):
#     created = False

#     if data.get("name"):
#         existing_doc = frappe.db.exists("Notice", {"name": data.get("name")})
#         if existing_doc:
#             doc = frappe.get_doc("Notice", existing_doc)
#         else:
#             doc = frappe.get_doc({"doctype": "Notice"})
#             created = True
#     else:
#         doc = frappe.get_doc({"doctype": "Notice"})
#         created = True

  
#     doc.update({
#         "name": data.get("name"),
#         "notice_id": data.get("notice_id") if data.get("notice_id") else doc.notice_id,  
#         "notice_type": data.get("notice_type") or doc.notice_type, 
#         "notice_date":  data.get("notice_date") or doc.notice_date, 
#         "entity":  data.get("entity") or doc.entity,
#         "gstin":  data.get("gstin") or doc.gstin,  
#         "gst_form":  data.get("gst_form") or doc.gst_form, 
#         "department":  data.get("department") or doc.department, 
#         "issuing_authority":  data.get("issuing_authority") or doc.issuing_authority,
#         "mobile_no":  data.get("mobile_no") or doc.mobile_no,
#         "email":  data.get("email") or doc.email,
#         "mode_of_communication":  data.get("mode_of_communication") or doc.mode_of_communication,
#         "din_no":  data.get("din_no") or doc.din_no,
#         "din_date":  data.get("din_date") or doc.din_date,
#         "ref_no":  data.get("ref_no") or doc.ref_no,
#         "ref_date":  data.get("ref_date") or doc.ref_date,
#         "issue_under_section":  data.get("issue_under_section") or doc.issue_under_section,
#         "issue_under_rule":  data.get("issue_under_rule") or doc.issue_under_rule,
#         "period_covered":  data.get("period_covered") or doc.period_covered,
#         "date_of_receipt_of_notice":  data.get("date_of_receipt_of_notice") or doc.date_of_receipt_of_notice,
#         "due_date":  data.get("due_date") or doc.due_date,
#         "prepared_by":  data.get("prepared_by") or doc.prepared_by,
#         "reviewed_by":  data.get("reviewed_by") or doc.reviewed_by,
#         "appeal_status":  data.get("appeal_status") or doc.appeal_status,
#         "date_or_replay_submit":  data.get("date_or_replay_submit") or doc.date_or_replay_submit,
#         "date_or_arn":  data.get("date_or_arn") or doc.date_or_arn,
#         "attachment":  data.get("attachment") or doc.attachment,
#         "date_of_appeal":  data.get("date_of_appeal") or doc.date_of_appeal,
#         "notice_status":  data.get("notice_status") or doc.notice_status,
#         "date_of_hearing":  data.get("date_of_hearing") or doc.date_of_hearing,
#         "notice_stage":  data.get("notice_stage") or doc.notice_stage,
#         "date_of_extension":  data.get("date_of_extension") or doc.date_of_extension,
#         "remarks":  data.get("remarks") or doc.remarks,

#         "demand_amount": data.get("demand_amount") or doc.demand_amount,
#         "pre_deposit_and_contingent_liability": data.get("pre_deposit_and_contingent_liability") or doc.pre_deposit_and_contingent_liability,
#         "disputed_amount": data.get("disputed_amount") or doc.disputed_amount,
#         "table_okzc": data.get("table_okzc") or doc.table_okzc,
#         "contingent_liabilities": data.get("contingent_liabilities") or doc.contingent_liabilities,
#     })


#     doc.save()
#     frappe.db.commit()

    
#     status_code = 201 if created else 200


#     filtered_response = {
#         "name": doc.name,
#         "status_code": status_code
#     }

#     return filtered_response

""" Below is the working code Original """
# @frappe.whitelist()
# def create_and_update_notice(**data):
#     try:
#         created = False

#         if data.get("name"):
#             existing_doc = frappe.db.exists("Notice", {"name": data.get("name")})
#             if existing_doc:
#                 doc = frappe.get_doc("Notice", existing_doc)
#             else:
#                 doc = frappe.get_doc({"doctype": "Notice"})
#                 created = True
#         else:
#             doc = frappe.get_doc({"doctype": "Notice"})
#             created = True

       
#         doc.update(data)

#         doc.save()
#         frappe.db.commit()

#         status_code = 201 if created else 200

#         filtered_response = {
#             "name": doc.name,
#             "status_code": status_code
#         }

#     except Exception as e:
        
#         frappe.db.rollback()  
#         filtered_response = {
#             "status_code": 406,
#             "error": str(e)
#         }

#     return filtered_response







@frappe.whitelist(allow_guest=True)
def create_and_update_notice(**data):
    try:
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

        doc.update(data)
        doc.save()
        frappe.db.commit()

        if 'attachment' in frappe.request.files:
            file = frappe.request.files['attachment']
            is_private = frappe.form_dict.get('is_private', 0)
            saved_file = save_file(file.filename, file.stream.read(), "Notice", doc.name, is_private=int(is_private))
            doc.attachment = saved_file.file_url
            doc.save()

        status_code = 201 if created else 200
        filtered_response = {
            "name": doc.name,
            "status_code": status_code
        }

    except Exception as e:
        frappe.db.rollback()
        filtered_response = {
            "status_code": 406,
            "error": str(e)
        }

    return filtered_response




@frappe.whitelist()
def latest_created_notice():

    vals = frappe.db.sql(""" SELECT t1.notice_id, t1.notice_date, t1.name ,t1.entity, t1.gst_form, t1.gstin, t1.stage, t1.notice_status FROM `tabNotice` t1 INNER JOIN (SELECT notice_id, MAX(creation) AS latest_creation FROM `tabNotice` GROUP BY notice_id) t2 ON t1.notice_id = t2.notice_id AND t1.creation = t2.latest_creation""", as_dict=1)
    return vals


@frappe.whitelist(allow_guest=True)
def create_and_update_appeal(**data):
    try:
        created = False

        if data.get("notice_id"):
            notice_name = frappe.db.get_value("Notice", {"notice_id": data.get("notice_id")}, "name")
            if not notice_name:
                raise ValueError(f"Notice with notice_id {data.get('notice_id')} does not exist.")
            data["notice_id"] = notice_name

        if data.get("name"):
            existing_doc = frappe.db.exists("Appeal", {"name": data.get("name")})
            if existing_doc:
                doc = frappe.get_doc("Appeal", existing_doc)
            else:
                doc = frappe.get_doc({"doctype": "Appeal"})
                created = True
        else:
            doc = frappe.get_doc({"doctype": "Appeal"})
            created = True

        doc.update(data)

        child_table_fields = ['demand_confirmation', 'pre_deposit', 'disputed_amount', 'refund', 'paid', 'contingent_liabilities']  

        for field in child_table_fields:
            if field in data:
                for child in data[field]:
                    if 'upload' in child:
                        attachment = child['upload']
                        child_doc = doc.append(field, {})
                        child_doc.upload = attachment

        doc.save()
        frappe.db.commit()

        status_code = 201 if created else 200
        filtered_response = {
            "name": doc.name,
            "status_code": status_code
        }

    except Exception as e:
        frappe.db.rollback()
        filtered_response = {
            "status_code": 406,
            "error": str(e)
        }

    return filtered_response




#User and Appellate Authority Master Data API
@frappe.whitelist()
def get_user_authority():
    try:
       
        user_data = frappe.get_all('User', fields=['full_name', 'email'])    
        authority_data = frappe.get_all('Appellate Authority Master', fields=['name'])

        frappe.local.response['http_status_code'] = 200
        return {
            'status': 'success',
            'message': 'Data fetched successfully',
            'data': {
                'user_data': user_data,
                'authority_data': authority_data,

            }
        }

    except Exception as e:
      
        frappe.local.response['http_status_code'] = 500
        return {
            'status': 'failure',
            'message': f'Error fetching data: {str(e)}'
        }


""" Below code works but without Attachment """
# @frappe.whitelist(allow_guest=True)
# def create_and_update_appeal(**data):
#     try:
#         created = False

#         if data.get("notice_id"):
#             notice_name = frappe.db.get_value("Notice", {"notice_id": data.get("notice_id")}, "name")
#             if not notice_name:
#                 raise ValueError(f"Notice with notice_id {data.get('notice_id')} does not exist.")
#             data["notice_id"] = notice_name

#         if data.get("name"):
#             existing_doc = frappe.db.exists("Appeal", {"name": data.get("name")})
#             if existing_doc:
#                 doc = frappe.get_doc("Appeal", existing_doc)
#             else:
#                 doc = frappe.get_doc({"doctype": "Appeal"})
#                 created = True
#         else:
#             doc = frappe.get_doc({"doctype": "Appeal"})
#             created = True

#         doc.update(data)
#         doc.save()
#         frappe.db.commit()

#         status_code = 201 if created else 200
#         filtered_response = {
#             "name": doc.name,
#             "status_code": status_code
#         }

#     except Exception as e:
#         frappe.db.rollback()
#         filtered_response = {
#             "status_code": 406,
#             "error": str(e)
#         }

#     return filtered_response


# @frappe.whitelist(allow_guest=True)
# def create_and_update_appeal(**data):
#     try:
#         created = False

#         if data.get("name"):
#             existing_doc = frappe.db.exists("Appeal", {"name": data.get("name")})
#             if existing_doc:
#                 doc = frappe.get_doc("Appeal", existing_doc)
#             else:
#                 doc = frappe.get_doc({"doctype": "Appeal"})
#                 created = True
#         else:
#             doc = frappe.get_doc({"doctype": "Appeal"})
#             created = True

#         doc.update(data)
#         doc.save()
#         frappe.db.commit()


#         status_code = 201 if created else 200
#         filtered_response = {
#             "name": doc.name,
#             "status_code": status_code
#         }

#     except Exception as e:
#         frappe.db.rollback()
#         filtered_response = {
#             "status_code": 406,
#             "error": str(e)
#         }

#     return filtered_response





# @frappe.whitelist()
# def create_and_update_notice(**data):
#     created = False

#     if data.get("name"):
#         existing_doc = frappe.db.exists("Notice", {"name": data.get("name")})
#         if existing_doc:
         
#             doc = frappe.get_doc("Notice", existing_doc)
#         else:
          
#             doc = frappe.get_doc({"doctype": "Notice"})
#             created = True
#     else:
     
#         doc = frappe.get_doc({"doctype": "Notice"})
#         created = True

  
#     fields_to_update = [
#         "notice_id",
#         "notice_type",
#         "demand_amount",
#         "pre_deposit_and_contingent_liability",
#         "disputed_amount",
#         "table_okzc",
#         "contingent_liabilities",
#     ]

#     for field in fields_to_update:
#         if field in data and data[field] is not None:
#             setattr(doc, field, data[field])  

    
#     doc.save()
#     frappe.db.commit()

    
#     status_code = 201 if created else 200

  
#     filtered_response = {
#         "name": doc.name,
#         "status_code": status_code
#     }

#     return filtered_response