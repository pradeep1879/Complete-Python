from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://Kumawat1879:Kumawat1879@cluster0.azmp5a7.mongodb.net/",
                      tlsAllowInvalidCertificates=True)

db = client["ytmanager"]
video_collection = db["videos"]
print(video_collection)

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def list_video():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']} and Time: {video['time']}")

def update_video(video_id, new_name, new_time):
    video_collection.update_one({'_id': ObjectId(video_id)}, {"$set": {"name": new_name, "time": new_time}})

def delete_video(video_id):
    video_collection.delete_one({'_id': ObjectId(video_id)})


def main():
    while True:
        print("\n Youtube manager app with db")
        print("1. List all youtube videos.")
        print("2. Add a youtube video.")
        print("3. Update a youtube video detail.")
        print("4. Delete a youtube video.")
        print("5. Exit the app.")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_video()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name,  time)
        elif choice == '3':
            video_id = input("Enter a video Id to update: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter the video Id to be deleted: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice")
    



if __name__ == "__main__":
    main()