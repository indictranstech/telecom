import frappe

def get_permission_query_conditions(user):
	if not user: user = frappe.session.user

	if not user in ("Administrator", "support@tanms.com"):
		return """(`tabEmployee`.user_id = '{0}')""".format(user)