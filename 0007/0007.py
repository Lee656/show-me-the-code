#coding: utf-8
# 未考虑嵌套注释
# 未考虑字符串中使用多行注释
# 未考虑使用"""abcde"""定义字符串

import os,re
# 我是注释
def _count(path):
    whiteline, code, comment = 0, 0, 0
    with open(path, 'r') as fin:
        for idx, line in enumerate(fin):
            line = line.strip()
            if line.strip() == '': # 统计空白行
                whiteline += 1
                continue
            elif re.search(r'#[^\'"]*?$', line):
                comment += 1
                if not line.startswith('#'):
                    code += 1
            else: code += 1
        fin.seek(0)
        content = fin.read()
        match = re.findall(r'("""(.|\s)*?""")', content)
        for m in match:
            comment += m[0].strip().count('\n') + 1
        match = re.findall(r'(\'\'\'(.|\s)*?\'\'\')', content)
        for m in match:
            comment += m[0].strip().count('\n') + 1
    print '%s: whiatline: %d code: %d comment: %d' %(os.path.basename(path), whiteline, code, comment)

def count(path):
    if os.path.isfile(path):
        if path.endswith('.py'):
            _count(path)
    else:
        for root, dirs, files in os.walk(path):
            for file in files:
                if not file.endswith('.py'): continue
                _count(os.path.join(root, file))

count('e:\GitProjects\\show-me-the-code\\')