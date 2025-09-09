# Monitor-_dangerous_podcasts

Three services in the system. The first one extracts audio files from their path, edits their metadata and sends them to Kafka. 
The second service receives the information from Kafka, adds an id to each record and sends the file to Mongo using gridfs and the metadata to Elastic. 
The third service extracts the file from Mongo. Transcribes it and adds the text to the metadata in Elastic


The choice of three services is because only the first service needs the local path on the computer. Also, the second service sends quickly to Elastic and Mongo without having to wait for the transcription to be added, which takes a long time. And the third service goes straight to Mongo and receives the files themselves that we uploaded using the gridfs library.