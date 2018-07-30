#"use strict";
"""
 Copyright (C) 2012-2014 Grant Galitz

 Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 """
 #CEEATE BY XMILE
 #TIME:2018-07-27

 
class GameBoyAdvanceCartridge(IOCore):
    self.IOCore = IOCore

    def __init__(self):
        self.flash_is128 = False
        self.flash_isAtmel = False
        self.ROM = self.getROMArray(self.IOCore.ROM)
        self.ROM16 = getUint16View(self.ROM)
        self.ROM32 = getInt32View(self.ROM)
        self.decodeName()
        self.decodeFlashType

    def getROMArray(self,old_array):
        self.ROMLength = min((old_array.length >> 2) << 2, 0x2000000)
        self.EEPROMStart = max(self.ROMLength|0, 0x1FFFF00) if ((self.ROMLength|0) > 0x1000000) else 0x1000000
        newArray = getUint8Array(this.ROMLength | 0)
        for index in range(0,self.ROMLength):
            newArray[index | 0] = old_array[index | 0] | 0
        return newArray
    
    def decodeName(self):
        self.name = "GUID_"
        if ((self.ROMLength|0) >= 0xC0):
        for address in  range(0xAC,0xB3):
            if ((self.ROM[address|0]|0) > 0):
                self.name += chr(self.ROM[address|0]|0)
            else:
                self.name += "_"    
        
    

    def decodeFlashType(self):
        self.flash_is128 = False
        self.flash_isAtmel = False
        flash_types = 0
        F = ord("F") & 0xFF
        L = ord("L") & 0xFF
        A = ord("A") & 0xFF
        S = ord("S") & 0xFF
        H = ord("H") & 0xFF
        underScore = ord("_") & 0xFF
        five = ord("5") & 0xFF
        one = ord("1") & 0xFF
        two = ord("2") & 0xFF
        M = ord("M") & 0xFF
        V = ord("V") & 0xFF
        length = ((self.ROM.length|0) - 12)|0
        for index in range(0,length,4):
            if ((self.ROM[index | 0] | 0) == (F)):
                if ((self.ROM[index | 1] | 0) == (L | 0)):
                    if ((self.ROM[index | 2] | 0) == (A | 0)):
                        if ((self.ROM[index | 3] | 0) == (S | 0)):
                            var tempIndex = ((index | 0) + 4) | 0
                            if ((self.ROM[tempIndex | 0] | 0) == (H | 0)):
                                if ((self.ROM[tempIndex | 1] | 0) == (underScore | 0)):
                                    if ((self.ROM[tempIndex | 2] | 0) == (V | 0)):
                                        flash_types |= 1
                                
                                elif ((self.ROM[tempIndex | 1] | 0) == (five | 0)):
                                    if ((self.ROM[tempIndex | 2] | 0) == (one | 0)):
                                        if ((self.ROM[tempIndex | 3] | 0) == (two | 0)):
                                            tempIndex = ((tempIndex | 0) + 4) | 0
                                            if ((self.ROM[tempIndex | 0] | 0) == (underScore | 0)):
                                                if ((self.ROM[tempIndex | 1] | 0) == (V | 0)):
                                                    flash_types |= 2

                                elif ((self.ROM[tempIndex | 1] | 0) == (one | 0)):
                                    if ((self.ROM[tempIndex | 2] | 0) == (M | 0)):
                                        if ((self.ROM[tempIndex | 3] | 0) == (underScore | 0)):
                                            tempIndex = ((tempIndex | 0) + 4) | 0
                                            if ((self.ROM[tempIndex | 0] | 0) == (V | 0)):
                                                flash_types |= 4
                                                break

        self.flash_is128 = ((flash_types|0) >= 4)
        self.flash_isAtmel = ((flash_types|0) <= 1)

