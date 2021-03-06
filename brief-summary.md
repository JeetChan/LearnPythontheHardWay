整个练习过程并没有遇到多大问题。由环境搭建到GitHub的使用，都较为顺利。见发表于简书的小结,[笨办法学Python](http://www.jianshu.com/p/7ef2819a896e)。

在这里主要回顾一下练习中解决问题的过程。以习题26为例，‘习题 26: 恭喜你，现在可以考试了！’这一练习是用时最多的，其他的练习都能很快完成。这一练习虽然用时较多，但主要还是语法上的错误，调试时只要根据错误提示信息修改便能逐一解决。[《Think Python 2ed》](http://greenteapress.com/thinkpython2/html/index.html)第二章‘调试’部分对程序错误有如下描述：
> 程序中可能会出现下面三种错误：语法错误（syntax error）、运行时错误(runtime error)和语义错误(semantic error)。我们如果能够分辨出三者区别，有助于快速追踪这些错误。

> 如果你的程序中存在一个语法错误，Python会显示一条错误信息，然后退出运行。你无法顺利运行程序。

所以语法错误问题是比较容易解决的。运行Python程序文件，查看Python错误信息，在这里我们看到‘File "exercise26.py", line 10’，用一个带行号的编辑器打开错误文件，在第10行发现‘print_first_word’方法是少了一个冒号，修正后再次运行错误就能解决了。见下图：

![](https://github.com/JeetChan/LearnPythontheHardWay/blob/master/image/debug.png)

随着我们不断深入学习，犯的语法错误会越来越少，这个时候我们会遇到运行时错误和语义错误。当苦思冥想也无法解决问题时我们需要善于提问，运用搜索帮助解决问题。



## 参考

[Rubber duck debugging](https://en.wikipedia.org/wiki/Rubber_duck_debugging)

[Stack Overflow](https://stackoverflow.com/)

[提问的智慧](https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way/blob/master/README-zh_CN.md)

## CHANGELOG

* 170731创建