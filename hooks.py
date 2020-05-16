# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "Create document monitor"
app_title = "create_doc"
app_publisher = "Marcos Vinicius Fernandes Machado"
app_description = "Monitoring created documents"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = ""
app_license = "MIT"

## insert code below in your hook.py file ##
doc_events = {
	"example_doc":{
		"before_save": "notify.main.notify_new_doc"
	}
}