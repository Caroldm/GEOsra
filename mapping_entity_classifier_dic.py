import sys
import csv 
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob

with open('/Users/Carol/Desktop/GSM_musmusculus.csv','rU') as input_file, open('/Users/Carol/Desktop/class_MM_gsm_assay.csv','w') as output:
	data = csv.reader(input_file)
	

# CONTROLS list


	list_wds = [('RNA-Seq','RNASEQ'),('RNA-Seq','rnaseq'),('RNA-Seq','RNA_SEQ'),('RNA-Seq','rna-seq'),('RNA-Seq','rna sequencing'),('RNA-Seq','RNA SEQUENCING'),
	('RNA-Seq','RNA Sequencing'),('RNA-Seq','RNA sequencing'),('RNA-Seq','RNA seq'),('RNA-Seq','RNA Seq'),
	('ChIP-Seq','chip-seq'),('ChIP-Seq','ChIP-Seq'),('ChIP-Seq','Chip-seq'),('ChIP-Seq','CHIP_SEQ'),('ChIP-Seq','Chipseq'),
	('ChIP-Seq','CHIPseq'),('ChIP-Seq','ChIPSeq'),('ChIP-Seq','ChIPSeq'),('ChIP-Seq','ChIP-seq'),('ChIP-Seq','ChIPSeq'),
	('ChIP-Seq','ChIPSEQ'),('ChIP-Seq','ChIPSeq')]

	# list_wds = [
	# ('control', 'Control'),
	# ('Control', 'Control'),
	# ('CONTROL', 'Control'),
	# ('crtl', 'Control'),
	# ('CTRL', 'Control'),
	# ('DMSO treated', 'Control'),
	# ('DMSO TREATED', 'Control'),
	# ('dmso treated', 'Control'),
	# ('DMSO', 'Control'),
	# ('dmso', 'Control'),
	# ('Healthy', 'Control'),
	# ('healthy', 'Control'),
	# ('Healthy', 'Control'),
	# ('no treatment', 'Control'),
	# ('No treatment', 'Control'),
	# ('NO TREATMENT', 'Control'),
	# ('nonstimulated', 'Control'),
	# ('normal', 'Control'),
	# ('NORMAL', 'Control'),
	# ('Normal', 'Control'),
	# ('Untreated', 'Control'),
	# ('Untreated', 'Control'),
	# ('UNTREATED', 'Control'),
	# ('untreated', 'Control'),
	# ('veh', 'Control'),
	# ('Vehicle', 'Control'),
	# ('vehicle', 'Control'),
	# ('Vehicle treated', 'Control'),
	# ('vehicle treated', 'Control'),
	# ('veh treated', 'Control'),
	# ('veh treatment', 'Control'),
	# ('Vehicle Treatment', 'Control'),
	# ('vehicle TREATMENT', 'Control'),
	# ('wild type', 'Control'),
	# ('Wild Type', 'Control'),
	# ('WILD TYPE', 'Control'),
	# ('wild-type', 'Control'),
	# ('wt', 'Control'),
	# ('WT', 'Control'),
	# ('young', 'Control'),
	# ('Young', 'Control'),
	# ('Saline', 'Control'),
	# ('SALINE', 'Control'),
	# ('saline', 'Control'),
	# ('Saline Treated', 'Control'),
	# ('Saline treated', 'Control'),
	# ('Saline TREATED', 'Control'),
	# ('SALINE TREATED', 'Control'),
	# ('SALINE treated', 'Control'),
	# ('SALINE Treated', 'Control'),
	# ('saline treated', 'Control'),
	# ('saline Treated', 'Control'),
	# ('saline TREATED', 'Control'),
	# ('Saline Treatment', 'Control'),
	# ('Saline treatment', 'Control'),
	# ('Saline TREATMENT', 'Control'),
	# ('SALINE TREATMENT', 'Control'),
	# ('SALINE treatment', 'Control'),
	# ('SALINE Treatment', 'Control'),
	# ('saline treatment', 'Control'),
	# ('saline Treatment', 'Control'),
	# ('saline TREATMENT', 'Control'),
	# ('Unlesioned', 'Control'),
	# ('UNLISIONED', 'Control'),
	# ('unlisioned', 'Control'),
	# ('CTRL', 'Control'),
	# ('ctrl', 'Control'),
	# ('Ctrl', 'Control'),
	# ('pre-prednisolon', 'Control'),
	# ('Normoxia', 'Control'),
	# ('NORMOXIA', 'Control'),
	# ('normoxia', 'Control'),
	# ('Negative Control', 'Control'),
	# ('NEGATIVE CONTROL', 'Control'),
	# ('negative control', 'Control'),
	# ('uninfected','Control'),
	# ('Uninfected','Control'),
	# ('UNINFECTED','Control'),
	# ('shControl','Control'),
	# ('shcontrol','Control'),
	# ('shCTRL','Control'),
	# ('shCtrl','Control'),
	# ('Before','Control'),
	# ('before', 'Control')
	]
#usei pra fazer a apresentacao
	test=[]
	for line in data:
	#print(line[3])
		sample=line[2]
		description=line[3]
		blob=TextBlob(description)
		text_words=(blob.words)
		#print(text_words)
		for wds in list_wds:
		#print(wds)
			for word in text_words:
			#print(word)
				if word in wds:
					print(line[0] + line[1] + line[2] + word)
					a = (line[1] + ',' + line[2] +',' + line[3] +','+ word + ',' + '\n')
					output.write(line[1]+','+ line[2]+','+line[3]+','+word+','+'\n')
					



