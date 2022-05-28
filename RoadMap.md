# 文本挖掘的学习路线

## 1 编程
**掌握编程技术是文本挖掘的基础。在正式学习文本挖掘的其他知识之前，应该确保自己有基本的Python编程能力。**

### 1.1 Python基础

* **内容：** Python有两个大版本，请选择学习Python3，可参见廖雪峰的[Python教程](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000) 。
   
  **要求：** 学习到"常用第三方模块"即可，后面的部分凭兴趣学习。需将教程提到的每一行代码都亲手实验，掌握**如何运行Python** 、**python的特性** 和**面向对象编程** 。注意[Python的代码规范](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/) ，不要写的太丑。

  **时间：** 一周内完成。

### 1.2 重要的Python包

* **内容1：利用Python操纵字符串** ，可参见[教程1](https://www.jianshu.com/p/b758332c44bb) 、 [教程2](https://www.jiqizhixin.com/articles/2020-02-28-2)  、[教程3](https://www.runoob.com/python/python-strings.html) 。
   
  **要求：** 三个教程各有侧重，稍有交叉。需将教程提到的每一行代码都亲手实验。

  **时间：** 12小时内完成。

* **内容2：利用Python进行分词** ，可参见[教程](https://github.com/fxsjy/jieba) 。
   
  **要求：** 需将教程提到的每一行代码都亲手实验。掌握对程序中的变量进行分词、对程序外输入的句子进行分词、对文件中的句子进行分词、把分词结果保存到文件中等。

  **时间：** 12小时内完成。

* **内容3：利用Numpy进行矩阵操作** ，可参见[中文教程](https://blog.csdn.net/xiaoxiangzi222/article/details/53084336) 或者 [英文教程](https://docs.scipy.org/doc/numpy/user/quickstart.html) 。
   
  **要求：** 需将教程提到的每一行代码都亲手实验。

  **时间：** 2天内完成。

* **内容4：利用scikit-learn实现机器学习** ，可参见[中文教程](https://sklearn.apachecn.org/#/docs/master/51) 或者 [英文教程](https://scikit-learn.org/stable/tutorial/index.html) 。
   
  **要求：** **前置要求：掌握下面要求的机器学习基础** 。需将教程提到的每一行代码都亲手实验。

  **时间：** 2天内完成。

* **内容5：利用Pytorch实现深度学习** ，可参见[中文教程](https://www.w3cschool.cn/pytorch/pytorch-5ubt3bby.html) 或者 [英文教程](https://pytorch.org/tutorials/beginner/basics/intro.html) 。
   
  **要求：** **前置要求：掌握下面要求的深度学习基础** 。需将教程提到的每一行代码都亲手实验。

  **时间：** 2天内完成。

* 其他包等用到的时候再进行针对性的学习。

[comment]: <> (5. 学习利用pandas做数据的统计分析。直接跟着[野鸡教程]&#40;https://blog.csdn.net/Yan_Joy/article/details/78095115&#41; 或者[专业教程]&#40;http://pandas.pydata.org/pandas-docs/stable/tutorials.html&#41; 做。（练习时间不超过2天）。)

注：要学会百度/google找到自己感兴趣的内容。一些bug可以在[stackoverflow](https://stackoverflow.com/) 上找到。

## 2 快速入门机器学习和深度学习

**注：不要随意扩展阅读以及跳读，请按照规划认真阅读理解每一部分。如果有问题，请随时联系老师。**

**我在此处不建议新入门的同学直接钻入课程和书本中，不然容易陷入大量的细节中不能自拔。（不过仅仅是个人建议，一家之言。）**

### 2.1 机器学习基础
* 线性回归
  * 数学表示：y = f(x)与最小二乘法 [学习链接](https://zhuanlan.zhihu.com/p/72513104)
  * 一切的基础：梯度下降算法 [学习链接](https://www.cnblogs.com/byrans/p/4700202.html)

* 逻辑回归
  * sigmoid函数的意义：压缩任意实数到0-1 [学习链接](https://zhuanlan.zhihu.com/p/28408516)
  * 求解方法：梯度下降算法 [学习链接](https://zhuanlan.zhihu.com/p/44591359)

**注意：在更新参数时，线性回归和逻辑回归的思路一模一样。**

### 2.2 多层感知机（全连接，MLP）
* 了解前向传播和后向传播 [学习链接](https://zhuanlan.zhihu.com/p/23937778)

### 2.3 词嵌入（Word2vec）
* 了解如何用word2vec生成词嵌入 [学习链接](https://blog.csdn.net/qq_44015059/article/details/105601082)

### 2.4 卷积神经网络
* 什么是卷积神经网络 [学习链接](https://zhuanlan.zhihu.com/p/44464548) （看理论部分即可）
* 在文本中的应用 [学习链接](https://zhuanlan.zhihu.com/p/44614213) （选读）

### 2.5 循环神经网络
* 什么是循环神经网络 [中文学习链接](https://zhuanlan.zhihu.com/p/42717426) 或 [英文原版学习链接](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)
* 在文本中的应用 [学习链接](https://zhuanlan.zhihu.com/p/25928551) （选读）

### 2.6 注意力机制
* 什么是注意力机制 [学习链接](https://zhuanlan.zhihu.com/p/67909876) （看理论部分即可）
* 什么是自注意力机制 [学习链接](https://zhuanlan.zhihu.com/p/484524337)

### 2.7 Pytorch代码实践
* [NLP FROM SCRATCH: CLASSIFYING NAMES WITH A CHARACTER-LEVEL RNN](https://pytorch.org/tutorials/intermediate/char_rnn_classification_tutorial.html)
* [NLP FROM SCRATCH: GENERATING NAMES WITH A CHARACTER-LEVEL RNN](https://pytorch.org/tutorials/intermediate/char_rnn_generation_tutorial.html)
* [NLP FROM SCRATCH: TRANSLATION WITH A SEQUENCE TO SEQUENCE NETWORK AND ATTENTION](https://pytorch.org/tutorials/intermediate/seq2seq_translation_tutorial.html)
* [我们提供的文本挖掘入门代码](https://github.com/ECNU-Text-Computing/Text-Mining-Start)
* [我们提供的文本挖掘进阶代码](https://github.com/ECNU-Text-Computing/Text-Mining)

### 2.8 其他代码实践
* [复旦NLP实验室NLP上手教程](https://github.com/FudanNLP/nlp-beginner)

### 2.9 文本挖掘的主要方向
* 分类、匹配、序列标注、生成、阅读理解等

## 3 详细学习文本挖掘

**在你掌握了机器学习与深度学习最核心的思想之后，会发现有大量的细节还不是很清楚，这时候除了每次针对性的搜索和学习之外，最好跟着某门课或者某本书系统的重新学习一遍。**

### 3.1 课程
1. 基础：微积分、线性代数、概率论和统计学，**可以把当年的课本拿出来复习一遍**
   * 微积分：至少应该懂得如何求导
   * 线性代数：至少懂矩阵相乘、点乘、秩的概念、矩阵分解等
   * 概率论与统计：至少需要懂抽样和几种常见的分布

2. 进阶：机器学习
   * 入门课程：[吴恩达老师的Coursera课程](https://www.bilibili.com/video/BV164411b7dx)
   * 其他课程：林轩田老师的[机器学习基石](https://www.bilibili.com/video/av1624332) 和 [机器学习技法](https://www.bilibili.com/video/av12469267)
   * 其他理论和代码搭配教学的课程：华盛顿大学的[机器学习专项课程](https://www.bilibili.com/video/BV1LW411B7uB)
   * 文本相关的课程：翟成祥老师的[文本挖掘和分析](https://www.bilibili.com/video/BV1Ci4y1u7Qw)
   
3. 再进阶：深度学习
   * 吴恩达老师关于[deep learning的课程](https://www.bilibili.com/video/BV16r4y1Y7jv)
   * Manning老师关于自然语言处理的[CS224n](https://www.bilibili.com/video/av13383754)
   * 李宏毅老师的[深度学习课程](https://www.bilibili.com/video/BV1Wv411h7kN) 

### 3.2 书籍
* 周志华老师的西瓜书[《机器学习》](https://item.jd.com/11867803.html)
* 李航老师的小蓝书[《统计学习方法》](https://item.jd.com/12385906.html)
* 邱锡鹏老师的[《神经网络与深度学习》](https://nndl.github.io/)
* Manning老师检索相关的[《信息检索导论》](https://item.jd.com/12554083.html)
* 宗成庆老师NLP相关的[《统计自然语言处理》](https://item.jd.com/12646701.html)
* 最经典的[《Pattern Recognition and Machine Learning》](https://item.jd.com/63186422373.html)