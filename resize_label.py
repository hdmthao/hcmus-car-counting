import csv

scale = 800 / 1920

with open('train_resize_labels.csv', mode='w') as write_file:
    writer = csv.writer(write_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    with open('data/train_labels.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count > 0:
                row[1] = '800'
                row[2] = '450'
                row[4] = int(int(row[4]) * scale)
                row[5] = int(int(row[5]) * scale)
                row[6] = int(int(row[6]) * scale)
                row[7] = int(int(row[7]) * scale)
            writer.writerow(row)
            line_count += 1