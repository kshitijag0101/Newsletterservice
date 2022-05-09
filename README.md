# Newsletterservice
This newsletter service provides admin the access to add topics for the news and add the news and specify the time at which it will be delivered. 
The user can subscribe to any specific topic of his choice.
when the system runs the mails are delivered to the user as per the time specified by the admin for the news.
There are two files in the project main.py and sendmail.py
main.py is used for admin login and user login where admin can add the topic and the news related to the topic and user can subscribe to a   specific topic.
sendmail.py is used to send the mail to the users at the time specified by the admin.
In the project I have used MySQL as database and libraries like mysql-connector , STMP ,SSL ,time to schedule and send the message.
To run this project on your system you should have MySql,Python installed on your system. You just have to set the password of MySql in main.py and create a database named newsletter in MySql also enter admin details in admin table and you are ready to go then in sendmail.py you just have to change the email and password of the sender to start your service.
<br/>Limitation of system is that :-
1) It does not allow user to subscribe two or more topics
2) It sends the mail when sendmail.py is run.
