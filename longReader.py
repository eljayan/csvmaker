from identify import isImei, isSerial

def longReader(sh):
    
    #this function reads the templates that contain IMEIs and serials
    #in one single column. It assumes the IMEIs go first and the serials.

    imeiList = []
    maxrow = sh.nrows
    dictData = {}   #the initial dictionary
    nimei = 1       #the number of imeis found, can be 1 or 2, no more
    for r in range(maxrow):
        try:    
            cell = int(sh.cell_value(r, 0))
            cell = str(cell)
        except:
            cell = unicode(sh.cell_value(r,0))
        
        if nimei > 3:
            print "I couldn't find Serials in this file." #If it records more than 3 straight Imeis, it is rejected.
            return None
        elif isSerial(cell):
            dictData.update({'serial' : cell}) #when a serial is found it must add temporal dictionary to list
            if dictData.has_key('imei1'):
                imeiList.append(dictData) 
                dictData = {} #resets the temporal dictionary
                nimei = 1
            else:
                return None #if the temporal dictionary doesnt have an IMEI, then it is rejected.
        elif isImei(cell):
            dictData.update({'imei'+str(nimei) : cell})
            nimei+=1
    
    return imeiList
