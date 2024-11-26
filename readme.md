

Daily crypto marketing notification creation app
We would like you to create a crypto notification app. The features it should include:

 

Create a server which will be able to take in the following rest APIs



Create a notification. Line items may include current price of BTC, market trade volume, intra day high price, market cap 
Send a notification to an email
List sent notifications (sent, outstanding, failed etc.)
Delete a notification


How to submit
Please upload the code for this project to GitHub, and post a link to your repository below.



Notificaiton server


Endpoint 
------------

- Creation Notic - [post] /v1/notic
- Delete Notic - [delete] /v1/notic/{notic_id}
- Get all Notic - [get] /v1/notic
- Send a notification [post] /v1/notic/{notic_id}/send# Bitgo
