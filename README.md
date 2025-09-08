# Monitor-_dangerous_podcasts

There are two services.

one sends messages to Kafka after extracting metadata about the audio file.

The second service receives the files from the producer, adds an id and STT sends the metadata to Elastic and the file itself use gridfs library to Mongo, so that it is possible to save a signal in binary form and extract it later.

The service adds the transcription before sending to Elastic, although this slows down the program in sending the data to Elastic and Mongo. So that we don't have to loop through all the files from Elastic again and change them once more.