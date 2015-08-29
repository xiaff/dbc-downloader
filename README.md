# 豆瓣用户读书短评下载工具
这个工具可以下载用一位豆瓣读书用户的ID，批量下载其所有的读书短评，并导出为Markdown格式文件。

### 运行方法
1. 如果你想直接运行，请点击[这里](https://github.com/xiaff/dbc-downloader/raw/master/dbc-downloader.zip)下载工具，在解压后打开**dbc-downloader.exe**运行。
2. 如果你在计算机中安装了**Python 2.7**以及**codeces**、**BeautifulSoup** 模块，可以直接运行**DoubanUserBookCommentDownloader.py**.

### 设置代理
可以选择是否使用代理。  
如果需要在使用时设置HTTP代理，请确保代理可用并使用以下格式：**IP:PORT**。例如：`127.0.0.1:80`

### 用户id
首先访问用户的豆瓣主页，在地址栏看到的那一串数字或英文，就是用户的id。  
例如某用户的读书主页网址为：`http://book.douban.com/people/1000001/`,该用户的id则为`1000001`。

### 输出格式
用户的读书短评最终会以Markdown格式输出，该文件的扩展名为**.md**。  
如果你不了解Markdown，你可以使用markdown编辑器将该文件转换为pdf或html文件。

### 其他
为了防止由于访问过于频繁而使IP被豆瓣频闭，在代码的循环中使用了`time.sleep(5)`，每访问一个
网页等待5秒。如果你愿意的话，可以修改这个数值。
