import cv2
import os
import numpy as np

try:
    import mediapipe as mp
    from mediapipe.python.solutions import pose as mp_pose
    from mediapipe.python.solutions import drawing_utils as mp_drawing
except ImportError as e:
    print(f"failed to load. Error {e}")
    exit()

def calculate_angle(a,b,c):
    a,b,c = np.array(a), np.array(b), np.array(c)
    radians = np.arctan2(c[1]-b[1],c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians * 180.0 / np.pi)
    return 360 - angle if angle > 180.0 else angle

def play_ding():
    suara_path = "/usr/share/sounds/freedesktop/stereo/message-new-instant.oga"
    if os.path.exists(suara_path):
        os.system(f'paplay {suara_path} &')

def clear_screen():
    os.system('clear')

def main():
    while True:
        clear_screen()
        print("\n=== FORM TRACKER ===")
        print("1.Push Up")
        print("2.Bicep Curl (Tangan Kiri)")
        print("3.Bicep Curl (Tangan Kanan)")
        print("4.Tutup Program")
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == '4':
            print("See You later!")
            break

        if pilihan not in ['1','2','3']:
            print("Pilihan tidak tersedia")
            continue

        cap = cv2.VideoCapture(0)
        counter = 0
        stage = "neutral"

        print("ketik 'q' untuk menghentikan program")

        with mp_pose.Pose(min_detection_confidence=0.7, min_tracking_confidence=0.7) as pose:
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret: break

                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False
                results = pose.process(image)
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                if results.pose_landmarks:
                    try:
                        landmarks = results.pose_landmarks.landmark
                        #Push Up Section
                        if pilihan == '1':
                            shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                            elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                            wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
                            angle = calculate_angle(shoulder,elbow,wrist)
                            

                            if angle > 160:
                                stage = "UP"
                            if angle < 90 and stage == "UP":
                                stage = "DOWN"
                                counter += 1
                                play_ding()
                    
                        #Left Bicep Curl Section
                        elif pilihan == '2':
                            shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                            elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                            wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
                            angle = calculate_angle(shoulder,elbow,wrist)

                            if angle > 160:
                                stage = "DOWN"
                            if angle < 40 and stage == "DOWN":
                                stage = "UP"
                                counter += 1
                                play_ding()
                    
                        #Right Bicep Curl Section
                        elif pilihan == '3':
                            shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                            elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                            wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
                            angle = calculate_angle(shoulder,elbow,wrist)

                            if angle > 160:
                                stage = "DOWN"
                            if angle < 40 and stage == "DOWN":
                                stage = "UP"
                                counter += 1
                                play_ding()
                    
                        #Calculation on arms
                        cv2.putText(image,str(int(angle)), tuple(np.multiply(elbow, [640,480]).astype(int)),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
                    except:
                        pass
                #Output frame
                cv2.rectangle(image, (0,0), (280,80), (245,117,16), -1)
                cv2.putText(image, f'REPS: {counter}', (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,255,255),2)
                cv2.putText(image, f'STAGE: {stage}', (10,100), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0),2)

                if results.pose_landmarks:
                    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
            
                cv2.imshow('Form Tracker', image)
                if cv2.waitKey(10) & 0xFF == ord('q'): 
                    break
    
        cap.release()
        cv2.destroyAllWindows()
        for i in range(10):
            cv2.waitKey(1)

if __name__ == "__main__":
    main()