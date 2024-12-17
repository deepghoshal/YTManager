import sqlite3

con=sqlite3.connect('youtube_videos.db')
cursor=con.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos (
                   id INTERGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   time TEXT NOT NULL
        )
    ''')


def list_videos():
       cursor.execute("SELECT * FROM videos")
       for row in cursor.fetchall():
           print(row)
    
    
def add_video(name,time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?,?)",(name,time))
    con.commit()
    
def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?,time =? WHERE id=?",(new_name,new_time,video_id))
    con.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id=? ",(video_id,))
    con.commit()


def main():
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
                list_videos()

            case'2':
                name=input("Enter video name ")
                time=input("Enter video time ")               
                add_video(name,time)
            
            case'3':
                video_id=input("Enter video id to update")
                name=input("Enter video name ")
                time=input("Enter video time ")
                update_video(video_id,name,time)
                
            case'4':
                video_id=input("Enter video id to delete")
                delete_video(video_id)
                               
            case'5':
                break
    con.close()
if __name__=="__main__":
    main()