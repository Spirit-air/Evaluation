import argparse
import pandas as pd
from pathlib import Path
import AMR_para
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
#对话数据集
def process_txt(file_path):
    content = Path(file_path).read_text()
    return content
# 提问数据集
def process_RACE(file_path):
    df = pd.read_parquet(file_path)
    questions = df['question']
    options = df['options']
    # 检查是否存在'article'列
    articles = df['article']
    answer_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    
    df['selected_option'] = df.apply(lambda row: row['options'][answer_map[row['answer']]], axis=1)
    extracted_answers=df['selected_option']
    return questions, articles, extracted_answers

def process_truthful(file_path):
    df = pd.read_parquet(file_path)
    pd.set_option('display.max_colwidth', None)
    questions = df['question']
    # 合并所有correct答案
    df['answers'] = df.apply(lambda row: [row['best_answer']] + [ans for ans in row['correct_answers'] if ans != row['best_answer']], axis=1)
    answers = df['answers']
    return questions, answers
if __name__=='__main__':
#设计命令行解析方法
        parser = argparse.ArgumentParser(description='create convs from same amr')
     # 句子数据文件名称
        parser.add_argument('--fname', type=str, default='train', help='type of data to generate amr parsing for its convs')
     # 聊天的数据文件目录
        parser.add_argument('--path', type=str, default='data/Topical_Chat/', help='the path of the file')
    # 数据类型
        parser.add_argument('--ftype', type=str)
        args = parser.parse_args()
    # 使用命令行，输入和输出文件名格式(原始句子名字)
        file_type = args.ftype
        fname = '{}/{}.{}'.format(args.path, args.fname, args.ftype)
        foutput = '{}/parsed_{}.txt'.format(args.path, args.fname)        
        # 打开文件
        
        if file_type == 'txt':
            question = process_txt(fname)           
        elif file_type == 'parquet':
            if args.fname == 'RACE':
                race_quest, race_artic, race_answers = process_RACE(fname)
                Paraphrasing.parse2AMR(race_quest)
                
            elif args.fname == 'truthfulQA':
                truthfulQA_quest, truthfulQA_answer = process_truthful(fname)
                AMR_para.parse2AMR(truthfulQA_quest)
                # print(truthfulQA_quest.head())
        #处理文件数据
        # split_convs(fr)
