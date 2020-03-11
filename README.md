# PyC2-demo

# 如要使用记得修改对应搭建c2服务器的ip

### 20200311 更新：

加入心跳包机制。以及上下线提醒

## demo

从入门到放弃的产物，学习过程中用python实现的一个单点c2基本功能。

采用http传输，server端采用Flask+redis队列，目前仅实现了单点连接命令执行功能。

命令的传输直接写的get方式明文传输，命令执行的结果是post方式base64编码传输。

若有精力的话后续应该会持续更新。

仅供学习

![](https://raw.githubusercontent.com/timwhitez/PyC2-demo/master/demo1.PNG)

![](https://raw.githubusercontent.com/timwhitez/PyC2-demo/master/frame.PNG)

## todo

~~-加入心跳包及上线提醒~~
- [ ] 用c++/Golang 重构client
- [ ] 加入多对多支持
- [ ] 流量加密/编码
- [ ] 加入argument spoofing
- [ ] 加入R3 Kill AntiVirus
- [ ] 整合上传等功能组件
