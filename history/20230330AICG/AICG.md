### 学习难度
* 一次可以背多少个单词? 3, 8, 30, 300
* 哑巴英语的本质原因, 没办法兼容如此落后的语言体系, 谷爱凌中文说的比英文慢很多


### 技术列表
* NN, 本质是搜索, nn之前讲过
* GAN, 
* CNN, 
* transform, 
* bert, 
* diffusion, 
* embedding

### 思路
* GAN
* VAE 编码解码模型 Variational Autoencoder

### 降维
- embedding -> 降维, 我们知道高维空间都可以映射到低维(任意维度)空间
 - 新兴的词嵌入基于人工神经网络，而不是过去的n元语法模型和非监督式学习
- autoencoding, 自编码器

#### VAE 变分自编码
- 自编码, 降维, 编码->解码



### 机制
#### attention 注意力



### 复杂模型
#### transform 模型
- 输入: 
  - 字节对压缩(替换最频繁连续字节为未出现过的字节)
  - embedding -> 降维, 我们知道高维空间都可以映射到低维(任意维度)空间
    - 新兴的词嵌入基于人工神经网络，而不是过去的n元语法模型和非监督式学习

- Transformer模型使用VAE机制
- 每個編碼層和解碼層都使用了注意力機制。
- 對於每個輸入，注意力會權衡每個其他輸入的相關性，並從中提取資訊以產生輸出
- 每個解碼層都包含一個額外的注意力機制，它會在從編碼層提取資訊之前先從之前解碼器的輸出中提取資訊。
- 編碼層和解碼層都有一個前饋神經網路用於對輸出進行額外處理，並包含殘差連接和層歸一化步驟。
  - 前馈网络, 在之前控制论有讲过




### 名词列表


### dall-e2
DALL-E 2的工作是训练两个模型。第一个是Prior，接受文本标签并创建CLIP图像embedding。第二个是Decoder，其接受CLIP图像embedding并生成图像。模型训练完成之后，推理的流程如下：
输入的文本被转化为使用神经网络的CLIP文本embedding。
使用主成分分析（Principal Component Analysis）降低文本embedding的维度。
使用文本embedding创建图像embedding。
进入Decoder步骤后，扩散模型被用来将图像embedding转化为图像。
图像被从64×64放大到256×256，最后使用卷积神经网络放大到1024×1024。


#### stable diffusion

Stable Diffusion是一个文转图的模型，其使用了CLIP ViT-L/14文本编码器，能够通过文本提示调整模型。它在运行时将成像过程分离成“扩散 （diffusion）”的过程——从有噪声的情况开始，逐渐改善图像，直到完全没有噪声，逐步接近所提供的文本描述。