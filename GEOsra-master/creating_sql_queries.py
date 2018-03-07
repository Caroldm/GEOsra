import csv

with open ('/Users/Carol/Documents/SRA_RNA-seq_GEO/search_geo_pl_py/organized_geo_query.csv','rU') as f1, open ("/Users/Carol/Desktop/gsm_to_gse_all_samples1.sql",'w') as output:
	data=csv.reader(f1)
	#next(data, None) 	

	# for line in data:
	# 	id_ac=line[0]
	# 	accession=line[1]
	# 	sample=line[2]
	# 	description=line[3]
	# 	sample_type=line[4]
	# 	#print(cell_lines)


	# 	out="""
	# 	INSERT INTO `sample_gse` (`gsm`,`description`)
	# 	VALUES (
	#   		(SELECT `gsm` FROM `gsm` WHERE `sample` = "%s"), 
	#   		(SELECT `description` FROM `gsm` WHERE `accession` = "%s")
	# 	); 
	# 	""" %(sample,accession)	
	# 	output.write(out)
	# 	print(out)


	for line in data:
		accession=line[0]
		sample=line[1]
		description=line[2]
		#print(cell_lines)

		out="""
		INSERT INTO `gsm` (`accession`,`sample`,`description`)
		VALUES('%s', '%s', '%s');
		""" %(accession,sample,description)

		output.write(out)
		#print(out)