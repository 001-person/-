import os
import os.path

dir = 'read_view'

def delate_py(path):
    try:
        os.remove(path)
    except:
        return 0
    return 1

def get_ui_file():
    files = os.listdir(dir)
    for file in files:
        if os.path.splitext(file)[1] == '.ui':
            return file

def get_py_name(ui_file):
    return os.path.splitext(ui_file)[0] + '.py'

def runMain():
    ui_file = get_ui_file()
    py_file = get_py_name(ui_file)
    delate_py(dir+'/'+py_file)
    cmd = 'pyuic5 -o {pyfile} {uifile}'.format(pyfile=dir+'/'+py_file, uifile=dir+'/'+ui_file)
    os.system(cmd)


if __name__ == '__main__':
    runMain()
