# Importing required packages
import firebase_admin
from firebase_admin import credentials, db
import glob
from PIL import Image
import time

# Initializing the database with URL
cred = credentials.Certificate('./edge-genics-experiment-firebase-adminsdk-gx3hb-f3784b1a52.json')
firebase_admin.initialize_app(cred,{
    'databaseURL': 'https://edge-genics-experiment-default-rtdb.asia-southeast1.firebasedatabase.app/'
}) 

def listener(event):
    global count
    global label_array
    print(event.event_type)  # Indicates the type of the event done
    print(event.path)  # References the path of the event
    print(event.data)  # Gives the UPDATED DATA, None if deleted

    # Now, executing specific functions based on the new data(UPDATED DATA)

    if isinstance(event.data, dict):
        for key, value in event.data.items():
            print(key, value)
            print(count)
            print(label_array[count])
            if str(value) == label_array[count]:
                count += 1
                # /// Execute your code here ///
                print('Data updated as ', str(event.data))
                if (count < 10):
                    count_str = "0"+str(count)
                else:
                    count_str = str(count)
                image = Image.open('pics/pic'+count_str+'.jpg')

                # Display the image
                image.show()
                # time.sleep(3)
                # image.close()

    elif str(event.data) == None:
        # /// Execute your code here ///
        print('Your data has been deleted!')

count = 0
label_array =["Hello1","Hello2","Hello3"]
db.reference('/').listen(listener) # It calls the above listener method(It continuosly listens for the data changes in your database)
# Everytime the data changes, listener function will be called
