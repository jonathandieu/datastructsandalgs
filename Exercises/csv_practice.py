import csv

if __name__ == "__main__":
    file_path = "./addresses.csv" # Path to .csv file

    with open(file_path) as my_file: # Using "with" statement ensures that file will be closed afterwards.

        # Using list comprehension
        data = [line for line in my_file]
        print(f"This is using the List Comprehension Way: {data}")

        csv_reader = csv.reader(my_file)
        print(f"This is using the csv_reader way from the csv import: ")
        for row in csv_reader:
            print(row)
