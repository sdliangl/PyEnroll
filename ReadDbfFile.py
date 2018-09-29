# 读取dbf文件的Demo

from dbfread import DBF



def opendb (filename):
    tb = DBF(filename, load=True)
    return tb


if __name__ == "__main__":
    table = opendb("gkcf.dbf")
    for record in table.deleted:
        for field in record:
            print(field,"=",record[field], end = ",")
        print()

