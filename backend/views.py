from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
import json
import requests


class HouseLoanAPIView(APIView):

    def get(self, request, income):
        headers = {
            'Content-Type': 'application/json',
            'clientId': 'clientId2',
            'accessToken': 'eyJhbGciOiJIUzI1NiJ9.eyJpc3MiIDogImh0dHBzOi8vY2FwaS5kYnMuY29tIiwiaWF0IiA6IDE1NDIzNDUzMTExMTEsICJleHAiIDogMTU0MjM0ODkxMTExMSwic3ViIiA6ICJTVmN3TXpZPSIsInB0eXR5cGUiIDogMSwiY2xuaWQiIDogImNsaWVudElkMiIsImNsbnR5cGUiIDogIjIiLCAiYWNjZXNzIiA6ICIxRkEiLCJzY29wZSIgOiAiMkZBLVNNUyIgLCJhdWQiIDogImh0dHBzOi8vY2FwaS5kYnMuY29tL2FjY2VzcyIgLCJqdGkiIDogIjgzNzU4NDIxMjgzNTE5MzQ4OTgiICwiY2luIiA6ICJRMGxPTURBd01EQXgifQ.hJ4JP_GBV63Hq6SbhF-ozSCeN8l0E0fs61BfDFGxoqc',
        }
        data = json.dumps({
            "homeLoanAllpicants":
            [{"homeLoanApplicant": {"dateOfBirth":"1999-08-10","fixedMonthlyIncome":{"amount":income,"currency":"SGD"}}}]})
        response = requests.post('https://www.dbs.com/sandbox/api/sg/v1/mortgages/calculateHDBAffordability', headers=headers, data=data)
        return JsonResponse(json.loads(response.text))
