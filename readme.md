
Objective
---------
 * Daily crypto marketing notification creation app
 We would like you to create a crypto notification app. The features it should include:
Create a server which will be able to take in the following rest APIs
Create a notification. Line items may include current price of BTC, market trade volume, intra day high price, market cap 
Send a notification to an email
List sent notifications (sent, outstanding, failed etc.)
Delete a notification


How to submit
Please upload the code for this project to GitHub, and post a link to your repository below.

## Objective

Develop a crypto notification app with the following features:

1. Server with REST APIs: 
   - Implement a server to handle RESTful API requests.

2. Notification Management:
   - Create a Notification: 
     - Create a notification with the following line items: current price of BTC, market trade volume, intra day high price, market cap.
   - Send Notification:
     - Dispatch the notification to specified email addresses.

3. Notification Tracking:
   - List Notifications:
     - View sent notifications.
     - Track outstanding notifications.
     - Identify failed notification attempts.

4. Notification Deletion:
   - Remove notifications as required (Make sure not to send notification if it is deleted from the system, use lock).


## Components
1. API Server
   - Framework: Flask
   - ORM - sqlmodel
   - Database: PostgreSQL
   - Endpoints:
     - `POST /notification`: Create a new notification
     - `POST /notification/<id>/send`: Send a notification to email
     - `GET /notifications`: List all notifications
     - `DELETE /notification/<id>`: Delete a notification
2. Data Model
   - Notification
     - this is model where we will store the notification and check the status of the notification
   - Email Notification Log
     - this is model where we will store the email notification log and check the status of the notification
3. Service
   - this is service layer where we will implement the business logic
   - NotificationService
     - this will create, list, delete, get, send the notification
   - EmailService
     - this will send the email notification
   - PhoneService
     - this will send the phone notification

4. Client
    - emailclient - singleton class to handle the email dispatch


User -> API Server -> NotificationService -> EmailService -> Client

## thinks to do 
- since this is high volume app we might need to impelement worker and scale the server
- 
