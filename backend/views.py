from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
import json
import requests


class HouseLoanAPIView(APIView):

    def get(self, request, income):
        headers = {
            'Content-Type': 'application/json',
            'clientId': '9924b74f-36a7-458a-afe6-c3a9f9f270b7',
            'accessToken': 'eyJhbGciOiJIUzI1NiJ9.eyJpc3MiIDogImh0dHBzOi8vY2FwaS5kYnMuY29tIiwiaWF0IiA6IDE1NDIzNDkzMjExMjAsICJleHAiIDogMTU0MjM1MjkyMTEyMCwic3ViIiA6ICJTVmN3TXpZPSIsInB0eXR5cGUiIDogMSwiY2xuaWQiIDogIjk5MjRiNzRmLTM2YTctNDU4YS1hZmU2LWMzYTlmOWYyNzBiNyIsImNsbnR5cGUiIDogIjIiLCAiYWNjZXNzIiA6ICIxRkEiLCJzY29wZSIgOiAiMkZBLVNNUyIgLCJhdWQiIDogImh0dHBzOi8vY2FwaS5kYnMuY29tL2FjY2VzcyIgLCJqdGkiIDogIjMwMDI5NjYwMzE4Mjk4MTAwMTUiICwiY2luIiA6ICJRMGxPTURBd01EQXgifQ.Cyblc_7LQG6ybEpz39PB_BbyJvoEhq-7Y9k0tgbpsLY',
        }
        data = json.dumps({
            "homeLoanAllpicants":
            [{"homeLoanApplicant": {"dateOfBirth":"1999-08-10","fixedMonthlyIncome":{"amount":income,"currency":"SGD"}}}]})
        response = requests.post('https://www.dbs.com/sandbox/api/sg/v1/mortgages/calculateHDBAffordability', headers=headers, data=data)
        return JsonResponse(json.loads(response.text))
