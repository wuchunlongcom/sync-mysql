# 前端：
# 1. 没有此状态文件时，对登陆用户就正常显示同步按钮。
# 2. 有此文件时，对登陆用户就显示一个 <Span> ，不是 button，写 “同步中，请等待””
# 3. 用户点击按钮后，在后台create一个文件，里面写0，表示同步中...
# 后端：
# 1. 加一条crontab，每分钟跑一次脚本
# 2. 判断：
# 2.1 如果文件存在并且内容是0  
# 2.2 删除文件
# 2.3 同步中... 
# 2.4 如果文件不存在 —> 空跑


# from django.http.response import HttpResponseRedirect  不支持切换！
# print('read_txt(STATEFILE):',read_txt(STATEFILE))  # 查看日记 /tmp/test.log

def work():
    
    import os
    from account.data.syncdb import syncdb
    from myAPI.fileAPI import read_txt
    from django.conf import settings
    # from .models import Student
    
    STATEFILE = os.path.join(settings.BASE_DIR, 'account','data', 'syncdbstatus.txt') # 状态文件
    # 如果文件存在并且内容是0          
    if os.path.isfile(STATEFILE) and read_txt(STATEFILE) == '0':                            
        os.remove(STATEFILE) 
        syncdb() 
