import glob
import json 

all_files = glob.glob("raw_output/*.json")

for file_name in all_files:

    # Read the file
    with open(file_name) as f:
        data = json.load(f)

    for program_file in data["files"]:
        for mutant_count, mutant in enumerate(data["files"][program_file]["mutants"]):

            # Got the mutant
            print(mutant["id"])
            print(mutant["location"])
            print(mutant["mutatorName"])
            print(mutant["replacement"])
            print(mutant["status"])
            print("")

            # # Read the original cpp file
            original_program = open(program_file, 'r')
            lines = original_program.readlines()

            # Line Number (assuming lines number)
            line_number = mutant["location"]["start"]["line"]
            start_c = mutant["location"]["start"]["column"]
            end_c = mutant["location"]["end"]["column"]
            replacement = mutant["replacement"]

            # Create an output file
            processed_file_name = program_file[program_file.rfind("/")+1:]
            file_type = program_file[program_file.rfind("."):]
            processed_file_name = processed_file_name[:processed_file_name.find(".")]
            processed_file_name = processed_file_name + "_mutant{}".format(mutant_count) + file_type
            
            output_file = open("./output/" + processed_file_name, 'w')

            for i, line in enumerate(lines):
                current_line_number = i + 1

                if current_line_number == line_number:
                    new_line = line[:start_c-1] + replacement + line[end_c-1:]
                else:
                    new_line = line

                output_file.write(new_line)

            output_file.close()
            original_program.close()

        