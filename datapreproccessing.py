import csv

data_set_1=[]
data_set_2=[]

with open("final.csv","r") as f:
    csv_reader=csv.reader(f)
    for row in csv_reader:
        data_set_1.append(row)

with open("archieve_dataset_sorted_1.csv","r") as g:
    csv_reader_2=csv.reader(g)
    for row in csv_reader_2:
        data_set_2.append(row)

header_1=data_set_1[0]
header_2=data_set_2[0]

planet_data_1=data_set_1[1:]
planet_data_2=data_set_2[1:]

headers=header_1+header_2

planet_data=[]

for index,data_row in enumerate(planet_data_2):
    planet_data.append(planet_data_1[index]+planet_data_2[index])

with open("mergedataset.csv","a") as d:
    csv_writer=csv.writer(d)
    csv_writer.writerow(headers)
    csv_writer.writerow(planet_data)
