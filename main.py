from __future__ import unicode_literals
import frappe
import frappe.defaults
from frappe.utils import nowdate, cstr, flt, cint, now ,getdate
from frappe import throw, _
from frappe.utils import formatdate, get_number_format_info
import requests
import json
import datetime

@frappe.whitelist()
def notify_new_doc(doc,action):
	try:
		doc = doc.as_dict()
		if '__run_link_triggers' in doc:
			msg = """
<h2>Document created</h2>
<h3 style='color: #999999'>E-mail alert: New document created</h3>
<strong>Document type:</strong> {doctype}<br>
<strong>Created by:</strong> {user}<br>
<strong>Creation date:</strong> {date}<br><br>
<strong>Information:</strong><br>
<pre>{doc}</pre>
""".format(doctype=doc.doctype, user=doc.owner, date=frappe.utils.get_datetime(doc.creation).strftime('%m/%d/%Y %H:%M:%S'), doc=doc)
			subject = "[Creation] new monitored type document created"
			recipients="team@company.com"
			frappe.sendmail(recipients=recipients, subject=subject, message=msg, now=True)
		else:
			pass
	except Exception as e:
		print(e)
		pass