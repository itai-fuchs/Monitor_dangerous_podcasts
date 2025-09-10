# Monitor-_dangerous_podcasts

5 services in the program.

1. First service:
Publishes to Kafka the paths of audio files along with their metadata.


2. Second service:
Receives the information from Kafka.
Adds an id to each file
Sends the metadata to the Elastic index.
And the file itself is sent to Mongo using the gridfs library, which allows you to save large files in Mongo.


3. Third service:
Exports the audio files from Mongo. Performs an stt process on them and adds the resulting output to the same document (based on the id) as a field in Elastic.

We chose to access Mongo directly and not need to know the path of the original file. So that there are no complex dependencies between the different services.


4. Fourth service:
Access to Elastic and performed logic on the stt to calculate the risk of the text and add the relevant fields.

We chose to verify the risk percentage by calculating the number of dangerous words. And normalized the percentages.

In addition, we chose to divide the risk level into 3: high, medium and none. According to the risk percentage out of 100. Above 40 percent is high risk and below it is medium risk.

In addition, the decision as to whether this is a criminal incident was determined by the risk percentage. Risk above 50 percent was determined as criminal.


5. fifth service uses fastapi to query data from elastic.

We initially chose 2 queries. One to find all documents that are incriminated. And all documents that have a high risk rating.