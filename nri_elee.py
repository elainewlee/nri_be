
#* The program should prompt the user for the number of questions to put in the quiz. Any integer value greater than 0 is acceptable.
import sys, csv #, argparse
from sys import argv

#make the raw input into an integer, for comparison below
num_q = int(raw_input("How many questions would you like in the quiz? ")) 

if num_q > 0:
	print "This quiz will have %d questions." % (num_q)
else:
	print "Please enter a value greater than 0."

# * The expected output is to display a list of question_ids.
# open questions.csv file
script, qfile = argv
# print "These are the question_ids in the %s file:" % qfile #sanity check

strand_id_list = []
strand_id_count	= () #create an empty set of unique strand ids
standard_id_list = []
standard_id_count	= () #create an empty set of unique standard ids

with open('questions.csv', 'rb') as qfile:
	reader = csv.reader(qfile)
	# print "reader = %r" % reader
	next(reader, None)# skip header row

	for r in reader: 
# * Use each strand as close as possible to an equal number of times. (e.g. There are two strands, so if the user asks for a 3 question quiz, it's okay to choose one strand twice and the other once.)		
		str_id = r[0] #strand is the 1st column in the .csv file
		print "str_id = %r" % str_id 
		strand_id_list.append(str_id) #append strand_id in file to a list to record all strand ids
		print "strand_id_list.append %r " % strand_id_list  #sanity check
		strand_id_count	= set(strand_id_list) #record unique strand ids to a set
		print "strand_id_count %r " % strand_id_count  #sanity check
# * Use each standard as close as possible to an equal number of times.
		std_id = r[2] #standard_id is the 3rd column in the .csv file
		print "std_id = %r" % std_id
		standard_id_list.append(std_id) 
		print "standard_id_list.append %r " % standard_id_list  
		standard_id_count	= set(standard_id_list) 
		print "standard_id_count %r " % standard_id_count 

# * Without the usage file, prefer questions that have not yet been assigned.
		# q_id = r[4] #question_id is the 4th column in the .csv file
		# print repr(q_id)


# * Duplicating questions in the quiz is OKAY, if the quiz requires more questions than are available with even distribution!