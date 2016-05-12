from identify import isImei, isSerial

def wideReader(sh):
    #this function reads any template, looking for IMEIs and serials
    #in a single row
    
    maxrow = sh.nrows
    maxcol = sh.ncols
    imeiList = []

    for r in range(maxrow):
        tempDict = {} #creates the dictionary and an Imei counter
        nImei = 1
        for c in range(maxcol):
            try:    
                cell = int(sh.cell_value(r, c))
                cell = str(cell)
            except:
                cell = unicode(sh.cell_value(r,c))

            if isImei(cell):
                tempDict.update({'imei'+str(nImei) : cell})
            elif isSerial(cell):
                tempDict.update({'serial':cell})

        if tempDict.has_key('serial') and tempDict.has_key('imei1'):  #if it has a serial and imei the dict is complete and added to list
            imeiList.append(tempDict)
        elif tempDict.has_key('imei1'): #if it has imei but not serial, it uses imei as serial
            tempDict.update({'serial':tempDict['imei1']})
            imeiList.append(tempDict)
        else:
            continue #if it doesnt have serial and imei, just continues.
    
    return imeiList

    '''
    IMEICOL = 4
    SERIALCOL = 17
    maxrow = sh.nrows
    imeiList = []
    for r in range(1, maxrow):
        #  Imei, Serial pairs:
        values = {
            'imei' : sh.cell(r,IMEICOL).value,
            'serial' : sh.cell(r,SERIALCOL).value
        }
        imeiList.append(values)
    return imeiList
    '''
