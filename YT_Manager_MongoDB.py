from pymongo import MongoClient
import json

client=MongoClient("mongodb+srv://deepghoshal2002:FYOQQVMgFflewgi3@practicedb.ay2ds.mongodb.net/")



db=client["ytmanager"]

video_collection=db["videos"]

print(video_collection)


def list_video():
   for video in video_collection.find():
       print(f"ID:{video['_id']},Name:{video['name']},Time: {video['time']}")

def add_video(name,time):
    video_collection.insert_one({"name":name,"time":time})

def update_video(video_id,new_name,new_time):
    video_collection.update_one({'_id': ObjectId(video_id)}, {"$set": {"name": new_name, "time": new_time}})

def delete_video(video_id,name,time):
    video_collection.delete_one({'_id':video_id},{'name':name},{'time':time})


def main():
    while True:
        print("\n YouTube Manager | Choose Options")
        print("1. List all YT videos")
        print("2. Add a new YT videos")
        print("3. Update a YT videos")
        print("4. Delete a YT videos")
        print("5. Exit the App")
        choice=input("Enter choice : ")
        
        if choice =='1':
            list_video()
        elif choice == '2':
            name=input("Enter video name ")
            time=input("Enter video time ")
            add_video(name,time)
        elif choice == '3':
            video_id=("Enter video id")
            name=input("Enter video name ")
            time=input("Enter video time ")
            update_video(video_id,name,time)
        elif choice =='4':
            video_id=("Enter video id")
            delete_video(video_id,name,time)
        elif choice =='5':
            break
        else:
            print("invalid choice")


if __name__=="__main__":
    main()



