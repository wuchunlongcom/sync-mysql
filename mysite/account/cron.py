# 定时器  跑同步脚本
# 前端：
# 1. 没有此状态文件时，对登陆用户就正常显示同步按钮。
# 2. 有此文件时，对登陆用户就显示一个 <Span> ，不是 button，写 “同步中，请等待””
# 3. 用户点击按钮后，在后台create一个文件，里面写0，表示待同步
# 后端：
# 1. 加一条crontab，每分钟跑一次脚本
# 2. 脚本判断逻辑：
# 2.1 状态文件存在+内容是0  -- 待同步
#     状态文件内容改成1
#     跑同步脚本
# 2.2 状态文件存在+内容是1  -- 同步中
#     跑同步脚本
# 2.3 状态文件存在+内容是1  -- 同步完成
#     同步脚本跑完，删除状态文件    
# 2.4 状态文件不存在
#     空跑、啥也不做

# from django.http.response import HttpResponseRedirect  不支持切换！
# print('read_txt(STATEFILE):',read_txt(STATEFILE))  # 查看日记 /tmp/test.log

def work():
    
    import os
    from account.data.syncdb import syncdb
    from myAPI.fileAPI import read_txt
    from django.conf import settings
    from .models import Student
    from mysite.settings import STATEFILE  
            
    # 状态文件存在+内容是0
    if os.path.isfile(STATEFILE) and read_txt(STATEFILE) == '0':
       
        with open(STATEFILE,'w') as f:
            f.write('1')
		
		# 跑同步脚本
        syncdb()   

        #删除状态文件                    
        if os.path.isfile(STATEFILE):
            os.remove(STATEFILE) 
