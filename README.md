
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
------------------------------------------------------------------------------------------------------------------------

! Will continue adding and organizing soon.

Back in 2016 I had a working GEOsra website. Luckly still got all the files and scripts but will have to start over on joomla online now. SO under construction https://geosra.joomla.com/ 

------------------------------------------------------------------------------------------------------------------------

# The main objective was to
Use the available SRA data from GEO studies to create a database that fulfills our current requirements for data and has a build in structure that facilitates the analysis.


# Current model
The current model is to just search GEO for a particular condition of interest... and then go through the search results one by one.  By doing this we end up looking  at various studies that are not relevant for that specific project, even when they are relevant they might not have enough samples or their samples might not have SRA files available and we’ll skip it.

Usually we’ll also go through a significant number of studies that have all the data necessary for the analysis available but do not fit the criteria for the project.  

To decide if that study is useful. I’ll have to open the page, read the title, probably the description and do a quick check on the samples to make sure what I’m looking even if not in the description is not mixed in the samples.

Essentially when all of that happens most of the work necessary to classify that GSE and its (samples and conditions) has already been done and we could have potentially analyzed it.

This actually leads to a big loss in time/ work and data.

But at the same time it’s impossible to create projects and tags for everything or to predict what studies, diseases, drugs or whatever else condition will be relevant for us  in the future.
Also depending on what you're interested in... the same GSE and its conditions may be organized into multiple different ways.

Still seeing the same GSE over and over again and not doing anything about it simply doesn’t feel right.

The database was created so the data and metadata could be saved, organized and characterized by (assay and sample conditions) in adequate form, structure and annotation for any number offuture analysis. 

With GEO Accession, source link, date added, assay type, number of samples, organism, title, summary, and conditions specific for each accession.

The studies GSEs are also linked to their samples GSMs that are classified by its specifities.

The database contains mouse, human studies for multiple assay types such as ATAC-seq, RNA-seq, Chip-seq, etc. 

then In the said future I can just search the database and pipe it to the analysis,with a lot less overhead, instead of going back and looking through everything again, categorizing the same study and samples again. Hopefully this would prevent or reduce this loss of time/data and speed up the process.


 
