## 获取binance的api
### 参考：https://binance.zendesk.com/hc/zh-cn/articles/360002502072-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BAAPI
### 把api_key和secret_key放置在api.ini中，方便后续调用

## 安装binance官网API文档上介绍的第三方python sdk, Binance_Futures_python包
### 参考：https://binance-docs.github.io/apidocs/futures/cn/#ed913b7357
### 将python sdk拷贝到project下：git clone https://github.com/Binance-docs/Binance_Futures_python.git
### 切换到Binance_Futures_python目录下安装sdk：python setup.py install
### 遇到requests.exceptions.ConnectionError，不确定是网络接口失效没有维护，还是需要科学上网，debug预计比较费时，暂时绕过。

## 安装github上star比较多的python-binance包
### 同样遇到requests.exceptions.ConnectTimeout，进一步怀疑是binance的API连接需要科学上网

## 在阿里云香港linux服务器上测试是否科学上网问题
### 激活conda的虚拟python3环境：source activate py37
### 用git命令下载python-binance包源代码到linux服务器：git clone https://github.com/sammchardy/python-binance.git
### 切换到python-binance包源代码目录下，安装python-binance包：python setup.py install
### 运行测试代码，遇到'no module named backports'错误，安装backports包
### 运行测试代码，遇到'no module named backports.zoneinfo'错误，网上搜索问题感觉不好定位原因，放弃python-binance包尝试
### git clone Binance_Futures_python包，安装该包后，测试能否跑通，证明可以跑通！！！
### 以上尝试证明Binance_Futures_python包没有问题，但是需要在科学上网环境下运行，由于本地电脑windows环境无科学上网配置，需要把代码放在可以科学上网的环境下运行

## 用Binance_Futures_python包，在外网环境下获取币种数据和K线数据，并保存在本地
### sdk接口中的binance_f用于获取永续掉期合约，binance_d用于获取期货合约，选择获取永续掉期合约
### 发现示例中只给出打印数据的例子，数据保存本地的话需要自己实现下
### 把获取k线数据函数返回的object类对象用json解析为dict，然后转换成pandas的dataframe格式，保存为csv文件