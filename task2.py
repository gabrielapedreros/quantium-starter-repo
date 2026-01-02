"""DATA PROCESSING: Soul Foods csv files - Morsel transaction data
Layers
Writer - Output
 Input Processing
  Row Handling
"""

import csv #cvs files are spreadsheets, usually human edit

def readFiles(inputFile, outputWriter):                
    #with open('daily_sales_data_0.csv') as csv_file:
    #newline:
    with open(inputFile, newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader, None) #skip header
        #variables
        rows_read = 0 #per input file
        rows_written = 0 #per output file

        for row in csv_reader:
            rows_read += 1 #skip header
            if len(row) < 5: #5 rows
                continue
                #if rows_read == 0:
                    #print(f'Column names are {", ".join(row)}') #check header file, then
                        #product, price, quantity, date, region
                        #row[0],row[1],row[2],row[3],row[4]
                    #ignore header file
            product = row[0].strip().lower()
                #else:
                    #rows_read += 1
                #normalization for text comparison
                    #product = row[0]
                    #print(product)
                    #normProd = product.lower()
                    #print(normProd)
                    #no_white_space_normProd = normProd.strip()
                    #print(no_white_space_normProd)
                    # if no_white_space_normProd == "pink morsel": 
                    #print (f'\tsold {row[2]} {row[0]} for {row[1]} each on {row[3]} in the {row[4]} region.')
                    #print(no_white_space_normProd)
            if product == "pink morsel":
                price = row[1].strip().replace("$","")
                quantity = row[2].strip()

                priceFinal = float(price)
                quantityFinal=int(quantity)

                sales = priceFinal*quantityFinal #quantity x price (total sales for a given day)
                date = row[3].strip()
                region = row[4].strip()  
                    
                    #type conversion
                    #price = row[1]
                    #print(price)
                    #newPrice = price.replace("$","")
                    #print(newPrice)
                    #priceFinal = float(newPrice)
                    #print(priceFinal)

                    #quantity = row[2]
                    #print(quantity)
                    
                    #quantityFinal = int(quantity)
                    #print(quantityFinal)

                    #sales = priceFinal * quantityFinal
                    #print(sales)

                outputWriter.writerow([f"{sales:.2f}", date, region])
                rows_written += 1
        print(f'Processed {rows_read} lines in {inputFile}. {rows_written} rows written in the output file.')

def main():
    file0 = 'data/daily_sales_data_0.csv'
    file1 = 'data/daily_sales_data_1.csv'
    file2 = 'data/daily_sales_data_2.csv'
    #added new line
    with open('output_file.csv', mode ='w', newline='') as output_file: 
        output_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        output_writer.writerow(['Sales','Date','Region'])
        readFiles(file0, output_writer)
        readFiles(file1, output_writer)
        readFiles(file2, output_writer)

    print(f'Processed {file0}, {file1}, {file2}. Output file is done.')

if __name__ ==  "__main__":
    main()