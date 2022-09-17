import csv

data=[]

with open("archive_dataset.csv","r") as f:
    csv_reader=csv.reader(f)
    for row in csv_reader:
        data.append(row)

headers=data[0]
planet_data=data[1:]

for data_point in planet_data:
    data_point[2]=data_point[2].lower()

planet_data.sort(key=lambda planet_data:planet_data[2])


with open("archieve_dataset_sorted.csv","a+") as g:
    csv_writer=csv.writer(g)
    csv_writer.writerow(headers)
    csv_writer.writerow(planet_data)

with open("archieve_dataset_sorted.csv") as input,open("archieve_dataset_sorted_1.csv","w",newline='') as output:
    writer=csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip() for field in row):
            writer.writerow(row)







    


    