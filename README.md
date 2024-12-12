# CISC 4900 Project

# Description
This is my CISC 4900 Project, supervised by Professor Hui Chen. 

The files that are being uploaded here are the tasks I work on in the supervised project and are constantly updated as I work on the project: Webvulmap(Mapping Security Vulnerability between Computer Science Body of Knowledge). 
The main repository is owned by my supervisor aka Professor Hui Chen, the public repository is linked here: https://github.com/RealVulnerabilityEdu/webvulmap/commits/main/

Project website: https://secwebmap.streamlit.app

Please note that both private and public repositories are the same, once the changes have been committed in the private repository it will then be done the same with the public repository. Afterwards I will then upload the files to this current repository to showcase it. My Repository > Private > Public > My Repository
The reason behind having two repositories is because of privacy reasons.

## Mapping Web App
The web application maps between software security topics (CWEs and CVEs)
and CS curriculum topics. It serves two main goals:

1. It allows instructors or learners understand what prerequisite material is
	 needed to help teach/learn about certain secure programming topics in terms
	 of CWEs and CVEs, and
2. It also helps them locate real world examples, such as CWEs and CVEs
	 relevant to a course topic.

With this tool, one can learn what common language (i.e. c++, SQL) and
knowledge are associated with a known secure vulnerability (e.g., a CWE or a
CVE) and follows up with web sources to learn more. For instance, learners are
currently studying a topic in interested in their course, such as, Classic
Buffer Overflow (a Knowledge Topic). This tool can informs the learners that
this problem is commonly observed in programming languages like C/C++, and
secure vulnerabilities caused by this problem is often categorized as CWE-120
Classic Buffer Overflow. The tool links to CVE instances in this CWE, such as
CVE-2000-1094, i.e.,  a Buffer Overflow bug in AOL Instant Messenger (AIM)
before 4.3.2229 allows remote attackers to execute arbitrary commands via a
"buddyicon" command with a long "src" argument (source:[https://nvd.nist.gov/vuln/detail/CVE-2000-1094](https://nvd.nist.gov/vuln/detail/CVE-2000-1094))

## Technologies Used
Python and HTML/CSS
Generally, we will manually map a small set of topics/software security topic, and use it to train a machine learning model to map the rest.


## Tasks that I will be doing

1. To create the map between computer science knowledge topics and
software security topics

2. To enhance the web application when 1 is done


Task 1: Familiarize with the processing pipeline of parsing a knowledge area. The input to the pipeline is the CS2013 pdf file, and the output is a JSON file for the selected knowledge area.

Task 2: To develop a Python program that takes a JSON file as input. The program of the output is a single JSON object that contains all the KAs. This program should build upon the existing programs. 
My approach to it is to manually add/read in the json files for now, then use a forloop to iterate to load the files and have them all dumped into the python dictionary list. 

Task 3: To facilitate JSONinifying the curriculum document, a PDF file to a JSON object, we are creating a metadata file that specifies, Knowledge Area's begin and end page numbers in the PDF file. 
	Also write a Python script that validates the integrity of the file.

Task 4: Use the csv file in Task 3 as the input, and produce a single JSON file for the curriculum that contains all the knowledge areas using a python/shell script. My approach to this was using python and imported task 3's validate csv program into this script.It takes in the csv file as input, validates it and converts it to json file. If validation fails it will then return back. 
