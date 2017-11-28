from pyfiglet import Figlet
import glob, os
import pandas

f = Figlet(font='lean')
print(f.renderText('Galactus'))

def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB', 'XB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


# Sample file_data
file_data = {
    'file_path': [],
    'size': [],
    'formatted_size': []
}

dir_path = "/var/log"

for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith(".log"):
            file_path = os.path.join(root, file)
            file_size = os.stat(file_path).st_size
            # Write to file_data
            file_data['file_path'].append(file_path)
            file_data['size'].append(file_size)
            file_data['formatted_size'].append(convert_bytes(file_size))

df_response = pandas.DataFrame(file_data).sort_values('size', ascending=False)

print(df_response)
