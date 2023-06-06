import cv2

def is_blacked_out(frame, intensity_threshold):
    average_intensity = cv2.mean(frame)[0]
    return average_intensity < intensity_threshold

def main():
    # Video file or webcam index
    video_source = 'http://192.168.4.1/mjpeg/1'  # Replace with your video file path or webcam index (e.g., 0)

    # Intensity threshold for blacked-out frames
    intensity_threshold = 10  # Adjust this value according to your needs

    # Open the video stream
    video_capture = cv2.VideoCapture(video_source)

    while video_capture.isOpened():
        ret, frame = video_capture.read()

        # Break the loop if the video stream ends
        if not ret:
            break

        # Check if the frame is blacked-out
        if is_blacked_out(frame, intensity_threshold):
            print("Blacked-out frame detected!")

    # Release the video stream and close windows
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()