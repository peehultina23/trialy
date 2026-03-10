from pyfingerprint.pyfingerprint import PyFingerprint
import time



f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
if not f.verifyPassword(): exit("Wrong password!")



def enroll():
    while not f.readImage(): pass
    f.convertImage(0x01)
    if f.searchTemplate()[0] >= 0: print("Already enrolled!"); return
    time.sleep(2)
    while not f.readImage(): pass
    f.convertImage(0x02)
    if f.compareCharacteristics():
        print("Enrolled at #", f.storeTemplate())
    else: print("No match!")



def search():
    while not f.readImage(): pass
    f.convertImage(0x01)
    pos = f.searchTemplate()[0]
    print("Access granted #" if pos>=0 else "Access denied!", pos)



while True:
    c = input("E/S/Q: ").lower()
    if c == 'q': break
    if c == 'e': enroll()
    if c == 's': search()
