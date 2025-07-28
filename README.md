# Finger Counter using OpenCV and MediaPipe 🖐️

Ứng dụng đơn giản sử dụng xử lý ảnh số để nhận diện bàn tay và đếm số ngón tay giơ lên theo thời gian thực bằng webcam. Dự án sử dụng thư viện OpenCV và MediaPipe.

## 🧠 Tính năng

- Nhận diện bàn tay trong khung hình thời gian thực.
- Đếm số ngón tay đang giơ lên (0-5).
- Hiển thị số ngón tay kèm hình ảnh minh họa.
- Tính toán và hiển thị FPS (Frames per Second) để đánh giá hiệu suất xử lý thời gian thực.

## 🧠 Giải Thích Kỹ Thuật

- MediaPipe Hands cung cấp 21 điểm đặc trưng (landmarks) cho mỗi bàn tay.
- Dựa vào vị trí các điểm này (tọa độ X-Y), chương trình xác định xem mỗi ngón tay đang co lại hay duỗi ra.
- Khi biết trạng thái của 5 ngón tay, chương trình sẽ hiển thị số lượng tương ứng.

## 🛠️ Công nghệ sử dụng

- Python3.x : Ngôn ngữ chính
- OpenCV : Xử lí ảnh, truy cập webcam, chuển đổi màu
- MediaPipe : Nhận diện bànn tay và trích xuất toạ độ các điểm trên bàn tay

## 📁 Cấu trúc thư mục

```bash
finger-counter/
├── finger/
│ └── Fingers/ # Chứa ảnh minh họa từ 0 đến 5 ngón tay
├── hand.py # Module nhận diện tay với MediaPipe
├── opencv-demnontay.py # Tệp chính chạy ứng dụng
├── README.md
└── .gitignore
```

## ⚙️ Cài đặt

```bash
# Tạo môi trường ảo (tuỳ chọn)
python3 -m venv venv
source venv/bin/activate  # Trên Mac/Linux

# Cài đặt thư viện cần thiết
pip install opencv-python mediapipe
```

## 🚀 Hướng Dẫn Sử Dụng

```bash
# Chạy  chương trinh
python3 opencv-demgontay.py
Nhấn q để thoát chương trình.
```

## 📸 Yêu cầu phần cứng

- Webcam hoặc camera tích hợp.
- Máy có thể chạy OpenCV và xử lý real-time

## 📄 Giấy phép

- Dự án phục vụ mục đích học tập.
- Tự do sử dụng, chỉnh sửa và chia sẻ

## Tác giả

Phạm Tuấn Anh - Dự án cá nhân phục vụ mục đích học môn Nhập Môn Xử lý Ảnh Số.
Nếu bạn thấy dự án hữu ích, hãy ⭐ star trên GitHub để ủng hộ nhé!
