import csv
vec=[]
with open ('IntroToPy/mountains_db.tsv', newline ='', encoding='UTF-8-sig') as durdur:
    rows=csv.reader (durdur, delimiter='\t')
    for row in rows:
        if row:
            print (row)

for chestie in vec:
    print (chestie[0])