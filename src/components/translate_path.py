# This function must receive the path and return a tuple with the filename and the path
def translate(file_path):
    file_name = file_path.split('/')[-1]
    file_path = '/'.join(file_path.split('/')[0:-1]) + '/'
    return (file_name, file_path)