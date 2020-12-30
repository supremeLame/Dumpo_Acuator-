#!/usr/bin/python

import datetime
import requests
import urllib2
import time
import re
import sys


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# auditevents: Exposes audit events information for the current application. Requires an AuditEventRepository bean.
# beans:  Displays a complete list of all the Spring beans in your application.
# caches: Exposes available caches.
# conditions: Shows the conditions that were evaluated on configuration and auto-configuration classes and the reasons why they did or did not match.
# configprops:  Displays a collated list of all @ConfigurationProperties.
# env: Exposes properties from Spring Environment.
# flyway: Shows any Flyway database migrations that have been applied. Requires one or more Flyway beans.
# health: Shows application health information.
# httptrace: Displays HTTP trace information (by default, the last 100 HTTP request-response exchanges). Requires an HttpTraceRepository bean.
# info: Displays arbitrary application info.
# integrationgraph:  Shows the Spring Integration graph. Requires a dependency on spring-integration-core.
# loggers: Shows and modifies the configuration of loggers in the application.
# liquibase: Shows any Liquibase database migrations that have been applied. Requires one or more Liquibase beans.
# metrics: Shows metrics information for the current application.
# mappings: Displays a collated list of all @RequestMapping paths.
# scheduledtasks: Displays the scheduled tasks in your application.
# sessions: Allows retrieval and deletion of user sessions from a Spring Session-backed session store. Requires a Servlet-based web application using Spring Session.
# jolokia: Exposes JMX beans over HTTP (when Jolokia is on the classpath, not available for WebFlux). Requires a dependency on jolokia-core.
# logfile: Returns the contents of the logfile (if logging.file.name or logging.file.path properties have been set). 
# prometheus:  Exposes metrics in a format that can be scraped by a Prometheus server. Requires a dependency on micrometer-registry-prometheus.
# threaddump:  Performs a thread dump.
# hystrix.stream: Set of metrics it gathers about each HystrixCommand

# Jason endpoints 
jasonEndpointList=["auditevents","beans","caches","conditions","configprops","env","flyway","health","httptrace","info","integrationgraph","loggers","liquibase","metrics","mappings","scheduledtasks","sessions","jolokia","logfile","prometheus","threaddump","hystrix.stream"
]
# Binary endpoints 
binaryEndpoint = "heapdump" # Returns an hprof heap dump file.

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Get miliseconds to append to filename for multiple runs
thisNow = datetime.datetime.now() 

# Create file to write jason output
outputJason = open(thisNow.strftime("%f")+"_acuatorJason.txt", "w+")

# Create file to write binary output
outputBinary = open(thisNow.strftime("%f")+"_acuatorBinary.txt", "w+")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)


# Accepts input from command prompt 
target_url = raw_input("Please type host URL:")

if  not re.match(regex,target_url):
	
	print("URL is not valid, please try again\n")
	sys.exit()

# Adding actuator URL component
final_url = target_url+"/actuator/"

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print("\nRun connectivity test ...\n")

# Test connectivity
def internet_on():
    try:
        urllib2.urlopen(target_url, timeout=1)

        return True

    except urllib2.URLError as err: 
    
        return False

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Download all Jason Responses
if internet_on(): 
    # For each endpoint of the acutator get data and write a file
    for eachEnpoint in jasonEndpointList:
        # Fetch URL(s)
        rForJason = requests.get(final_url+eachEnpoint)
        rForJason.encoding = 'utf-8' # Set utf-8 for file processing
        # Adding file headers
        outputJason.write("\n---------------------------------------------\n")
        outputJason.write("URL fetched: "+final_url+eachEnpoint+"\n")
        outputJason.write("-----------------------------------------------\n")
        print("--------------------------------------------------------------------------\n")
        print("Querying endpoint: "+eachEnpoint+"\n")
        print("--------------------------------------------------------------------------\n")
        time.sleep(5) 
        # If the server returns and HTML and no Jason the endpoint is disabled
        if "text/html" in rForJason.headers["content-type"]: 
                    outputJason.write("Endpoint disabled or blocked:"+eachEnpoint+"\n")
                    print("Endpoint: "+eachEnpoint+" is disabled or blocked\n")
                    print("--------------------------------------------------------------------------\n")
                    time.sleep(5)  
        else:
                    print(rForJason.text)
                    outputJason.write(rForJason.text)
print("--------------------------------------------------------------------------\n")
print("\n Creating file: "+outputJason.name+" with Jason responses\n")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Download Binary Response
print("--------------------------------------------------------------------------\n")
print("Querying endpoint: "+binaryEndpoint+"\n")
print("--------------------------------------------------------------------------\n")

rForBinary = requests.get(final_url+binaryEndpoint)
rForBinary.encoding = 'utf-8' # Set utf-8 for file processing

if "text/html" in rForBinary.headers["content-type"]:

    print("Endpoint: "+binaryEndpoint+" is disabled or blocked:\n")
    print("--------------------------------------------------------------------------\n")
    outputBinary.write("--------------------------------------------------\n")
    outputBinary.write("URL fetched: "+final_url+binaryEndpoint+"\n")
    outputBinary.write("--------------------------------------------------\n")
    outputBinary.write("Endpoint: "+binaryEndpoint+" disabled or blocked: \n")
    
else:
    outputBinary.write(rForBinary.content)
    print("\n\nDownload finished...")
    outputBinary.write("--------------------------------------------------\n")
    outputBinary.write("URL fetched: "+final_url+binaryEndpoint+"\n")
    outputBinary.write("--------------------------------------------------\n")
    print("\n Creating file: "+outputBinary.name+" with binary response\n")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Running regex against the downloaded files
pattern1 = "crypto"
pattern2 = "username"
pattern3 = "password"
pattern4 = "credentials"
pattern5 = r"[a-zA-Z]+.java"
jasonFile = outputJason.read()

searchJasonResult = open(thisNow.strftime("%f")+"_JasonSearchResults.txt", "w+")
searchJasonResult.write('\n--------------------------------\n')	
searchJasonResult.write('\n---------------Jason Search Results ------------\n')	

searchJasonResult.write("\n---Pattern searched: "+pattern1+"-------------\n")

for line in jasonFile:
    for match in re.finditer(pattern1, line):
        searchJasonResult.write(line)

searchJasonResult.write("\n---Pattern searched: "+pattern2+"-------------\n")

for line in jasonFile:
    for match in re.finditer(pattern2, line):
        searchJasonResult.write(line)
        searchJasonResult.write(line)

searchJasonResult.write("\n---Pattern searched: "+pattern3+"-------------\n")

for line in jasonFile:
    for match in re.finditer(pattern3, line):
        searchJasonResult.write(line)
        searchJasonResult.write(line)

searchJasonResult.write("\n---Pattern searched: "+pattern4+"-------------\n")

for line in jasonFile:
    for match in re.finditer(pattern4, line):
        searchJasonResult.write(line)
        searchJasonResult.write(line)

searchJasonResult.write("\n---Pattern searched: "+pattern5+"-------------\n")

for line in jasonFile:
    for match in re.finditer(pattern5, line):
        searchJasonResult.write(line)

print("\n Creating file with regex results of Jason responses: "+searchJasonResult.name+"\n")



# Close files
searchJasonResult.close()
outputJason.close()
outputBinary.close()
# Sys exit
sys.exit()
