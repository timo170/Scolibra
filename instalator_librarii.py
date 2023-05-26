import os 

librarii = ["tk", "mysql-connector-python", "Pillow", "qrcode", "opencv-python", "pyzbar"]

for i in range(len(librarii)):
    os.system("pip install " + librarii[i])
