with open("pandas_output_csv_file.csv") as f:
    for i in range(3):
        print(f.readline(), end="")