################reports.py #####to create reports
#!/usr/bin/env python3


import reportlab
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,T$

def generate_report(title,table_data, filename):
    styles = getSampleStyleSheet()
    report_title = Paragraph(title,styles["h1"])
    table_style = [('GRID', (0,0),(-1,-1),1,colors.black)]
    report_table = Table(data=table_data, style=table_style,hAlign=$
    report = SimpleDocTemplate(filename)
    report.build([report_title, report_table])
