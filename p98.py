def swapFileData():
    firstFile = input("File Name: ")
    anotherFile = input("Other File Name: ")
    A = open(firstFile)
    B =open(anotherFile)
    dataA = A.read()
    dataB = B.read()
    Aa = open(firstFile,"w")
    Bb = open(anotherFile,"w")
    Aa.write(dataB)
    Bb.write(dataA)

swapFileData()