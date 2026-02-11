import frappe

def create_timeline_entry(doc, method=None):
    # Create Communication entry so it appears in Timeline of Lead/Prospect/Customer/etc.
    comm = frappe.new_doc("Communication")

    comm.communication_type = "Communication"
    comm.communication_medium = "Social Media"
    comm.sent_or_received = "Received" if doc.direction == "Incoming" else "Sent"

    comm.subject = f"{doc.platform} {doc.interaction_type}"

    message_text = frappe.utils.escape_html(doc.message_text or "")
    url_line = f"<br><br><a href='{doc.message_url}' target='_blank'>Open on {doc.platform}</a>" if doc.message_url else ""
    comm.content = message_text + url_line

    comm.reference_doctype = doc.reference_doctype
    comm.reference_name = doc.reference_name

    comm.save(ignore_permissions=True)
