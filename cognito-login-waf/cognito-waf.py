import requests

url = "https://cognito-idp.us-east-1.amazonaws.com/"

payload = "{\r\n    \"AuthParameters\": {\r\n        \"USERNAME\": \"<your_email>\",\r\n        \"PASSWORD\": \"<your_pw>\"\r\n    },\r\n    \"AuthFlow\": \"USER_PASSWORD_AUTH\",\r\n    \"ClientId\": \"<your_client_id>\"\r\n}"
headers = {
  'X-Amz-Target': 'AWSCognitoIdentityProviderService.InitiateAuth',
  'Content-Type': 'application/x-amz-json-1.1'
}

for x in range(150):
    response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
print (f"Login tried {x} times")