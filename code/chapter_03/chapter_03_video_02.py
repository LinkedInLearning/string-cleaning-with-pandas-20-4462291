import pandas as pd
import re

report_files = [
    './company_reports/zarp-9_85.txt',
    './company_reports/zag_12_15.txt',
    './company_zeport/zlob_06_06.txt',
    './company_reportz/znome_07_10.txt'
]
# I need to find the company names
# that start with a z in report files:
# zarp, zag, zlob, znome
re.search(r'z\w+', report_files[0]).group(0) # Copilot generated

[re.search(r'z\w+', x).group(0) for x in report_files] # You'll see the issue

[re.search(r'\w{3,5}(?=[-_]\d)', x).group(0) for x in report_files] # Human generated