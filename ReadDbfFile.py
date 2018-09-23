from dbfread import DBF
import os

def getDirPath():
    return (os.path.dirname(__file__))

def opendb (filename):
    tb = DBF(filename)
    return tb


if __name__ == "__main__":
    table = opendb("gkcf.dbf")
    for record in table:
        for field in record:
            print(field,"=",record[field], end = ",")
        print()

