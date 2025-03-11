import csv

input_file= "security_incidents.csv"
output_file="security_incidents_modified.csv"

def process_security_incidents(input_file, output_file):
    # read the csv file
     with open(input_file, mode ='r', newline= "", encoding = "utf-8") as infile:
         reader=csv.reader(infile)
         data =list(reader)

     if data:
        data[0].append("Status")

        for row in data[1:]:
            row.append("Pending")




#write csv file
        with open(output_file, mode= "w", newline="", encoding= "utf-8")as outfile:
            writer = csv.writer(outfile) 
            writer.writerows(data)

if __name__ == "__main__":
    process_security_incidents(input_file , output_file)
    print(f"Modified file saved as { output_file}")