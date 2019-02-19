import sys
import os
import time


#class Hypothesis
class Hypothesis:
#make init function for all the init variables
	def __init__(self, prior, chr, lim):
		self.prior = prior
		self.chr = chr
		self.lim = lim
		self.prior = prior

def createHypothesis():
	hyp1 = Hypothesis(0.1,1.0,0.0)
	hyp2 = Hypothesis(0.2, 0.75, 0.25)
	hyp3 = Hypothesis(0.4, 0.5, 0.5)
	hyp4 = Hypothesis(0.2, 0.25, 0.75)
	hyp5 = Hypothesis(0.1, 0.0, 1.0)
	return hyp1,hyp2,hyp3,hyp4,hyp5
	
def displayfile():
    r_file = open("result1.txt", 'w')
	#r_file.close()
	
def checkprior():
    #check if prior value is present or not
	probabilityofpriorvalue = 0.0
	print("Hypothesis made")
	
	
def main():
	if (len(sys.argv) > 2):
		print ('Command to run python task1.py <Observation String>')
		sys.exit(0)	
	r_file = open("result.txt", 'w')	
	# Creating a result file for storing the result
#	Create hypothesis 
	hyp1,hyp2,hyp3,hyp4,hyp5 = createHypothesis()
	#print(hyp1,hyp2,hyp3,hyp4,hyp5)
	#check if the length is not equal to 2
	if (len(sys.argv) != 2):
		try:
		# write to the file the probabilities
			r_file.write('Observation sequence Q: \r\n');
			r_file.write('Length of Q: 0\r\n\n');
			# Writnig the results for the final probability of each hypothesis
			r_file.write("P(hyp1 | Q) = %.5f \r\n" % (hyp1.prior))
			r_file.write("P(hyp2 | Q) = %.5f \r\n" % (hyp2.prior))
			r_file.write("P(hyp3 | Q) = %.5f \r\n" % (hyp3.prior))
			r_file.write("P(hyp4 | Q) = %.5f \r\n" % (hyp4.prior))
			r_file.write("P(hyp5 | Q) = %.5f \r\n\n" % (hyp5.prior))
			r_file.write("Probability that the next candy we pick will be chr, given Q: 0.50000\r\n")
			r_file.write("Probability that the next candy we pick will be lim, given Q: 0.50000\r\n")
			r_file.close()
		except Exception:
			print ('Error creating a file')
			r_file.close()
		sys.exit(0)
		#If cannot create a file exit the system
	observation = sys.argv[1]  #get observation string from the user
	print("The observation string is-------------")
	print(observation)
	len_of_obs_string = len(observation) 	# getting teh length of the string
	count_candy = 0
	count_lim = 0
	count_z = 0
	new_prior = 0.0
	prior_already = 0.0
	probabilityofC0 = 0.0
	probabilityofL0 = 0.0
	r_file.write('Observation sequence is : ' + observation + '\r\n');
	r_file.write('Length of observation string is: ' + str(len_of_obs_string) + '\r\n\n');
	r_file.write('Length of OBS tring:'+str(len_of_obs_string)+'\n');
	for i in range(0, len_of_obs_string):
		#print("reached")
		probabilityofC0 = (hyp1.prior*hyp1.chr) + (hyp2.prior*hyp2.chr) + (hyp3.prior*hyp3.chr) + (hyp4.prior*hyp4.chr) + (hyp5.prior*hyp5.chr)
		probabilityofL0 = (hyp1.prior*hyp1.lim) + (hyp2.prior*hyp2.lim) + (hyp3.prior*hyp3.lim) + (hyp4.prior*hyp4.lim) + (hyp5.prior*hyp5.lim)
		if (observation[i] == 'c' or observation[i] == 'C'):
			new_prior = ( (hyp1.chr * hyp1.prior) / probabilityofC0);
			hyp1.prior = new_prior
			new_prior = ( (hyp2.chr * hyp2.prior) / probabilityofC0);
			hyp2.prior = new_prior
			new_prior = ( (hyp3.chr * hyp3.prior) / probabilityofC0);
			hyp3.prior = new_prior
			new_prior = ( (hyp4.chr * hyp4.prior) / probabilityofC0);
			hyp4.prior = new_prior
			new_prior = ( (hyp5.chr * hyp5.prior) / probabilityofC0);
			hyp5.prior = new_prior
			count_candy = count_candy + 1;
			#print("reached")
		elif (observation[i] == 'l' or observation[i] == 'L'):
			new_prior = ( (hyp1.lim * hyp1.prior) / probabilityofL0);
			hyp1.prior = new_prior
			new_prior = ( (hyp2.lim * hyp2.prior) / probabilityofL0);
			hyp2.prior = new_prior
			new_prior = ( (hyp3.lim * hyp3.prior) / probabilityofL0);
			hyp3.prior = new_prior
			new_prior = ( (hyp4.lim * hyp4.prior) / probabilityofL0);
			hyp4.prior = new_prior
			new_prior = ( (hyp5.lim * hyp5.prior) / probabilityofL0);
			hyp5.prior = new_prior
			count_lim = count_lim + 1;
		else:
		    #print("reached")
			print ('The inputs can only be a combination of C/c or L/l')
			r_file.close();
			#sys.exit(0)
		probabilityofL0 = (hyp1.prior*hyp1.lim) + (hyp2.prior*hyp2.lim) + (hyp3.prior*hyp3.lim) + (hyp4.prior*hyp4.lim) + (hyp5.prior*hyp5.lim)
		probabilityofC0 = (hyp1.prior*hyp1.chr) + (hyp2.prior*hyp2.chr) + (hyp3.prior*hyp3.chr) + (hyp4.prior*hyp4.chr) + (hyp5.prior*hyp5.chr)
		try:
			print("The Second try")
			# Writnig the results for the final probability of each hypothesis
			r_file.write("After Observation %d = %s\n" %(i+1,observation[i]))
			r_file.write("P(hyp1 | Q) = %.6f \r\n" %(hyp1.prior))
			r_file.write("P(hyp2 | Q) = %.6f \r\n" %(hyp2.prior))
			r_file.write("P(hyp3 | Q) = %.6f \r\n" %(hyp3.prior))
			r_file.write("P(hyp4 | Q) = %.6f \r\n" %(hyp4.prior))
			r_file.write("P(hyp5 | Q) = %.6f \r\n\n" %(hyp5.prior))
			#print("reached")
			r_file.write("Probability that the next candy we pick will be lim, given Q: %.6f \r\n" %(probabilityofL0))
			r_file.write("Probability that the next candy we pick will be chr, given Q: %.6f \r\n" %(probabilityofC0))
			

		except Exception:
			print ("Error creating a file")
			r_file.close()
	r_file.close()


if (__name__ == '__main__'):
	main()