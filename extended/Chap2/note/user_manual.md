天气查询，  
输入城市名，返回该城市最新的天气数据；  
输入指令，获取帮助信息（一般使用 h 或 help）；  
输入指令，获取历史查询信息（一般使用 history）；  
  **history指令接受两个可选参数，**   
  *1.history 获取当天历史查询信息  
  2.history [城市名]  获取该城市历史查询信息  
  3.history [日期(YYY-MM-DD)]  获取该日期历史查询信息  
  4.history [城市名] [日期(YYY-MM-DD)]  获取指定城市指定日期历史查询信息  
  注：第一种情况相当于history [当天日期(YYY-MM-DD)]，第四种情况，当两个可选参数都输入时，第一个参数必需是城市名，第二个参数必需是日期。*  

输入指令，退出程序的交互（一般使用 quit 或 exit）；  
在退出程序之前，打印查询过的所有城市。  

使用方法：  
* 安装第三方模块
  ```
  pip install python-dateutil  
  pip install simplejson  
  pip install tinydb  
  ```
* 进入文件所在目录，执行``` python weather.py```语句运行程序，按提示输入相应命令。