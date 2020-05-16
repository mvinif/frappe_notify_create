
# New doc monitoring in Frappe/ERPNext

This method is a simple way to keep monitoring which file was created and by whom, also providing the information about the doc

## Usage
To ideal usage of this method, firstly we need :

 - Setup a default outgoing email account in Frappe configuration
 - Configure hook.py file
 - Insert main.py in frappe app
 - Configure which doctypes are going be monitored inside the file main.py
 
After the configuration the method runs automatically once someone made a change
 
## Functionality
Each created doc trigger the function, which verify if the doctype is in monitored list, once validated, the method send the e-mail notification

## Pending
 - Capture doc in monitored list
