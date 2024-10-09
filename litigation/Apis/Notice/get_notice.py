import frappe



@frappe.whitelist()
def get_notice_with_child_tables(notice_name):
    
    notice_doc = frappe.get_doc('Notice', notice_name)

    
    return {
        "notice": notice_doc.as_dict(),
        "notice_demand_amount": notice_doc.get("notice_demand_amount"),
        "notice_pre_deposit_and_contingent_liability_amount": notice_doc.get("notice_pre_deposit_and_contingent_liability_amount"),
        "notice_disputed_amount": notice_doc.get("notice_disputed_amount"),
        "notice_admitted_amount": notice_doc.get("notice_admitted_amount")
    }
