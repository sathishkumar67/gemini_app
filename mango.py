import pymongo

# Replace the following variables with your MongoDB Atlas connection string
username = "sathish"
password = "Pytorch12."
cluster_name = 'Cluster0'
database_name = 'your_database_name'

# Construct the connection string
connection_string = "mongodb+srv://sathish:Pytorch12.@cluster0.ynfsh.mongodb.net/"

# Create a MongoDB client
client = pymongo.MongoClient(connection_string)

# # Access a specific database (replace 'your_database_name' with your actual database name)
db = client[database_name]
#
# # Access a specific collection within the database (replace 'your_collection_name' with your actual collection name)
collection = db["s"]

# # Now, you can perform operations on the collection, such as inserting documents or querying data
# # Insert a single document
document = {"name": "John Doe", "age": 30, "city": "Example City"}
collection.insert_one(document)

