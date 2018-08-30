import pandas as pd
import os
from pandas import ExcelWriter

main_directory = "D:\\Indices\\Indices8-24-18\\"

output_directory = "D:\\Indices\\output\\"

targets = ["DOW30", "SP500", "NSDQ"]


files = {}

for each_dir in os.listdir(main_directory):

        path = main_directory + each_dir + "\\"

        filename = path + os.listdir(path)[0]

        files[each_dir] =  pd.read_csv(filename, sep=",", converters={"Price" : lambda x: float(repr(x,",.2f"))})

        files[each_dir].columns = files[each_dir].columns + "_" + each_dir


output_data_table = {}

for target in targets :

    for source in files:

        if source != target :

            target_index = "Date_" + target
            source_index = "Date_" + source

            output_file_name = target + "vs" + source

            output_data_table[output_file_name] = files[target].join(files[source].set_index(source_index),on = target_index)

            output_file = output_directory + output_file_name + ".xlsx"

            writer = ExcelWriter(output_file)

            output_data_table[output_file_name].to_excel(writer, index=False)

            writer.save()




