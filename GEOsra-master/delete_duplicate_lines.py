# import csv 
# with open ('/Users/Carol/Desktop/test_out02.csv','rU') as data, open ('out2.csv','w') as out:
# 	data=csv.reader(f1)
# 	#next(data, None) 	

#_____###
# linhas duplicadas###
lines_seen = set() # holds lines already seen
outfile = open('/Users/Carol/Documents/SRA_RNA-seq_GEO/search_geo_pl_py/gse_category_classifier_text_mining_out1.csv','w')
for line in open('/Users/Carol/Documents/SRA_RNA-seq_GEO/search_geo_pl_py/gse_category_classifier_text_mining_out.csv','rU'):
    if line not in lines_seen: 
        outfile.write(line)
        lines_seen.add(line)
outfile.close()

##_____###
# import csv

# with open ('/Users/Carol/Documents/SRA_RNA-seq_GEO/gse_gsm_descrpi_type_RNAseq.csv','rU') as f1, open ('rna_out3.csv','w') as out:
#  	data=csv.reader(f1)
#  	next(data, None) 
#  	string=('GSM')
#  	for line in data:
#  		for line[0] in line:
#  			if any(s in line[0] for s in string):
#  				print(line)
#  				out.write(str(line))
# ##getting line count
# # def file_len(fname):
# #     with open(fname) as f:
# #         for i, l in enumerate(f):
# #             pass
# #     return i + 1