# PyC2-demo

从入门到放弃的产物，学习过程中用python实现的一个单点c2基本功能。

采用http传输，server端采用Flask+redis队列，目前仅实现了单点连接命令执行功能。

命令的传输直接写的get方式明文传输，命令执行的结果是post方式base64编码传输。

若有精力的话后续应该会持续更新。

仅供学习

![](https://github.com/timwhitez/PyC2-demo/blob/master/demo.PNG?raw=true)
