import os 

librarii = ["tk", "mysql-connector-python", "Pillow", "qrcode", "opencv-python", "pyzbar","requests"]

for i in range(len(librarii)):
    os.system("pip install " + librarii[i])
