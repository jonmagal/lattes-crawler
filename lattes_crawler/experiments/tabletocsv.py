import csv

def save_sheet(file_name, content, title = False):        
    csv_writer = csv.writer(open(file_name, 'wb'))
    if title:
        csv_writer.writerow(title)
    for c in content:
        csv_writer.writerow(c)
        
def user_contents(self, file_name, source, data_types):    
        rows = []
        title = ['id',]
        title += data_types
        
        for research in self.researches:
            row = [research.id,]
            for data_type in data_types:
                content_number = content.objects.count_content(research = research, source = source, 
                                                               data_type = data_type)
                row.append(content_number)
            rows.append(row)
    
        save_sheet(file_name, rows, title)