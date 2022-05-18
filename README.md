# Text Mining Start
这是学习文本挖掘编程的一个入门版本。

## 1. 怎么运行？

### 1.1 数据：

**我将提供一个datasets.zip文件，你将之放置在该项目的根目录下，然后解压即可。最终该项目的目录结构如文件tree.txt所示。**

### 1.2 数据预处理：
* **show_json_data**：查看源数据。

`python3 Data_Processor.py --phase show_json_data`

* **extract_abs_label**：从源数据中提取输入和输出。因为我用的是aapr这个数据集，所以此处是abs和label。对于不同的源数据，要自己写不同的数据处理方法。

`python3 Data_Processor.py --phase extract_abs_label`

* **save_abs_label**：将处理好的干净数据保存下来。

`python3 Data_Processor.py --phase save_abs_label`

* **split_data**：将干净数据按照某种比例分割开。

`python3 Data_Processor.py --phase split_data`

* **get_vocab**：为深度学习部分，生成一个字典。

`python3 Data_Processor.py --phase get_vocab`

**注意，如果你的系统中仅有python3，没有python2，那么你可能需要把`python3`替换为`python`。**

### 1.3 训练深度学习模型:

`python3 main.py --phase aapr.dl.mlp.norm`

`python3 main.py --phase aapr.dl.textcnn.norm`

`--phase` 后的 `aapr.dl.mlp.norm`为main.py中parser可以捕捉的参数，此时为深度学习的config文件名。 

### 1.4 训练深度学习模型:

`python3 main.py --phase aapr.ml.lr.tf`

`python3 main.py --phase aapr.ml.lr.tfidf`

`python3 main.py --phase aapr.ml.lr.lda`

`python3 main.py --phase aapr.ml.svm.tf`

`python3 main.py --phase aapr.ml.svm.tfidf`

`python3 main.py --phase aapr.ml.svm.lda`

`--phase` 后的 `aapr.ml.svm.tf`为main.py中parser可以捕捉的参数，此时为机器学习的config文件名。


## 2. To be continued...

风雨过后一定会有美好的天空

天晴之后总会有彩虹

战胜疫情一定有始有终

孤独尽头不一定惶恐

愿疫情早日退散。