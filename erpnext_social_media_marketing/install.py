import frappe

def after_install():
    create_contact_social_fields()

def create_contact_social_fields():
    fields = [
        {
            "doctype": "Custom Field",
            "dt": "Contact",
            "fieldname": "smm_section",
            "label": "Social Media",
            "fieldtype": "Section Break",
            "insert_after": "email_id",
            "collapsible": 1
        },
        {
            "doctype": "Custom Field",
            "dt": "Contact",
            "fieldname": "linkedin_url",
            "label": "LinkedIn URL",
            "fieldtype": "Data",
            "options": "URL",
            "insert_after": "smm_section"
        },
        {
            "doctype": "Custom Field",
            "dt": "Contact",
            "fieldname": "x_handle",
            "label": "X (Twitter) Handle",
            "fieldtype": "Data",
            "insert_after": "linkedin_url"
        },
        {
            "doctype": "Custom Field",
            "dt": "Contact",
            "fieldname": "instagram_handle",
            "label": "Instagram Handle",
            "fieldtype": "Data",
            "insert_after": "x_handle"
        },
    ]

    for f in fields:
        if not frappe.db.exists("Custom Field", {"dt": f["dt"], "fieldname": f["fieldname"]}):
            frappe.get_doc(f).insert(ignore_permissions=True)

    frappe.clear_cache()
