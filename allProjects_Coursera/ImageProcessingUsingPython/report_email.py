###############report_email.py###################
#!/usr/bin/env python3
import reports
import os
#from datetime import datetime
import emails
import datetime
if __name__ == "__main__":
    desc = "/home/student-01-72557e2aabe5/supplier-data/description$
    d = datetime.datetime.now().date()
    datestr = d.strftime('%b %d, %Y')

    title = "Processed Update on {}".format(datestr)
    table_data = []
    table_list = []
    for files in os.listdir(desc):
        filename = desc + files
        with open(filename, 'r') as f:
            reads = f.readlines()
        name = reads[0].strip()
        weight = reads[1].strip()

        table_list.append({"name":name, "weight":weight})
    for tables in table_list:
        for k,v in tables.items():
            table_data.append([k,v])
    print(table_data)
    reports.generate_report(title,table_data, "/tmp/processed.pdf")
    sender = "automation@example.com"
    receiver = "student-01-72557e2aabe5@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A $

    message = emails.generate_email(sender, receiver, subject, body$
    emails.send_email(message)
