# import csv 
# from textblob.classifiers import NaiveBayesClassifier
# from textblob import TextBlob


# train = [
#     ('I love this sandwich.', 'pos'),
#     ('This is an amazing place!', 'pos'),
#     ('I feel very good about these beers.', 'pos'),
#     ('This is my best work.', 'pos'),
#     ("What an awesome view", 'pos'),
#     ('I do not like this restaurant', 'neg'),
#     ('I am tired of this stuff.', 'neg'),
#     ("I can't deal with this", 'neg'),
#     ('He is my sworn enemy!', 'neg'),
#     ('My boss is horrible.', 'neg')
# ]
# test = [
#     ('The beer was good.', 'pos'),
#     ('I do not enjoy my job', 'neg'),
#     ("I ain't feeling dandy today.", 'neg'),
#     ("I feel amazing!", 'pos'),
#     ('Gary is a friend of mine.', 'pos'),
#     ("I can't believe I'm doing this.", 'neg')
# ]

# cl = NaiveBayesClassifier(train)

# # Classify some text
# print(cl.classify("Their burgers are amazing."))  # "pos"
# print(cl.classify("I don't like their pizza."))   # "neg"

# # Classify a TextBlob
# blob = TextBlob("The beer was amazing. But the hangover was horrible. "
#                 "My boss was not pleased.", classifier=cl)
# print(blob)
# print(blob.classify())

# for sentence in blob.sentences:
#     print(sentence)
#     print(sentence.classify())

# # Compute accuracy
# print("Accuracy: {0}".format(cl.accuracy(test)))

# # Show 5 most informative features
# cl.show_informative_features(5)

import csv 
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob

with open('/Users/Carol/Documents/SRA_RNA-seq_GEO/search_geo_pl_py/summary_for_classifier.csv','rU') as input_file, open('/Users/Carol/Documents/SRA_RNA-seq_GEO/search_geo_pl_py/database_data_study_category_classifier.csv','w') as output:
	data = csv.reader(input_file)
	
	list_wds = [
	('RNASEQ','RNA-Seq'),
	('rnaseq','RNA-Seq'),
	('RNA_SEQ','RNA-Seq'),
	('rna-seq','RNA-Seq'),
	('rna sequencing','RNA-Seq'),
	('RNA SEQUENCING','RNA-Seq'),
	('RNA Sequencing','RNA-Seq'),
	('RNA sequencing','RNA-Seq'),
	('RNA seq','RNA-Seq'),
	('RNA Seq','RNA-Seq'),
	('chip-seq','ChIP-Seq'),
	('ChIP-Seq','ChIP-Seq'),
	('Chip-seq','ChIP-Seq'),
	('CHIP_SEQ','ChIP-Seq'),
	('Chipseq','ChIP-Seq'),
	('CHIPseq','ChIP-Seq'),
	('ChIPSeq','ChIP-Seq'),
	('ChIPSeq','ChIP-Seq'),
	('ChIP-seq','ChIP-Seq'),
	('ChIPSeq','ChIP-Seq'),
	('ChIPSEQ','ChIP-Seq'),
	('ChIPSeq','ChIP-Seq')
	]

	cl = NaiveBayesClassifier(list_wds)

	
	
	# test=[]
	# for line in data:
	# 	#print(line[0])
	# 	description=line[0]
	# 	#test=description.split()
	# 	test=description
	# 	print([test])
	# 	#blob=TextBlob(test)
	# 	#print(blob)
	# 	# from textblob import TextBlob
	# 	# blob=TextBlob(test)
	# 	for sentence in test:
	# 		print(sentence)
	# 		print(sentence.classify())

	test=[]
	for line in data:
		# print(line[0])
		description=line[1]
		blob=TextBlob(description)
		text_words=(blob.words)
		for wds in list_wds:
			#print(wds)
			for word in text_words:
				#print(word)
				if word in wds:
					print(line[0],word)

	