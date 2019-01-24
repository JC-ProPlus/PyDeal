# -*- coding: utf-8 -*-
import sys

langList=['1.C/C++','2.Java','3.Python','4.JavaScript','5.C#','6.Ruby']
print('你觉得哪种语言最好用？')
print(langList[0],langList[1],langList[2],langList[3],langList[4],langList[5])
rawBestLang = input('我选：')
bestLang = int(rawBestLang)
if bestLang==1:
    print('C/C++，是吗？')
elif bestLang==2:
    print('Java，是吗？')
elif bestLang==3:
    print('Python，是吗？')
elif bestLang==4:
    print('JavaScript，是吗？')
elif bestLang==5:
    print('C#，是吗？')
elif bestLang==6:
    print('Ruby，是吗？')
elif bestLang==114514:
    print('恭喜，进入上帝模式！')
else:
    print('数据错误！')
if bestLang==114514:
    print('需要更改些什么吗？')
    command = input('[PHP@PHP / ]#')
    for bestLang in range(9999999999999999999999999999):
        print('PHP是世界上最好的语言。')
else:
    print('知道吗？我喜欢PHP。')
    input('按任意键继续...')
    try:
        while 'JustPHP':
            sys.stdout.write('PHP是世界上最好的语言。\n')
    except KeyboardInterrupt as JustPHP:
        sys.exit(JustPHP)