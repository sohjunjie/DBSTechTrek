import json
import requests

# get nric from api
# manual input - spouse nric, joint monthly income
# get credit scores ?? from nric
# using credit scores, get a house for the couple ??

def getHouses(s_nric, income) :
	#get auth code
	#get access token
	access_token = "abc123"
	auth_code = "idontknow"
	
	url = 'https://www.dbs.com/sandbox/api/sg/v1/mortgages/calculateHDBAffordability'
	headers = {
	'Content-Type': 'application/json',
    'clientId': 'clientId2',
    'accessToken ': access_token }
	
	json.dumps({"homeLoanApplicants":{"dateOfBirth":"1988-01-01", "fixedMonthlyIncome": {"amount": income} } })
	
	#data = '{"homeLoanApplicants":[{"homeLoanApplicant":{"dateOfBirth":"1988-08-10","financialCommitment":{"carLoan":{"amount":500,"currency":"SGD"},"homeLoan":{"amount":1000,"currency":"SGD"},"otherLoans":{"amount":300,"currency":"SGD"}},"fixedMonthlyIncome":{"amount":4566,"currency":"SGD"},"isMainApplicant":true,"otherMonthlyIncome":{"amount":1000,"currency":"SGD"}}}]}'
	data = json.dumps({"homeLoanApplicants":{"dateOfBirth":"1988-01-01", "fixedMonthlyIncome": {"amount": income}}})
	print (data)
	ret = requests.post(url, headers = headers, data = json.dumps({"homeLoanApplicants":{"dateOfBirth":"1988-01-01", "fixedMonthlyIncome": {"amount": income}}}))
	print (ret.text)