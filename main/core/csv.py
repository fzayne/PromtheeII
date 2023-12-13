import csv
import io
def read_csv(file):
    matrix_data = []
    title=[]
    # with open(filename, 'r') as file:
    csv_data = io.StringIO(file.stream.read().decode('utf-8'))
    csv_reader = csv.reader(csv_data)
    for row in csv_reader:
        current_row=[]
        for cell in row:
            try:
               current_row.append(float(cell))
            except:
               title.append(cell)
        if current_row != []:
            matrix_data.append(current_row)
     
    return (matrix_data,title)