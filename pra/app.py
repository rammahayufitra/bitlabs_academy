import cv2

# Untuk mengakses video dari kamera, gunakan nomor kamera (biasanya 0 untuk kamera bawaan).
# Untuk mengakses video dari file, gantilah '0' dengan nama file video.
video_source = 0  # Menggunakan kamera bawaan
# video_source = 'video_file.mp4'  # Menggunakan file video

# Buka koneksi video
cap = cv2.VideoCapture(video_source)

# Periksa apakah koneksi video terbuka dengan benar
if not cap.isOpened():
    print("Tidak dapat membuka video source")
    exit()

while True:
    # Baca frame dari video
    ret, frame = cap.read()

    if not ret:
        print("Tidak dapat membaca frame")
        break

    # Tampilkan frame
    cv2.imshow('Video', frame)

    # Hentikan loop dengan menekan tombol 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Tutup koneksi video dan jendela tampilan
cap.release()
cv2.destroyAllWindows()
