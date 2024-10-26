import frappe
from frappe import _
from frappe.auth import LoginManager 
from frappe.exceptions import AuthenticationError

@frappe.whitelist(allow_guest=True) 
def test():
    return "Hi from Jay Patel"

# Login
@frappe.whitelist(allow_guest=True) 
def signin(user,pwd):
    """
    Login user via username and password 
    """
    login_manager = LoginManager()
    login_manager.authenticate(user,pwd)
    login_manager.post_login()
    user_data = frappe.get_doc("User", frappe.session.user)
    
    frappe.response.sid = frappe.session.sid
    frappe.response.status_code = 200
    # frappe.response.user = user_data
    #     print("Login Sucess using APIs")
            

@frappe.whitelist() 
def privatepage():
    return frappe.session

# Logout
@frappe.whitelist() 
def signout():
    frappe.local.login_manager.logout()
    return {"message": _("Logged out successfully!")}

@frappe.whitelist(allow_guest=True)
def request_reset_password(user):
    """
    API to request a password reset
    """
    try:
        if not frappe.db.exists("User", {"username": user}):
            return {"error": _("User does not exist")}
        user_doc = frappe.get_doc("User", {"username": user})

        user_doc.reset_password()

        return {"status": "success", "message": _(f"Password reset link has been sent to your {user_doc.email} email.")}

    except Exception as e:
        frappe.local.response.status_code = 500
        return {"error": str(e)}