import time
import MAG3110
mag = MAG3110.MAG3110(1)
mag.SetCtrlReg1(0x39)

if __name__ == "__main__":
    try:
        while True:
            print("X: {0}, Y: {1}, Z: {2}, Temp: {3}".format(mag.GetXAxis(), mag.GetYAxis(), mag.GetZAxis(), mag.GetDieTemp()))
            time.sleep(0.5)
    except KeyboardInterrupt:
        exit()
