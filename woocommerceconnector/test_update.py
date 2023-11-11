import frappe


def on_update(doc, method):
    # Your custom code here
    frappe.msgprint("Bin updated!")
