import os
import sys
import time
from pathlib import Path

class File:

    def __init__(self, path):
        self.path = path
        self.pathstr = str(path)

    def read_size(self):
        return self.path.stat().st_size

    def __repr__(self):
        return self.pathstr

    def __eq__(self, value):
        return self.pathstr == value.pathstr

    def __hash__(self):
        return hash(self.pathstr)


def convert_file_to_filepath(file):
    return file.pathstr.replace(' ', '\ ')

def readable_bytes(b):
    kb = b / 1024.0
    mb = kb / 1024.0
    if mb > 1:
        return "{:.2f}MB".format(mb)
    elif kb > 1:
        return "{:.2f}KB".format(kb)
    else:
        return "{:.2f}B".format(b)

def find_png_files(dir=None, limit=None):
    if dir is None:
        p_dir = Path.cwd()
    else:
        p_dir = Path(dir)

    files = []
    count = 0
    for p_file in p_dir.rglob('*.png'):
        file = File(p_file)
        files.append(file)
        count += 1
        if limit is not None and count > limit:
            break

    return files

def run_pngquant_with_files(files, debug=False):
    run_pngquant(list(map(convert_file_to_filepath, files)), debug=debug)

def run_pngquant(filepaths, debug=False):
    cmd = "pngquant --ext=.png --force "
    cmd += " ".join(filepaths)
    if not debug:
        os.system(cmd)


def run(dir=None, debug=False):
    if debug:
        print("------------------ 开启调试模式 ------------------")
        time.sleep(1)

    files = find_png_files(dir)
    
    file_records = {}
    for file in files:
        file_records[file] = file.read_size()
    
    batch = 10
    if len(files) <= batch:
        run_pngquant_with_files(files, debug)
        log_progress(files, file_records, debug)
    else:
        chunks = small_chunks(files, batch)
        for chunk in chunks:
            run_pngquant_with_files(chunk, debug)
            log_progress(chunk, file_records, debug)
            if not debug:
                time.sleep(0.5)
    if debug:
        print(f"一共找到{len(files)}张图片。")
    else:
        print(f"一共找到并压缩{len(files)}张图片。")

def small_chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i+n]

def log_progress(files, file_records, debug=False):
    sub_records = {}
    if len(files) == len(file_records):
        sub_records = file_records
    else:
        sub_records = {file: file_records[file] for file in files}
    
    for file, oldsize in sub_records.items():
        newsize = file.read_size()
        reduce_amount = (oldsize - newsize) * 1.0 / oldsize * 100.0
        if reduce_amount < 0:
            reduce_amount = 0
        if debug:
            print(f"{file.pathstr}")
        else:
            print("({:.0f}%) {}".format(reduce_amount, file.pathstr))

def get_param(param, default, args):
    # 主要参数
    if param is None:
        for arg in args:
            if "--" not in arg:
                return arg
    # 布尔选项
    if param in args:
        return True
    # 赋值选项
    for arg in args:
        if "=" in arg:
            components = arg.split("=")
            if param == components[0]:
                return components[1]
    # 没有找到参数
    return default

def log_help():
    text = """
    thinner程序用于查找并裁剪png图片资源，以减少图片体积。
    使用该程序需要预先安装python3.5+以及pngquant程序！
    
    使用: 
    python thinner.py [options] [根目录地址]
    如果没有根目录地址，默认为当前目录

    选项:
    --debug     仅打印查找的图片资源，不做图片处理
    --help      帮助菜单
    """
    print(text)

if __name__ == '__main__':
    args = sys.argv[1:]
    is_help = get_param("--help", False, args)
    if is_help:
        log_help()
    else:
        debug = get_param("--debug", False, args)
        directory = get_param(None, str(Path.cwd()), args)
        run(dir=directory, debug=debug)