import re

def isImei(s):
    #identifies IMEI format
    match = re.search(r'^\d{15}$', s)
    if match:
        return True

def isSerial(s):
    #identifies Serial Numbers
    if len(s)==16:
        return True


if __name__ == "__main__":
    test = "123456789jjjeb3ghgs"
    if isSerial(test):
        print "It is a serial"
    elif isImei(test):
        print "It is an IMEI"
    else:
        print "I dont know what it is!"
