import usb.core
import usb.util
import time
from selenium import webdriver

# Fungsi untuk mencari perangkat USB berdasarkan Vendor ID dan Product ID
def find_usb_device(vendor_id, product_id):
    device = usb.core.find(idVendor=vendor_id, idProduct=product_id)
    return device

# Jika ada maka buka goggle jika tidak print tidak ditemukan
def automate_browser_based_on_usb(device):
    if device is not None:
        driver = webdriver.Edge()

        driver.get("https://www.instagram.com")
        
        # Tunggu selama 1000 detik (atau sesuaikan sesuai kebutuhan)
        time.sleep(1000)
        # Tutup browser
        driver.quit()
    else:
        print("Perangkat USB tidak ditemukan.")

# Vendor ID dan Product ID perangkat USB yang ingin Anda cari
vendor_id = 0x1058  # Vid cek di apk libsub
product_id = 0x2626  # Pid cek di apk libsub

# Nyari Perangkat Usb
usb_device = find_usb_device(vendor_id, product_id)

# Masuk ke function automate_browser_based_on_usb
automate_browser_based_on_usb(usb_device)