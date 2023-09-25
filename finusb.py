from selenium import webdriver
import time

# Inisialisasi driver Chrome
driver = webdriver.Chrome()

# Buka situs web Instagram
driver.get("https://www.instagram.com")

# Tunggu selama 10 detik (atau sesuaikan sesuai kebutuhan)
time.sleep(10)

# Tutup browser
driver.quit()
