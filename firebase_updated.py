# Importing required packages
import firebase_admin
from firebase_admin import credentials, db
import glob
from PIL import Image
import time

# Initializing the database with URL
cred = credentials.Certificate('./edge-genics-experiment-firebase-adminsdk-5j81b-1d738a8d9e.json')
firebase_admin.initialize_app(cred,{
    'databaseURL': 'https://edge-genics-experiment-default-rtdb.asia-southeast1.firebasedatabase.app/'
}) 

def listener(event):
    global count
    global label_array  # References the path of the event
    print("Data----",event.data)  # Gives the UPDATED DATA, None if deleted

    # Now, executing specific functions based on the new data(UPDATED DATA)

    if str(event.data) == label_array[count]:
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
label_array =["person","cat","remote","donut","dog","traffic light","bicycle","dog","bicycle","sandwich","umbrella","bus","bowl","banana","person","zebra","potted plant","elephant","clock","apple","tv","bird","giraffe","pizza","train"]
db.reference('/').listen(listener) # It calls the above listener method(It continuosly listens for the data changes in your database)
# Everytime the data changes, listener function will be called
