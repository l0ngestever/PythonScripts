import sys
import csv
import sqlite3


if __name__ in '__main__':
    print '== Import CSV into database ==\n'

    files = []

    if (len(sys.argv) < 3):
        print 'No arguments found. Use ' + sys.argv[0] + ' <database name> <csv file 1> <csv file 2> etc. csv files'
        sys.exit(0)
    else:
        for arg in sys.argv:
            if not arg == sys.argv[0] and not arg == sys.argv[1]:
                files.append(arg)

    db = sqlite3.connect(sys.argv[1])

    for fileName in files:
        with open(fileName, 'r') as f:
            cursor = db.cursor()

            reader = csv.reader(f)

            tableName = fileName[:-4]
            columns = ', '.join(next(reader))

            SQL = "CREATE TABLE " + tableName + " (" + columns + ");"

            for row in reader:
                tmpData = []
                for item in row:
                    tmpData.append("\"" + item + "\"")
                data = ', '.join(tmpData)
                SQL += "\nINSERT INTO " + tableName + " (" + columns + ") VALUES (" + data + ");"

            cursor.executescript(SQL)

            print '== Creating table ' + tableName + ' succesfully! =='

    print '\n== Import succesfully! =='
