# nonebot_plugin_howtocook
_:tada::tada::tada:做饭指南:tada::tada::tada:_

## 使用方法
1、在插件目录执行指令 git clone https://github.com/Shinoakii/nonebot_plugin_howtocook.git<br>
2、去[程序员在家做饭方法指南](https://github.com/Anduin2017/HowToCook)处clone源码<br>
3、把clone得到的dishes文件夹放置于nonebot_plugin_howtocook目录下<br>
4、在bot.py处加载本插件 nonebot.load_plugin("nonebot_plugin_howtocook")<br>
5、指令：今天吃什么、今晚吃什么、夜宵吃什么、中午吃什么、晚上吃什么、午饭吃什么、晚饭吃什么、怎么做+菜名<br>

## 一些问题
需要修改nonebot-plugin-htmlrender插件目录下的date_source.py文件中read_file的方法
在aiofiles.open()的括号内加入参数 , encoding = 'utf-8' <br>
![image](https://user-images.githubusercontent.com/86348789/205248200-e4cae188-b4eb-4a08-aefd-9330503c9efa.png)

## 功能展示
![image](https://user-images.githubusercontent.com/86348789/205208952-4abba1ec-e317-46a9-b7d9-0fe36304dcdf.png)


 
## 特别感谢

- [NoneBot2](https://github.com/nonebot/nonebot2)：本插件实装的开发框架。
- [go-cqhttp](https://github.com/Mrs4s/go-cqhttp)：稳定完善的 CQHTTP 实现。
- [程序员在家做饭方法指南](https://github.com/Anduin2017/HowToCook)：做菜方法来源于此

## 插件依赖

- [nonebot-plugin-htmlrender](https://github.com/kexue-z/nonebot-plugin-htmlrender)

## 包依赖
- fuzzywuzzy  安装命令： pip install fuzzywuzzy -i https://pypi.tuna.tsinghua.edu.cn/simple/
- python-Levenshtein 安装命令： pip install python-Levenshtein -i https://pypi.tuna.tsinghua.edu.cn/simple/
