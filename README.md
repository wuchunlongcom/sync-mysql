### 更新数据库数据 2020.02.25

### 功能
```
工程使用db.sqlite3数据库，连接mysql从mysql数据库获取数据，再写入db.sqlite3数据库

1、admin 添加一个按钮，按更新按钮，从mysql数据库获取数据，再写入db.sqlite3数据库;
2、前台实现，按更新按钮，从mysql数据库获取数据，再写入db.sqlite3数据库;

```

### 操作步骤  
```
1、./start_mysql.sh  用脚本初始化studb数据库（mysql）;
2、python mysite/initmysql.py  给studb数据库(mysql)的account_student表，初始化1000条记录；   
3、./start_mysql.sh 数据初始化，从studba数据库account_student表中获取数据；此时list db.sqlite3中Student表中是没有数据的;
4、./start.sh -i ;
5、前台实现更新数据库;
6、按更新按钮, 连接mysql 数据库，更新实例中的db.sqlite3数据库数据，list中获得数据;

```

### 使用到的技术
```
1、连接studb(mysql数据库)
2、脚本操作mysql   https://www.cnblogs.com/study-learning/p/10800820.html
3、程序运行过程显示动画
```