import csv

if __name__ == "__main__":
    file_path = "./addresses.csv" # Path to .csv file

    with open(file_path) as my_file: # Using "with" statement ensures that file will be closed afterwards.

        # Using list comprehension
        # data = [line for line in my_file]
        # print(f"This is using the List Comprehension Way: {data}")

        # csv_reader = csv.reader(my_file)
        # print(f"This uses the csv_reader way from the csv import: ")
        # for row in csv_reader:
        #     print(row)

        print("This uses the dictreader from the csv import: ")
        dict_reader = csv.DictReader(my_file)
        for line in dict_reader:
            print(line)
