import json
import requests

# get nric from api
# manual input - spouse nric, joint monthly income
# get credit scores ?? from nric
# using credit scores, get a house for the couple ??

def getHouses(income) :
	print(income)
	headers = {
		'Content-Type': 'application/json',
		'clientId': 'clientId2',
		'accessToken': 'eyJhbGciOiJIUzI1NiJ9.eyJpc3MiIDogImh0dHBzOi8vY2FwaS5kYnMuY29tIiwiaWF0IiA6IDE1NDIzNDUzMTExMTEsICJleHAiIDogMTU0MjM0ODkxMTExMSwic3ViIiA6ICJTVmN3TXpZPSIsInB0eXR5cGUiIDogMSwiY2xuaWQiIDogImNsaWVudElkMiIsImNsbnR5cGUiIDogIjIiLCAiYWNjZXNzIiA6ICIxRkEiLCJzY29wZSIgOiAiMkZBLVNNUyIgLCJhdWQiIDogImh0dHBzOi8vY2FwaS5kYnMuY29tL2FjY2VzcyIgLCJqdGkiIDogIjgzNzU4NDIxMjgzNTE5MzQ4OTgiICwiY2luIiA6ICJRMGxPTURBd01EQXgifQ.hJ4JP_GBV63Hq6SbhF-ozSCeN8l0E0fs61BfDFGxoqc',
	}

	#data = '{"homeLoanApplicants":[{"homeLoanApplicant":{"dateOfBirth":"1988-08-10","financialCommitment":{"carLoan":{"amount":500,"currency":"SGD"},"homeLoan":{"amount":1000,"currency":"SGD"},"otherLoans":{"amount":300,"currency":"SGD"}},"fixedMonthlyIncome":{"amount":4566,"currency":"SGD"},"isMainApplicant":true,"otherMonthlyIncome":{"amount":1000,"currency":"SGD"}}}]}'
	data = json.dumps({"homeLoanAllpicants":[{"homeLoanApplicant":{"dateOfBirth":"1999-08-10","fixedMonthlyIncome":{"amount":income,"currency":"SGD"}}}]})

	response = requests.post('https://www.dbs.com/sandbox/api/sg/v1/mortgages/calculateHDBAffordability', headers=headers, data=data)
	decoded = json.loads(response.text)
	return decoded["maximumLoanAmount"]["amount"]
	