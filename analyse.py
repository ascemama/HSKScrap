
class AnalyseString:
    def __init__(self, inputString):
        self.inputString=inputString
        self.inputStringLength=len(inputString)
        self.inputStringNbOfChineseChar=0
        self.inputStringNbOfDistinctChineseChar=0
        self.nbHSK1Char=0
        self.nbHSK2Char=0
        self.HSK1Array=AnalyseString.loadHSK('HSK1.txt')
        self.HSK2Array=AnalyseString.loadHSK('HSK2.txt')
        self.HSK3Array=AnalyseString.loadHSK('HSK3.txt')
        self.HSK4Array=AnalyseString.loadHSK('HSK4.txt')
        self.HSK5Array=AnalyseString.loadHSK('HSK5.txt')
        self.HSK6Array=AnalyseString.loadHSK('HSK6.txt')
        self.HSK1MdArray=AnalyseString.fillHSKMdArray(self.HSK1Array)
        self.HSK2MdArray=AnalyseString.fillHSKMdArray(self.HSK2Array)
        self.HSK3MdArray=AnalyseString.fillHSKMdArray(self.HSK3Array)
        self.HSK4MdArray=AnalyseString.fillHSKMdArray(self.HSK4Array)
        self.HSK5MdArray=AnalyseString.fillHSKMdArray(self.HSK5Array)
        self.HSK6MdArray=AnalyseString.fillHSKMdArray(self.HSK6Array)
        self.NonHSKMdArray={}
        self.NbHSK1Char=0
        self.NbHSK2Char=0
        self.NbHSK3Char=0
        self.NbHSK4Char=0
        self.NbHSK5Char=0
        self.NbHSK6Char=0
        self.NbNonHSKCha=0
        self.NbHSK1DistinctChar=0
        self.NbHSK2DistinctChar=0
        self.NbHSK3DistinctChar=0
        self.NbHSK4DistinctChar=0
        self.NbHSK5DistinctChar=0        
        self.NbHSK6DistinctChar=0
        self.NbNonHSKDistinctChar=0
        self.HSK1Percent=0
        self.HSK2Percent=0
        self.HSK3Percent=0
        self.HSK4Percent=0
        self.HSK5Percent=0
        self.HSK6Percent=0

         
         
    def loadHSK(hskFilePath):
        with open(hskFilePath, 'r', encoding='utf8') as f:
            HSKSTR = f.read()
            #print(hskFilePath+" List:\n")
            #print(list(set(HSK1STR)))
        return list(set(HSKSTR))

    def fillHSKMdArray(HSKArray):
        HSKMdArray={}
        for character in HSKArray:
            HSKMdArray[character]=0
        return HSKMdArray

    def characterOcurrence(self,source):
        for character in source:
            if u'\u4e00' <= character <= u'\u9fff':
                self.inputStringNbOfChineseChar=self.inputStringNbOfChineseChar+1
                if character in self.HSK1MdArray:
                    self.HSK1MdArray[character]=self.HSK1MdArray[character]+1
                else:
                    if character in self.HSK2MdArray:
                        self.HSK2MdArray[character]=self.HSK2MdArray[character]+1
                    else:
                        if character in self.HSK3MdArray:
                            self.HSK3MdArray[character]=self.HSK3MdArray[character]+1
                        else:
                            if character in self.HSK4MdArray:
                                self.HSK4MdArray[character]=self.HSK4MdArray[character]+1
                            else:
                                if character in self.HSK5MdArray:
                                    self.HSK5MdArray[character]=self.HSK5MdArray[character]+1
                                else:
                                    if character in self.HSK6MdArray:
                                        self.HSK6MdArray[character]=self.HSK6MdArray[character]+1
                                    else:
                                        if character not in self.NonHSKMdArray:
                                            self.NonHSKMdArray[character]=0
                                        else:
                                            self.NonHSKMdArray[character]=self.NonHSKMdArray[character]+1

        #print("HSKMdTArray List:\n")
        #print(HSKMdArray)
        #return HSKMdArray

    def AnalysHSKProfile(self):
        self.characterOcurrence(self.inputString)
        self.ComputeNbHSKXChar()
        self.ComputeNbHSKXDistinctChar()
        self.ComputePercentage()

    
    def ComputePercentage(self):
        NbDistinctChar=self.NbHSK1DistinctChar+self.NbHSK2DistinctChar+self.NbHSK3DistinctChar+self.NbHSK4DistinctChar+self.NbHSK5DistinctChar+self.NbHSK6DistinctChar+self.NbNonHSKDistinctChar
        if NbDistinctChar != 0:
            self.HSK1Percent=self.NbHSK1DistinctChar/NbDistinctChar*100
            self.HSK2Percent=self.NbHSK2DistinctChar/NbDistinctChar*100
            self.HSK3Percent=self.NbHSK3DistinctChar/NbDistinctChar*100
            self.HSK4Percent=self.NbHSK4DistinctChar/NbDistinctChar*100
            self.HSK5Percent=self.NbHSK5DistinctChar/NbDistinctChar*100
            self.HSK6Percent=self.NbHSK6DistinctChar/NbDistinctChar*100
        #print("NbDistinctChar:"+str(NbDistinctChar))
        #print("HSK1Percent:"+str(self.HSK1Percent))
        #print("HSK2Percent:"+str(self.HSK2Percent))
        #print("HSK3Percent:"+str(self.HSK3Percent))
        #print("HSK4Percent:"+str(self.HSK4Percent))
        #print("HSK5Percent:"+str(self.HSK5Percent))
        #print("HSK6Percent:"+str(self.HSK6Percent))
    
    def ComputeNbHSKXChar(self):
        #print("NbChar in Site: "+str(self.inputStringLength))
        #print("Nb Chinese Char in Site: "+str(self.inputStringNbOfChineseChar))
        self.NbHSK1Char=AnalyseString.ComputeNbChar(self.HSK1MdArray)
        self.NbHSK2Char=AnalyseString.ComputeNbChar(self.HSK2MdArray)
        self.NbHSK3Char=AnalyseString.ComputeNbChar(self.HSK3MdArray)
        self.NbHSK4Char=AnalyseString.ComputeNbChar(self.HSK4MdArray)
        self.NbHSK5Char=AnalyseString.ComputeNbChar(self.HSK5MdArray)
        self.NbHSK6Char=AnalyseString.ComputeNbChar(self.HSK6MdArray)
        self.NbNonHSKChar=AnalyseString.ComputeNbChar(self.NonHSKMdArray)
         
        #print("NbChar HSK1: "+str(self.NbHSK1Char))
        #print("NbChar HSK2: "+str(self.NbHSK2Char))
        #print("NbChar HSK3: "+str(self.NbHSK3Char))
        #print("NbChar HSK4: "+str(self.NbHSK4Char))
        #print("NbChar HSK5: "+str(self.NbHSK5Char))
        #print("NbChar HSK6: "+str(self.NbHSK6Char))
        #print("NbChar Non-HSK: "+str(self.NbNonHSKChar))

    def ComputeNbChar(HSKXMdArray):
        NbChar=0
        for key in HSKXMdArray:
            NbChar=NbChar+HSKXMdArray[key]
        return NbChar
    
    def ComputeNbHSKXDistinctChar(self):

        self.NbHSK1DistinctChar=AnalyseString.ComputeNbDistinctChar(self.HSK1MdArray)
        self.NbHSK2DistinctChar=AnalyseString.ComputeNbDistinctChar(self.HSK2MdArray)
        self.NbHSK3DistinctChar=AnalyseString.ComputeNbDistinctChar(self.HSK3MdArray)
        self.NbHSK4DistinctChar=AnalyseString.ComputeNbDistinctChar(self.HSK4MdArray)
        self.NbHSK5DistinctChar=AnalyseString.ComputeNbDistinctChar(self.HSK5MdArray)
        self.NbHSK6DistinctChar=AnalyseString.ComputeNbDistinctChar(self.HSK6MdArray)
        self.NbNonHSKDistinctChar=AnalyseString.ComputeNbDistinctChar(self.NonHSKMdArray)
         
        #print("NbChar distinct HSK1: "+str(self.NbHSK1DistinctChar))
        #print("NbChar distinct HSK2: "+str(self.NbHSK2DistinctChar))
        #print("NbChar distinct HSK3: "+str(self.NbHSK3DistinctChar))
        #print("NbChar distinct HSK4: "+str(self.NbHSK4DistinctChar))
        #print("NbChar distinct HSK5: "+str(self.NbHSK5DistinctChar))
        #print("NbChar distinct HSK6: "+str(self.NbHSK6DistinctChar))
        #print("NbChar distinct Non-HSK: "+str(self.NbNonHSKDistinctChar))


    def ComputeNbDistinctChar(HSKXMdArray):
        NbChar=0
        for key in HSKXMdArray:
            if HSKXMdArray[key]!= 0:
                NbChar=NbChar+1
        return NbChar

    
def main():
     
    with open('Chinese.txt', 'r', encoding='utf8') as f:
        sitestr = f.read()
        #characterOcurrence(hsk1List,sitestr)
        Ana=AnalyseString(sitestr)
        Ana.AnalysHSKProfile()
       # Ana.ComputeNbHSKXChar()
       # Ana.ComputeNbHSKXDistinctChar()

if __name__ == "__main__":
    main()



# HSK1STR=""
# with open('HSK1.txt', 'r', encoding='utf8') as f:
#     HSK1STR = f.read()
# HSK1TAB=list(set(HSK1STR))
# #HSK1TAB=HSK1STR.split("\n")
# print("HSK1 List:\n")
# print(HSK1TAB)

# HSK1TabMD={}
# for character in HSK1TAB:
#     HSK1TabMD[character]=0

# sitestr=""
# with open('Chinese.txt', 'r', encoding='utf8') as f:
#     sitestr = f.read()

# for character in sitestr:
#     if character in HSK1TabMD:
#         HSK1TabMD[character]=HSK1TabMD[character]+1
# print("HSK1TabMD List:\n")
# print(HSK1TabMD)







