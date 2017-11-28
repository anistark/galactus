from pyfiglet import Figlet
import glob, os
import pandas
import gzip
import shutil

all_extensions = [".log", ".dmg", ".png", ".jpg", ".mp3", ".mp4"]

# Max file size allowed
max_file_size = 5242880 # in bytes => 5MB

# file_data
file_data = {
    'file_path': [],
    'size': [],
    'formatted_size': []
}

# big files only
big_file_data = {
    'file_path': [],
    'size': [],
    'formatted_size': []
}


dir_path = os.getcwd()+"/temp"

def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB', 'XB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

def find_files(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith(tuple(all_extensions)):
                file_path = os.path.join(root, file)
                file_size = os.stat(file_path).st_size
                # Write to file_data
                file_data['file_path'].append(file_path)
                file_data['size'].append(file_size)
                file_data['formatted_size'].append(convert_bytes(file_size))
                if float(file_size) > float(max_file_size):
                    big_file_data['file_path'].append(file_path)
                    big_file_data['size'].append(file_size)
                    big_file_data['formatted_size'].append(convert_bytes(file_size))
    return pandas.DataFrame(big_file_data).sort_values('size', ascending=False)

def compress_file(input_file_path):
    output_file_path = input_file_path+'.gz'
    with open(input_file_path, 'rb') as f_in, gzip.open(output_file_path, 'wb') as f_out:
        file_response = shutil.copyfileobj(f_in, f_out)
    compressed_by_size = float(os.stat(input_file_path).st_size)-float(os.stat(output_file_path).st_size)
    return {
        'compressed_file': output_file_path,
        'compressed_by_size': compressed_by_size,
        'compressed_by_size_formatted': convert_bytes(compressed_by_size)
    }

if __name__ == "__main__":
    f = Figlet(font='lean')
    print(f.renderText('Galactus'), 'welcomes you!')
    print('Find files in:', dir_path)
    df_response = find_files(dir_path)
    total_files_compress = len(df_response['size'])
    for i in range(total_files_compress):
        compressed_file_data = compress_file(df_response['file_path'][i])
        print('compressed_file_data', compressed_file_data)
