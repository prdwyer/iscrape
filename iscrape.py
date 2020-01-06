import os
import sys
import argparse
import os.path
import subprocess
from ioc_finder import find_iocs

#dependencies pdfminer and ioc-finder




if __name__ == '__main__':


	parser = argparse.ArgumentParser(description='iocs from documents')
	parser.add_argument("-f","--file", dest="doc", default=None, help="file to search")
	args = parser.parse_args()
	filename = args.doc
	extension = os.path.splitext(filename)[-1]

	if "pdf" in extension:
		cmd = "pdf2txt.py " +args.doc	
		text = subprocess.getoutput(cmd)
		iocs = find_iocs(text)
	
		report = ""
		report = args.doc + "\n\n"

		for ioc in iocs:
			output = ""
			for thing in iocs[ioc]:
				output += thing+"\n"
				#print(thing)

			if output:
				output = ioc +":\n"+ output
				report += output+"\n"
		
		print(report)

	elif ("doc" or "ppt")in extension:
		print("doc file")	
	else:
		cmd = "cat " +args.doc	
		text = subprocess.getoutput(cmd)
		iocs = find_iocs(text)
	
		report = ""
		report = args.doc + "\n\n"

		for ioc in iocs:
			output = ""
			for thing in iocs[ioc]:
				output += thing+"\n"
				#print(thing)

			if output:
				output = ioc +":\n"+ output
				report += output+"\n"
		
		print(report)
