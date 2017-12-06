# PopClip-Builder

这是一个基于PopClip的插件生成工具，能通过代码生成PopClip的插件。

官方文档：https://github.com/pilotmoon/PopClip-Extensions



popclip.py中存放了Config.plist中所有项的类，如下：

- BeforeAfter(Enum)
- Requirement(Enum)
- OptionType(Enum)
- ActionType(Enum)
- KeysValue(Enum)
- Option
- Apps
- Action
- Config



使用popclip.py中的类先构建一个Config对象，接着使用build.py中的函数进行插件的打包，例如：



```python
# 构建Action对象
echoAction = Action('echo', type=ActionType.ShellScript('echo.sh', '/bin/sh'),
            image='icon.png', after=BeforeAfter.SHOW_RESULT)
# 构建Config对象，并将Action对象放入Config中
config = Config('BuilderTest', 'work.erio', [echoAction])
# 使用build函数创建项目，并且生成图标
build('NewProject', config, iconText='Echo')
```

