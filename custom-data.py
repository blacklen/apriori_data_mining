import csv

indexPath = "Book4.csv"

with open(indexPath) as f:
    reader = list(csv.reader(f))
    data = dict()
    data2 = dict()
    for row in reader[0:]:
        if int(row[3]) > 0:
            if row[0] not in data2:
                data2[row[0]] = [row[1]]
            else:
                data2[row[0]].append(row[1])
    # print(len(data))

    # with open('custom-data.csv', mode='w') as file:
    #     writer = csv.writer(file, delimiter=',')
    #     for key,value in data.items():
    #         writer.writerow(value)
        if int(row[3]) > 0 and len(row[1]) > 0:
            if row[1] not in data:
                data[row[1]] = 1
            else:
                data[row[1]] += 1

    list_item = list()
    with open('custom-apriori4.csv','w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        for key,value in data.items():
            list_item.append(key)
        writer.writerow([list_item,";"])
        for key, value in data2.items():
            row = list()
            for i in list_item:
                if i in value:
                    row.append("YES")
                else:
                    row.append("NO")
            row.append(';')
            writer.writerow(row)

    print(len(data))
    print(len(data2))
    f.close()