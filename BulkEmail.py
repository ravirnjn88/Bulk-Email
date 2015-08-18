
import smtplib
from auth import *

def sendmail(receivers,name):

	sender = 'ravi.ranjan.eee11@iitbhu.ac.in'
	from_add ="Ravi Ranjan <ravi.ranjan.eee11@iitbhu.ac.in>"
	to_add = "<%s>" % (receivers)
	subj = "Some clarifications needed!"
	message_text = """Hi %s <br>
	<br>
	I am Abhijeet, Senior year student at Indian Institute of Technology (BHU) Varanasi. I intend to apply for masters (with specialization in computer vision) at UMass.<br>
	<br>
	Just needed to know if the prospects are good this year or not. <br>
	<br>
	My resume is <a href="https://drive.google.com/file/d/0B03d7H_NFM9tX2dXaThDQ3I2dEE/view?usp=sharing"> here </a> <br>
	<br>
	If possible, do reply.  I am quite perplexed by the current unpredictable scenario of graduate admissions.Just need your speculations here a bit. That would be a vital help for me.<br>
	<br>
	Cheers,<br>
	Abhijeet Kislay
	""" % (name)

	msg = "From: %s\nTo: %s \nMIME-Version: 1.0\nContent-type: text/html\nSubject: %s\n\n%s" % ( from_add, to_add, subj, message_text)


	
	
	smtpObj = smtplib.SMTP('smtp.gmail.com',587)
	print "step1"
	smtpObj.starttls()
	print "step2"
	smtpObj.login(credential[0],credential[1])
	print "step3"
	smtpObj.sendmail(sender, receivers, msg)
	smtpObj.quit()        
	print "Successfully sent email"

fo = open("id.txt","r")

for lines in fo.readlines():
	sendmail(lines.split()[0],lines.split()[1]) 

#sendmail("ravirnjn88@gmail.com","ranjan")
