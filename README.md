# Monitor-_dangerous_podcasts

4 services in the program.

First service:
Publishes to Kafka the paths of audio files along with their metadata.


Second service:
Receives the information from Kafka.
Adds an id to each file
Sends the metadata to the Elastic index.
And the file itself is sent to Mongo using the gridfs library, which allows you to save large files in Mongo.


Third service:
Exports the audio files from Mongo. Performs an stt process on them and adds the resulting output to the same document (based on the id) as a field in Elastic.

We chose to access Mongo directly and not need to know the path of the original file. So that there are no complex dependencies between the different services.


Fourth service: 
Accessed Elastic and performed logic on the stt to calculate the risk of the text and added the relevant fields.

We chose to verify the risk percentage by calculating the number of dangerous words. And we normalized the percentages.

In addition, we chose to divide the risk level into 3 high, medium and low. According to the risk percentage out of 100.

In addition, the decision whether this is a criminal event was determined according to the risk percentage. Above 70 percent risk was determined as criminal.