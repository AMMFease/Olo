#!/usr/bin/python3
# encoding: utf-8

thisVersion = "v001"


#######################################################################################
## This file contains test suites, tests and associated utilties for the Olo Challenge.
##
## Please read the README.md and TestPlan.txt documents for requirements, test plan and
## notes for current restrictions and future enhancements.
##
## v001 - Initial version with starter utilities and first test use case (get posts).
#######################################################################################


#######################################################################################
## Imports
#######################################################################################
import requests


#######################################################################################
## Global variables
#######################################################################################
BaseUrl = "https://jsonplaceholder.typicode.com/"  # URL for JSONPlaceholder.

RunSetup = True     # Should the test case/suite run setup?
RunTeardown = True  # Should the test case/suite run teardown?

class APICall:      # Types of API calls exercised by this test suite.
    GET = 1
    POST = 2
    PUT = 3
    DELETE = 4


#######################################################################################
## Utilities
#######################################################################################

## Set up the SUT.
def setup():
    print("\nInitializing system...")
    
## Clean up the SUT.
def teardown():
    print("\nCleaning up system...")
    
## Make the API call and print the results.    
def callAPI(callType, callParams):
    url = "%s%s" % (BaseUrl, callParams) 
    
    if (callType == APICall.GET):
        print("\nAttempting GET call '%s'" % url)
        response = requests.get(url)   
    elif (callType == APICall.POST):
        print("not yet implemented")
    elif (callType == APICall.PUT):
        print("not yet implemented")
    elif (callType == APICall.DELETE):
        print("not yet implemented")
    else:
        print("Illegal value")
        
    # Print the results.
    # Success API return calls are 200 (OK) and 201 (Created).   
    print("Return code = %d" % response.status_code)     # Print http response code.
    print("Returned JSON response:\n%s" % response.text) # Print formatted JSON response. 
    
    # Return test results - success or failure.
    if ((response.status_code == 200) or (response.status_code == 201)):
        return True
    else:
        return False


#######################################################################################
## Tests
#######################################################################################
## Test "GET posts".
def testGet():
    setup()
    success = callAPI(APICall.GET, "posts")
    if (success):
        print("\n*** Test testGet() completed successfully. ***")
    else:
        print("\n*** Test testGet() failed. ***")
    teardown()
    
#######################################################################################
## Test Suites
#######################################################################################
print("\nBegin tests ....")
testGet()
print("\nTest execution complete.")


