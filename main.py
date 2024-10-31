import os
import shutil
from PIL import Image
import pillow_heif

input_path = "input"
output_path = "output"

# print(os.listdir(input_path))
input_files = os.listdir(input_path)
input_files_length = len(input_files)
progress = 0

if input_files and input_files_length > 1:
    for input_file in input_files:
        input_file_path = input_path + "/" + input_file
        if input_file[0] != ".":
            split_file = input_file.split(".")
            if len(split_file) < 3 and split_file[1] == "HEIC" and split_file[0][0] != ".":
                print("heic" + input_file)
                output_file_path = output_path + "/" + "".join(split_file[:-1]) + ".jpg"
                try:
                    heif_image = pillow_heif.open_heif(input_file_path)

                    image = Image.frombytes(
                        heif_image.mode,
                        heif_image.size,
                        heif_image.data,
                        "raw",
                        heif_image.mode,
                        heif_image.stride
                    )
                    image.save(output_file_path, "JPEG")
                    print(f'Converted ')
                except Exception as e:
                    print("Error occurred while opening the " + input_file + " file. Error code: " + str(e))
            else:
                shutil.copyfile(input_path + "/" + input_file, output_path + "/" + input_file)
            progress += 1
            print("Progress: " + str(progress) + "/" + str(input_files_length))
else:
    print("No files found in the input directory!")

