import cv2
import time
import os
import hand as htm  # import modul hand -file hand.py


cap = cv2.VideoCapture(1)  # sử dụng webcam từ phone/ 0,1,2..


FolderPath = "finger/Fingers"
# lst = os.listdir(FolderPath)
lst = sorted(os.listdir(FolderPath), key=lambda x: int(os.path.splitext(x)[0]))

# print(lst)
lst_2 = []  # khai báo list chứa các mảng giá trị của các hình ảnh/
for i in lst:
    # print(i)
    # Fingers/1.jpg , Fingers/2.jpg ...
    image = cv2.imread(f"{FolderPath}/{i}")
    # print(f"{FolderPath}/{i}")
    lst_2.append(image)
# print(len(lst_2)) --> 6
pTime = 0  # khai báo điểm bắt đầu

detector = htm.handDetector(detectionCon=0.75)  # 0.55 độ chính xác 55%
# 0.75 độ chính xác 75%

fingerid = [4, 8, 12, 16, 20]  # trichlo-ngontay
while True:
    ret, frame = cap.read()
    frame = detector.findHands(frame)
    lmList = detector.findPosition(frame, draw=False)  # phát hiện vị trí

    if len(lmList) != 0:
        fingers = []
        # viết cho ngón cái (ý tường là điểm 4 ở bên trái hay bên phải điểm 2 )
        if lmList[fingerid[0]][1] < lmList[fingerid[0] - 1][1]:
            fingers.append(1)
            # print(lmList[fingerid[0]][1])
            # print(lmList[fingerid[0] - 1][1])
        else:
            fingers.append(0)
        print(lmList)
        # viết cho 4 ngón dài
        for id in range(1, 5):
            if lmList[fingerid[id]][2] < lmList[fingerid[id]-2][2]:
                fingers.append(1)
                print(lmList[fingerid[id]][2])
                print(lmList[fingerid[id]-2][2])
            else:
                fingers.append(0)

        print(fingers)
        songontay = fingers.count(1)
        print(songontay)

    # chú ý mỗi bức ảnh sẽ đẩy về giá trị của 1 mảng có chiều rông, cao khác nhau
    # ví dụ ảnh 0.png : print(lst_2[0].shape) kết quả (126, 110, 3)
    # frame[0:126,0:110] = lst_2[0]
    # do các bức ảnh 0-5.png khác nhau các giá trị wisth, height nên phải get theo shape
        if songontay == 0:
            imge_index = 6
        else:
            image_index = songontay - 1
        h, w, c = lst_2[songontay-1].shape
        # nếu số ngón tay =0 thì lst_2[-1] đẩy về phần tử cuối cùng của list là ảnh 6
        frame[0:h, 0:w] = lst_2[songontay-1]

        # vẽ thêm hình chữ nhật hiện số ngón tay
        cv2.rectangle(frame, (0, 200), (150, 400), (0, 255, 0), -1)
        cv2.putText(frame, str(songontay), (30, 390),
                    cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 5)

    # trả về số giây, tính từ 0:0:00 ngày 1/1/1970 theo giờ  utc , gọi là(thời điểm bắt đầu thời gian)
    cTime = time.time()
    # tính fps Frames per second - đây là chỉ số khung hình trên mỗi giây
    fps = 1/(cTime-pTime)
    pTime = cTime
    # print(type(fps))
    # show fps lên màn hình,
    # fps hiện đang là kiểu float , ktra print(type(fps))
    cv2.putText(frame, f"FPS: {int(fps)}", (150, 70),
                cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.imshow("Mr.TA Lap Trinh", frame)
    if cv2.waitKey(1) == ord("q"):  # độ trễ 1/1000s , nếu bấm q sẽ thoát
        break
cap.release()  # giải phóng camera
cv2.destroyAllWindows()  # thoát tất cả các cửa sổ
