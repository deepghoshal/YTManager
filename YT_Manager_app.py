import json

def load_data():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return

def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)
        
    
def list_all_video(videos):
        print("\n")
        print("*"*70)
        for index,video in enumerate(videos,start=1):
            print(f"{index}. {video['name']},Duration:{video['time']}")
    
    
    
def add_video(videos):
    name=input("Enter video name: ")
    time=input("Enter video time: ")
    videos.append({'name':name,'time':time})
    save_data_helper(videos)
    
    
    
def update_video(videos):
    list_all_video(videos)
    index=int(input("Enter the video no to update "))
    if 1<= index <=len(videos):
        name=input("Enter the new video name: ")
        time=input("Enter the new video time: ")
        videos[index-1]={'name':name,'time':time}
        save_data_helper(videos)
        print("The Video is updated")
    else:
        print("invalid index selected")


def delete_video(videos):
    list_all_video(videos)
    index=int(input("Enter the video no to update "))
    if 1<= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
        print("The video is deleted")
    else:
        print("Invalid Video index selected")

def main():
    videos=load_data()
    while True:
        print("\n YouTube Manager | Choose Options")
        print("1. List all YT videos")
        print("2. Add a YT videos")
        print("3. Update a YT videos")
        print("4. Delete a YT videos")
        print("5. Exit App")
        choice=input("Enter choice : ")
        
        match choice:
            case'1':
                list_all_video(videos)

            case'2':
                add_video(videos)
            
            case'3':
                update_video(videos)
                
            case'4':
                delete_video(videos)
            case'5':
                break
if __name__ ==  "__main__":    #dunder if fn name main in any where in found just run the main fn
    main() 
    
