import usb.core
import subprocess

# Vendor ID dan Product ID perangkat Android Anda
vid = 0x22d9  # Ganti dengan VID perangkat Anda
pid = 0x2765  # Ganti dengan PID perangkat Anda

# Cari perangkat berdasarkan VID dan PID
device = usb.core.find(idVendor=vid, idProduct=pid)

if device is None:
    print("Perangkat Android tidak ditemukan.")
else:
    print("Perangkat Android ditemukan:", device)

#COBA ADB    
# # Contoh menjalankan perintah ADB untuk menampilkan daftar perangkat yang terhubung
# adb_command = "adb devices"
# result = subprocess.run(adb_command, shell=True, capture_output=True, text=True)
# print("Hasil perintah ADB:", result.stdout)


    # Buka perangkat USB untuk komunikasi
    try:
        device.set_configuration()
        endpoint = device[0][(0, 0)][0]

        # Data yang akan dikirim ke perangkat Android (contoh: 'Hello, Android!')
        data_to_send = 'Hello, Android!'

        # Kirim data ke perangkat Android
        device.write(endpoint, data_to_send)

        print("Data berhasil dikirim ke perangkat Android:", data_to_send)
    except Exception as e:
        print("Gagal mengirim data:", str(e))
