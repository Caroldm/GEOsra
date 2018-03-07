#1) Call perl script and execute it (have to keep it in the same folder-path)
import subprocess, sys

perl = "/usr/bin/perl"
perl_script = "geo.pl";
params = "--mount-doom-hot"
pl_script = subprocess.Popen([perl, perl_script, params], stdout=sys.stdout)
pl_script.communicate()

## 2) input the output from the perl script but only the wanted data.
import re

del_list = ['>','PDAT','<','Type="String"','Item Name=','/Item','"','</Item>','<DocSum>','<Item Name=','DocSum']

# I want to keep the rest of the line but not these words.
words = ['"Accession" Type="String">GSE','<Item Name="title" Type="String">','taxon','<Item Name="PDAT" Type="String">','Type="String">GSM','<Item Name="Title" Type="String">','<Item Name="n_samples" Type="Integer">','<Item Name="RelationType" Type="String">', '<Item Name="summary" Type="String">']

rep = re.compile(r'|'.join(del_list))
keep = re.compile(r"|".join(words))
r3 = re.compile("GSE(?=\d)")

with open("geo_sra.txt") as f, open("email_data.txt","w") as out:
    for line in f:
         # if line contains match from words
        if keep.search(line):
            # replace all unwanted substrings
            line=line.replace("PDAT","Date\t")
            line = rep.sub("", line.lstrip())
            line=line.replace("taxon","taxon\t")
            line=line.replace("title","Study title\t")
            line=line.replace("Title","Title\t ")
            line=line.replace("RelationType","RelationType\t")
            line=line.replace("n_samples Type=Integer", "Number_of_Samples\t")
            line= line.replace("Accession GSM", "GSM\tGSM")
            line=line.replace("Accession","\nAccession\t")
            line=line.replace("summary","Summary\t")
            line = r3.sub('http://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE', line)
            out.write(line)

### 6) Send results by email
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

fromaddr = "geo.weekly.analysis@gmail.com"
toaddr = "carol.dmonteiro@gmail.com"
#toaddr = "-----@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "GEO Data Sets - SRA search"

# send txt file in email body
f6 = (open("email_data.txt",'rU'))
geo = MIMEText(f6.read(),'plain') 
f6.close()
msg.attach(geo)

#convert to strin
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login("geo.weekly.analysis", "geoweekly")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
