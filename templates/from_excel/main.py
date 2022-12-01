#coding=utf-8
import pandas
import warnings

warnings.simplefilter("ignore")
src = "src/channels.xlsx"
channels = pandas.read_excel(src)
count = 0

results = open('results/results.sql','w')

for index, row in channels.iterrows():
    if (pandas.isna(row['課程ID'])):
        break
    else:
        id = int(row['課程ID'])+355
        # print(id)
        # break

        sql = "update channels set category_id={} where id = {};\n".format(int(row[17]),id)
        results.write(sql)
# 連線關閉
results.close()
print('處理結束')

