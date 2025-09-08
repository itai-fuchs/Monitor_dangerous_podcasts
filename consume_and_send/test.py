#
#
#
# from pymongo import MongoClient
#
# # Connect to MongoDB
# client = MongoClient("mongodb://localhost:27017")
#
# # Select your database (replace 'your_database' with the actual database name)
# db = client['your_database']
#
# import gridfs
#
# # Create a GridFS object for the selected database
# fs = gridfs.GridFS(db)
#
# # Define the file path you want to upload
# file_path = "C:\podcasts\download (10).wav"
#
# # Open the file and upload it
# with open(file_path, 'rb') as file_data:
#     file_id = fs.put(file_data, filename='file.txt', description='Sample text file')
#
# print(f"File uploaded with file_id: {file_id}")
#
# # Fetch the file using its filename
# file_data = fs.find_one({'filename': 'file.txt'})
#
# if file_data:
#     # Save the file to disk
#     with open("C:\podcasts\itai.wav", 'wb') as output_file:
#         output_file.write(file_data.read())
#     print("File downloaded successfully")
# else:
#     print("File not found")