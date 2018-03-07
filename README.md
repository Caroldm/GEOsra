
# GEOsra 

------------------------------------------------------------------------------------------------------------------------



Files:

1) esummary_xml.zip : esummary url xml result from esearch url IDs (WebEnv & Key).

2) gse_gsm_description_all_samples.csv : All 174549 samples from the 7876 GEO studies with SRA supplemental files for Human, Mouse and Rat.




Scripts

1) Query geo API, 2 scripts are needed geo.py and geo.pl
 - Python scripts calls the perl script that will perm the query and return the txt output to geo.py. Only lines that contain 
 usefull information for the db will be keep and unnecessary words deleted, replaced, cleaned. And then output  it to an  spreadsheet.

2) delete_duplicate_lines.py : script that will delete any duplicated lines ....

3) organizing_data_columns_to_rows.py : organizing spreadsheet data, from text to columns.

4) creating_sql_queries.py: INSERT INTO WHERE....



------------------------------------------------------------------------------------------------------------------------

! Will continue adding and organizing soon.

Back in 2016 I had a working GEOsra website. Luckly still got all the files and scripts but will have to start over on joomla online now. SO under construction https://geosra.joomla.com/ 