GameBoyAdvanceCartridge.prototype.readROMOnly8 = function (address) {
    address = address | 0;
    var data = 0;
    if ((address | 0) < (this.ROMLength | 0)) {
        data = this.ROM[address & 0x1FFFFFF] | 0;
    }
    return data | 0;
}
if (__LITTLE_ENDIAN__) {
    GameBoyAdvanceCartridge.prototype.readROMOnly16 = function (address) {
        address = address | 0;
        var data = 0;
        if ((address | 0) < (this.ROMLength | 0)) {
            data = this.ROM16[(address >> 1) & 0xFFFFFF] | 0;
        }
        return data | 0;
    }
    GameBoyAdvanceCartridge.prototype.readROMOnly32 = function (address) {
        address = address | 0;
        var data = 0;
        if ((address | 0) < (this.ROMLength | 0)) {
            data = this.ROM32[(address >> 2) & 0x7FFFFF] | 0;
        }
        return data | 0;
    }
}
else {
    GameBoyAdvanceCartridge.prototype.readROMOnly16 = function (address) {
        address = address | 0;
        var data = 0;
        if ((address | 0) < (this.ROMLength | 0)) {
            data = this.ROM[address] | (this.ROM[address | 1] << 8);
        }
        return data | 0;
    }
    GameBoyAdvanceCartridge.prototype.readROMOnly32 = function (address) {
        address = address | 0;
        var data = 0;
        if ((address | 0) < (this.ROMLength | 0)) {
            data = this.ROM[address] | (this.ROM[address | 1] << 8) | (this.ROM[address | 2] << 16)  | (this.ROM[address | 3] << 24);
        }
        return data | 0;
    }
}
GameBoyAdvanceCartridge.prototype.readROM8 = function (address) {
    address = address | 0;
    var data = 0;
    if ((address | 0) > 0xC9) {
        //Definitely ROM:
        data = this.readROMOnly8(address | 0) | 0;
    }
    else {
        //Possibly GPIO:
        data = this.IOCore.saves.readGPIO8(address | 0) | 0;
    }
    return data | 0;
}
GameBoyAdvanceCartridge.prototype.readROM16 = function (address) {
    address = address | 0;
    var data = 0;
    if ((address | 0) > 0xC9) {
        //Definitely ROM:
        data = this.readROMOnly16(address | 0) | 0;
    }
    else {
        //Possibly GPIO:
        data = this.IOCore.saves.readGPIO16(address | 0) | 0;
    }
    return data | 0;
}
GameBoyAdvanceCartridge.prototype.readROM32 = function (address) {
    address = address | 0;
    var data = 0;
    if ((address | 0) > 0xC9) {
        //Definitely ROM:
        data = this.readROMOnly32(address | 0) | 0;
    }
    else {
        //Possibly GPIO:
        data = this.IOCore.saves.readGPIO32(address | 0) | 0;
    }
    return data | 0;
}
GameBoyAdvanceCartridge.prototype.readROM8Space2 = function (address) {
    address = address | 0;
    var data = 0;
    if ((address | 0) >= 0xC4 && (address | 0) < 0xCA) {
        //Possibly GPIO:
        data = this.IOCore.saves.readGPIO8(address | 0) | 0;
    }
    else if ((address | 0) >= (this.EEPROMStart | 0)) {
        //Possibly EEPROM:
        data = this.IOCore.saves.readEEPROM8(address | 0) | 0;
    }
    else {
        //Definitely ROM:
        data = this.readROMOnly8(address | 0) | 0;
    }
    return data | 0;
}
GameBoyAdvanceCartridge.prototype.readROM16Space2 = function (address) {
    address = address | 0;
    var data = 0;
    if ((address | 0) >= 0xC4 && (address | 0) < 0xCA) {
        //Possibly GPIO:
        data = this.IOCore.saves.readGPIO16(address | 0) | 0;
    }
    else if ((address | 0) >= (this.EEPROMStart | 0)) {
        //Possibly EEPROM:
        data = this.IOCore.saves.readEEPROM16(address | 0) | 0;
    }
    else {
        //Definitely ROM:
        data = this.readROMOnly16(address | 0) | 0;
    }
    return data | 0;
}
GameBoyAdvanceCartridge.prototype.readROM32Space2 = function (address) {
    address = address | 0;
    var data = 0;
    if ((address | 0) >= 0xC4 && (address | 0) < 0xCA) {
        //Possibly GPIO:
        data = this.IOCore.saves.readGPIO32(address | 0) | 0;
    }
    else if ((address | 0) >= (this.EEPROMStart | 0)) {
        //Possibly EEPROM:
        data = this.IOCore.saves.readEEPROM32(address | 0) | 0;
    }
    else {
        //Definitely ROM:
        data = this.readROMOnly32(address | 0) | 0;
    }
    return data | 0;
}
GameBoyAdvanceCartridge.prototype.writeROM8 = function (address, data) {
    address = address | 0;
    data = data | 0;
    if ((address | 0) >= 0xC4 && (address | 0) < 0xCA) {
        //GPIO Chip (RTC):
        this.IOCore.saves.writeGPIO8(address | 0, data | 0);
    }
}
GameBoyAdvanceCartridge.prototype.writeROM16 = function (address, data) {
    address = address | 0;
    data = data | 0;
    if ((address | 0) >= 0xC4 && (address | 0) < 0xCA) {
        //GPIO Chip (RTC):
        this.IOCore.saves.writeGPIO16(address | 0, data | 0);
    }
}
GameBoyAdvanceCartridge.prototype.writeROM16DMA = function (address, data) {
    address = address | 0;
    data = data | 0;
    if ((address | 0) >= 0xC4 && (address | 0) < 0xCA) {
        //GPIO Chip (RTC):
        this.IOCore.saves.writeGPIO16(address | 0, data | 0);
    }
    else if ((address | 0) >= (this.EEPROMStart | 0)) {
        //Possibly EEPROM:
        this.IOCore.saves.writeEEPROM16(address | 0, data | 0);
    }
}
GameBoyAdvanceCartridge.prototype.writeROM32 = function (address, data) {
    address = address | 0;
    data = data | 0;
    if ((address | 0) >= 0xC4 && (address | 0) < 0xCA) {
        //GPIO Chip (RTC):
        this.IOCore.saves.writeGPIO32(address | 0, data | 0);
    }
}
    def nextIRQEventTime(self):
        #Nothing yet implement that would fire an IRQ:
        return 0x7FFFFFFF;

