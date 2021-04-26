# Autonomous German Vocabulary Word Frequency List - Learn What German Words to Learn with Twitch Streams

![kev1n](https://user-images.githubusercontent.com/53328559/115154362-49fa9c80-a02f-11eb-95ff-c431fbf761ec.png)

## Background:

Recently I set on a fun challenge of learning enough German so I could read Kafka in its original text; but what fun is language learning without consuming media?

I enjoy watching a German livesteamer on Twitch -- even if I can't understand anything he is saying. This project is an autonomously updating database that collects all Twitch chat messages from https://www.twitch.tv/kev1ntv, and then the database is parsed and a word frequency list is created.

By analyzing thousands of messages, I can learn what German vocabulary words I should learn so I can understand Kev1ntv's Twitch chat: updated automatically with the use of an AWS Lambda function.

## Visualizations:
**TOP 30 MOST USED WORDS:**

![image](https://user-images.githubusercontent.com/53328559/116025337-173f3e00-a605-11eb-8311-69dccbddac88.png)

**TOP 30 ACTIVE TWITCH VIEWERS:**
![image](https://user-images.githubusercontent.com/53328559/116025355-20c8a600-a605-11eb-8260-1f03db4a35af.png)

As of 8:32 PM, 4/25/2021, these graphs were created from 17,055 messages collected over the span of 10 days.

## Project Overview:

This project utilizes the Twitch API to create a function and check if the Twitch channel https://www.twitch.tv/kev1ntv is online. If it isn't online, then the script abandons the proccess and exits.

![image](https://user-images.githubusercontent.com/53328559/116025607-c845d880-a605-11eb-8bdc-960413fbe00f.png)


If the channel is online, then the script connects to the Twitch IRC channel utilizing socket, creating a function to read each message and user in live time.

![image](https://user-images.githubusercontent.com/53328559/116025641-dbf13f00-a605-11eb-87e7-96170aa5bdf1.png)


All messages are sent to a PostgreSQL RDS hosted on AWS:

![image](https://user-images.githubusercontent.com/53328559/115155537-4ff37c00-a035-11eb-8b7d-decd60c75528.png)

The Python script is then hosted on an AWS Lambda function, scheduled to execute the script every 5 minutes; so, data is collected from Kev1ntv's livestream autonomously if he is online.

![image](https://user-images.githubusercontent.com/53328559/116025743-0e02a100-a606-11eb-87ce-7714c0e7cc7d.png)

## Future of This Project:

If you look at the diagrams I created while I was learning how to complete this project, you can notice that I wanted to initially create something of a larger scale. But, as I worked through this project, I realized that it would be overkill to schedule my scripts with Airflow or use Kubernetes. Learning these tools would be useful, but it would be more beneficial to learn how to use these tools in a proper context.

While I definitely want to continue progressing and learning as I work torwards becoming a data engineer, I want to spend much of my upcoming time learning about data structures and algorithms, proper development practices, etc. I recently registed for the Databricks Data + AI Summit, and I registered for the Lakehouse with Delta Lake Deep Dive class. So, I want to also spend most of my time preparing and learning the fundamental concepts behind data engineering, so I can benefit as much as possible for the event. I am looking forward to getting a copy of "Designing Data Intensive Applications".


![20210415_220631](https://user-images.githubusercontent.com/53328559/115156116-a661ba00-a037-11eb-90c7-608ffdf8d755.jpg)

![20210412_005905](https://user-images.githubusercontent.com/53328559/115156145-c3968880-a037-11eb-9785-e411125f4b1e.jpg)

I had such a fun time making the first version of this project, and even though I spent hours frustratedly googling things, the satisfaction of making something made everything so worth it. I loved learning about basic networking with sockets, IRC, interacting with APIs, AWS, and PostgreSQL. I am excited to grow and improve in the future!

