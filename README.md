# NLP 词云生成器

该项目通过对电影对话文本进行NLP处理，包括分词、去除停用词、词性标注、命名实体识别和情感分析，生成词云。

## 前提条件

- Python 3.7 或更高版本
- 需要安装的Python库：
  - wordcloud
  - pillow
  - nltk
  - matplotlib
  - numpy
  - re（标准库）

## 安装

1. 克隆该仓库或下载脚本文件。

2. 安装所需的Python库：
   ```bash
   pip install wordcloud pillow nltk matplotlib numpy
   ```

3. 下载必要的NLTK数据：
   ```python
   import nltk
   nltk.download('stopwords')
   nltk.download('punkt')
   nltk.download('averaged_perceptron_tagger')
   nltk.download('maxent_ne_chunker')
   nltk.download('words')
   nltk.download('vader_lexicon')
   ```

## 文件说明

- `nlp_wordcloud.py`: 主要的Python脚本，执行NLP处理并生成词云。
- `assets/`: 包含用作词云遮罩的图片文件的目录。
  - `butterfly.webp`
  - `car.webp`
  - `dog.webp`
  - `tower.jpg`
  - `tree.jpg`
- `movie_lines.txt`: 包含电影对话的文本文件，格式如下：
  ```
  L1045 +++$+++ u0 +++$+++ m0 +++$+++ BIANCA +++$+++ They do not!
  L1044 +++$+++ u2 +++$+++ m0 +++$+++ CAMERON +++$+++ They do to!
  L985 +++$+++ u0 +++$+++ m0 +++$+++ BIANCA +++$+++ I hope so.
  L984 +++$+++ u2 +++$+++ m0 +++$+++ CAMERON +++$+++ She okay?
  L925 +++$+++ u0 +++$+++ m0 +++$+++ BIANCA +++$+++ Let's go.
  ```

## 使用方法

1. 确保所有必需的文件（`nlp_wordcloud.py`, `movie_lines.txt` 以及 `assets` 目录中的图片）在同一目录下。

2. 运行脚本：
   ```bash
   python nlp_wordcloud.py
   ```

3. 脚本将执行以下步骤：
   - **读取并清理 `movie_lines.txt` 文件中的电影台词**：提取对话文本并删除特殊字符和数字。
   - **对清理后的文本进行分词**：将文本分割成单个单词。
   - **去除停用词**：过滤掉常见的停用词（例如“the”，“is”）。
   - **使用不同的图片遮罩生成词云**：创建文本数据的可视化表示。
   - **词性标注**：标识每个单词的词性（例如，名词、动词）。
   - **命名实体识别**：检测并分类命名实体（如人名、组织名、地名）。
   - **情感分析**：分析文本的整体情感（正面、负面、中性）。

4. 词云将被显示，NLP分析结果将打印到控制台。

## 详细的NLP步骤

### 文本清理
`clean_text` 函数移除文本中的特殊字符和数字，以确保仅处理有意义的单词。

### 分词
使用NLTK的 `word_tokenize` 将文本分割成单个单词（词元）。

### 去除停用词
使用NLTK预定义的停用词列表去除常见的停用词，从而集中处理更重要的单词。

### 词性标注
使用NLTK的 `pos_tag` 对词元进行词性标注，标识其语法部分（例如名词、动词）。

### 命名实体识别
使用NLTK的 `ne_chunk` 识别并分类命名实体（例如人名、组织名）。

### 情感分析
使用NLTK的VADER（Valence Aware Dictionary and sEntiment Reasoner）进行情感分析，提供正面、负面、中性和综合情感评分。

## 示例输出

脚本将生成并显示如下词云：

- 蝴蝶形状的词云
- 汽车形状的词云
- 狗形状的词云
- 埃菲尔铁塔形状的词云
- 树形状的词云

此外，还会将词性标注、命名实体识别结果和情感分析分数打印到控制台。
