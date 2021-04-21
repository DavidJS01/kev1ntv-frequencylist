# Autonomous German Vocabulary Word Frequency List - Learn What German Words to Learn with Twitch Streams

![kev1n](https://user-images.githubusercontent.com/53328559/115154362-49fa9c80-a02f-11eb-95ff-c431fbf761ec.png)

## Background:

Recently I set on a fun challenge of learning enough German so I could read Kafka in its original text; but what fun is language learning without consuming media?

I enjoy watching a German livesteamer on Twitch -- even if I can't understand anything he is saying. This project is an autonomously updating database that collects all Twitch chat messages from https://www.twitch.tv/kev1ntv, and then the database is parsed and a word frequency list is created.

By analyzing thousands of messages, I can learn what German vocabulary words I should learn so I can understand Kev1ntv's Twitch chat: updated automatically with the use of an AWS Lambda function.

## Visualizations:
**TOP 30 MOST USED WORDS:**

![image](https://user-images.githubusercontent.com/53328559/115487817-4f620d80-a20e-11eb-853f-1ebf4a532eb8.png)

**TOP 30 ACTIVE TWITCH VIEWERS:**
![image](https://user-images.githubusercontent.com/53328559/115487836-59840c00-a20e-11eb-9674-42ba2c38d116.png)

As of 7:27PM 4/20/2021, these graphs were created from 7014 rows of data collected over the previous four days.

## Project Overview:

This project utilizes the Twitch API to create a function and check if the Twitch channel https://www.twitch.tv/kev1ntv is online. If it isn't online, then the script abandons the proccess and exits.

![image](https://user-images.githubusercontent.com/53328559/115155323-4584b280-a034-11eb-8ec1-a3bb41d9713c.png)

If the channel is online, then the script connects to the Twitch IRC channel utilizing Socket, creating a function to read each message and user in live time.

![image](https://user-images.githubusercontent.com/53328559/115155480-f723e380-a034-11eb-8c43-820f971235a2.png)

All messages are sent to a PostgreSQL RDS hosted on AWS:

![image](https://user-images.githubusercontent.com/53328559/115155537-4ff37c00-a035-11eb-8b7d-decd60c75528.png)

The Python script is then hosted on an AWS Lambda function, scheduled to execute the script every 5 minutes; so, data is collected from Kev1ntv's livestream autonomously if he is online.

Each time the Lambda function is executed, it stores data into the PostgreSQL DB and into a DynamoDB for backup.

![image](https://user-images.githubusercontent.com/53328559/115155960-01df7800-a037-11eb-9c89-1e7b9290240d.png)

## Future of This Project:

I still want to add a lot to this project! Eventually, I plan on containerizing the scripts, and placing those containers into an AWS EC2 instance. I will then use Apache Airflow to schedule those scripts to run instead of using a Lambda function. Here are some pictures of my "office" setup while I worked through this project:


![20210415_220631](https://user-images.githubusercontent.com/53328559/115156116-a661ba00-a037-11eb-90c7-608ffdf8d755.jpg)

![20210412_005905](https://user-images.githubusercontent.com/53328559/115156145-c3968880-a037-11eb-9785-e411125f4b1e.jpg)

So, I clearly was a bit confused as I worked through this project! There is still a lot of things I want to do with it, as listed below. My plan is to add these changes by the end of the summer semester: 

![image](https://user-images.githubusercontent.com/53328559/115156233-15d7a980-a038-11eb-9219-bc3034d850d8.png)

I had such a fun time making the first version of this project, and even though I spent hours frustratedly googling things, the satisfaction of making something made everything so worth it. I loved learning about basic networking with sockets, IRC, interacting with APIs, AWS, and PostgreSQL. 

This project will update frequently! I'm excited to improve it!
