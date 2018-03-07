import csv

with open('/Users/Carol/Documents/SRA_RNA-seq_GEO/search_geo_pl_py/email_data1.csv','rU') as f1, open('organized_geo_query.csv','w')as out:
	data = csv.reader(f1,)
	for line in data:
		info_title=line[0]
		info_meta=line[1]
		# print(info_title)
		if info_title =='Accession':
			a = info_meta
			#print(a)
		if info_title =='Study title':
			b = info_meta
			#print(a,b)
		# 	#print(a,b)
		if info_title == 'taxon':
			c = info_meta
			#print(a,c)
		if info_title == 'Date':
			d = info_meta
			#print(a,d)
		if info_title == 'GSM':
			e = info_meta
			print(a,e)
		if info_title == 'Summary':
			g = info_meta
			#print(a,g)

		if info_title == 'Number_of_Samples':
			h=info_meta
			print(a,h)
			print(b)

		if info_title == 'Title':
			i=info_meta
			print(a,i)
			
				
			out.write(a + ',' + e + ',' + i + '\n') 
			#out.write(str(line))
			#print(a + ',' + b + ',' + c + ',' + d + ',' + g + '\n')
		




		# # if info_title == 'Title':
		# # 	f = info_meta
			
		# 	#out.write(a + ',' + b + ',' + c + ',' + d +','+ e +','+ f +'\n')
			# out.write(a + ',' + b + ',' + c + ',' + d +',' + '%s"' + '\n') %g
			
		# # for row in reader:  
	 #            row[1] = f1.readline() # edit the 8th column 
	 #            writer.writerow(row)

	
