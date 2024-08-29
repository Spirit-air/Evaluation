import argparse
import pandas as pd
from pathlib import Path

def amr_parsing(path):
    stog = amrlib.load_stog_model(Bart_path)
    sentence=[]
    with open(path, 'r') as rf:
        lines = rf.readlines()
    sentence = [line.strip() for line in lines]
    graphs = stog.parse_sents(sentence)
    with open('../data/parse_amr.txt', 'w') as f:
        f.write("".join(graphs))
    return "".join(sentence)

def split_convs(readf):
     convs = readf.readlines()

def process_txt(file_path):
    content = Path(file_path).read_text()
    print(content)

def process_parquet(file_path):
    df = pd.read_parquet(file_path)
    print(df.head())
     
if __name__=='__main__':
#设计命令行解析方法
        parser = argparse.ArgumentParser(description='create convs from same amr')
     # 句子数据文件名称
        parser.add_argument('--fname', type=str, default='train', help='type of data to generate amr parsing for its convs')
     # 聊天的数据文件目录
        parser.add_argument('--path', type=str, default='data/Topical_Chat/', help='the path of the file')
    # 数据类型
        parser.add_argument('--ftype',type=str)
        args = parser.parse_args()
    # 使用命令行，输入和输出文件名格式(原始句子名字)
        file_type = args.ftype
        fname = '{}/{}.{}}'.format(args.path, args.fname,args.ftype)
        foutput = '{}/parsed_{}.txt'.format(args.path, args.fname)        
        # 打开文件
        if file_type == 'txt':
            content = Path(fname).read_text()
        elif file_type == 'parquet':
            content = pd.read_parquet(fname)

        print(content[1])
        #处理文件数据
        # split_convs(fr)
