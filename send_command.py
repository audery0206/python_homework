import serial
import time
# 串口配置
ser = serial.Serial('/dev/cu.usbmodem142201', 9600, timeout=1)

# 连续发送指令
for _ in range(10):
    for _ in range(10):
        ser.write(b'pwmwr 10 00\n')  # 发送 "pwmwr 10 00"
        ser.flush()
        time.sleep(1)

    for _ in range(10):
        ser.write(b'pwmwr 50 00\n')  # 发送 "pwmwr 50 00"
        ser.flush()
        time.sleep(1)

# 关闭串口
ser.close()
