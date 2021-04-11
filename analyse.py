
class AnalyseString:
    def __init__(self, inputString):
        self.inputString=inputString
        self.inputStringLength=len(inputString)
        self.nbHSK1Char=0
        self.nbHSK2Char=0
        self.HSK1Array=AnalyseString.loadHSK('HSK1.txt')
        self.HSK2Array=AnalyseString.loadHSK('HSK2.txt')
        self.HSK3Array=AnalyseString.loadHSK('HSK3.txt')
        self.HSK4Array=AnalyseString.loadHSK('HSK4.txt')
        self.HSK5Array=AnalyseString.loadHSK('HSK5.txt')
        self.HSK6Array=AnalyseString.loadHSK('HSK6.txt')
         
    def loadHSK(hskFilePath):
        with open(hskFilePath, 'r', encoding='utf8') as f:
            HSK1STR = f.read()
            print(hskFilePath+" List:\n")
            print(list(set(HSK1STR)))
        return list(set(HSK1STR))

    def characterOcurrence(hskArray, source):
        HSKMdArray={}
        for character in hskArray:
            HSKMdArray[character]=0
        for character in source:
            if character in hskArray:
                HSKMdArray[character]=HSKMdArray[character]+1
        print("HSKMdTArray List:\n")
        print(HSKMdArray)
        return HSKMdArray

    def AnalysHSKProfile(self):
        self.HSK1MdArray=AnalyseString.characterOcurrence(self.HSK1Array,self.inputString)
        self.HSK2MdArray=AnalyseString.characterOcurrence(self.HSK2Array,self.inputString)
        self.HSK3MdArray=AnalyseString.characterOcurrence(self.HSK3Array,self.inputString)
        self.HSK4MdArray=AnalyseString.characterOcurrence(self.HSK4Array,self.inputString)
        self.HSK5MdArray=AnalyseString.characterOcurrence(self.HSK5Array,self.inputString)
        self.HSK6MdArray=AnalyseString.characterOcurrence(self.HSK6Array,self.inputString)
    
    def ComputeNbHSKXChar(self):
        print("NbChar in Site: "+str(self.inputStringLength))
        self.NbHSK1Char=AnalyseString.ComputeNbChar(self.HSK1MdArray)
        self.NbHSK2Char=AnalyseString.ComputeNbChar(self.HSK2MdArray)
        self.NbHSK3Char=AnalyseString.ComputeNbChar(self.HSK3MdArray)
        self.NbHSK4Char=AnalyseString.ComputeNbChar(self.HSK4MdArray)
        self.NbHSK5Char=AnalyseString.ComputeNbChar(self.HSK5MdArray)
        self.NbHSK6Char=AnalyseString.ComputeNbChar(self.HSK6MdArray)
         
        print("NbChar HSK1: "+str(AnalyseString.ComputeNbChar(self.HSK1MdArray)))
        print("NbChar HSK2: "+str(AnalyseString.ComputeNbChar(self.HSK2MdArray)))
        print("NbChar HSK3: "+str(AnalyseString.ComputeNbChar(self.HSK3MdArray)))
        print("NbChar HSK4: "+str(AnalyseString.ComputeNbChar(self.HSK4MdArray)))
        print("NbChar HSK5: "+str(AnalyseString.ComputeNbChar(self.HSK5MdArray)))
        print("NbChar HSK6: "+str(AnalyseString.ComputeNbChar(self.HSK6MdArray)))
        print("NbChar Non-HSK: "+str(self.inputStringLength-self.NbHSK1Char-self.NbHSK2Char-self.NbHSK3Char-self.NbHSK4Char-self.NbHSK5Char-self.NbHSK6Char))

    def ComputeNbChar(HSKXMdArray):
        NbChar=0
        for key in HSKXMdArray:
            NbChar=NbChar+HSKXMdArray[key]
        return NbChar

    
def main():
     
    with open('Chinese.txt', 'r', encoding='utf8') as f:
        sitestr = f.read()
        #characterOcurrence(hsk1List,sitestr)
        Ana=AnalyseString(sitestr)
        Ana.AnalysHSKProfile()
        Ana.ComputeNbHSKXChar()

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







