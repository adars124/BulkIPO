import requests as req
import json
from typing import TypedDict

def fjson(resp):
    return json.loads(resp)

def login(user):

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }

    client_data  = {
        'clientId': user.clientId,
        'username': user.username,
        'password': user.password,
    }

    try:
        res = req.post('https://webbackend.cdsc.com.np/api/meroShare/auth/', json=client_data, headers=headers)

        if res.status_code == 200:
            print("Logged in successfully!")
            token = dict(res.headers)['Authorization']
            return str(token)
        else:
            err = fjson(res.text)
            return ('\nError: ' + err['documentation'])
    except Exception as e:
        print('Error: ', e)

def own_details(token):
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': token
    }

    res = req.get('https://webbackend.cdsc.com.np/api/meroShare/ownDetail/', headers=headers)

    if res.status_code == 200:
        return fjson(res.text)
    else:
        err = fjson(res.text)
        return ('\nError: ' + err['documentation'])

def get_client_boid(token, boid):
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'{token}'
    }

    res = req.get(f'https://webbackend.cdsc.com.np/api/meroShareView/myDetail/{boid}', headers=headers)

    if res.status_code == 200:
        return res.json()
    else:
        err = fjson(res.text)
        return ('\nError: ' + err['documentation'])

def get_applicable_share(token):
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'{token}'
    }

    json_data = {
        'filterFieldParams': [
            {
                'key': 'companyIssue.companyISIN.script',
                'alias': 'Scrip',
            },
            {
                'key': 'companyIssue.companyISIN.company.name',
                'alias': 'Company Name',
            },
            {
                'key': 'companyIssue.assignedToClient.name',
                'value': '',
                'alias': 'Issue Manager',
            },
        ],
        'page': 1,
        'size': 10,
        'searchRoleViewConstants': 'VIEW_APPLICABLE_SHARE',
        'filterDateParams': [
            {
                'key': 'minIssueOpenDate',
                'condition': '',
                'alias': '',
                'value': '',
            },
            {
                'key': 'maxIssueCloseDate',
                'condition': '',
                'alias': '',
                'value': '',
            },
        ],
    }

    res = req.post('https://webbackend.cdsc.com.np/api/meroShare/companyShare/applicableIssue/', json=json_data, headers=headers)

    if res.status_code == 200:
        return res.json()
    else:
        err = fjson(res.text)
        return ('\nError: ' + err['documentation'])
    
def bank_details(token, bankCode):
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'{token}'
    }

    res = req.get(f'https://webbackend.cdsc.com.np/api/bankRequest/{bankCode}', headers=headers)

    if res.status_code == 200:
        return res.json()
    else:
        err = fjson(res.text)
        return ('\nError: ' + err['documentation'])

def customer_code(token, code):
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'{token}'
    }

    res = req.get(f'https://webbackend.cdsc.com.np/api/meroShare/bank/{code}', headers=headers)

    if res.status_code == 200:
        return res.json()
    else:
        err = fjson(res.text)
        return ('\nError: ' + err['documentation'])

def apply_ipo(data):
    url = 'https://webbackend.cdsc.com.np/api/meroShare/applicantForm/share/apply'

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f"{data['token']}"
    }

    res = req.post(url, json=data, headers=headers)

    return res.json()
    
def apply_share(users, kitta, companyShareId):
    for user in users:
        token = login(user)

        ownDetails = own_details(token)
        getClientBoid = get_client_boid(token, ownDetails['demat'])

        bankDetails = bank_details(token, getClientBoid['bankCode'])

        customerCode = customer_code(token, bankDetails['bank']['id'])['id']

        data = {
            "accountBranchId": bankDetails['branch']['id'],
            "accountNumber": bankDetails['accountNumber'],
            "appliedKitta": str(kitta),
            "bankId": bankDetails['bank']['id'],
            "boid": ownDetails['boid'],
            "companyShareId": companyShareId,
            "crnNumber": user.crn,
            "customerId": customerCode,
            "demat": getClientBoid['boid'],
            "transactionPIN": user.pin,
            "token": token
        }

        applyIPO = apply_ipo(data=data)

    return applyIPO

