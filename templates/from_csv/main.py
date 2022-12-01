#coding=utf-8
import pandas

src = "src/xxx.csv"
rows = pandas.read_csv(src,encoding='utf-8')
count = 0

sql_file = open('results/result.sql','w')

for index, row in rows.iterrows():
    id = row['ID']
    title = row['column']

    sql = "INSERT INTO `tables` (`id`,`column`) VALUES ({},'{}'));\n".format(id,title)
    sql_file.write(sql)

sql_file.close()

print('處理結束')

