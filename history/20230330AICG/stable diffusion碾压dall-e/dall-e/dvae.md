DALL·E的目标是把文本token和图像token当成一个数据序列，通过Transformer进行自回归。由于图片的分辨率很大，如果把单个pixel当成一个token处理，会导致计算量过于庞大，于是DALL·E引入了一个dVAE模型来降低图片的分辨率







### DALL·E的整体流程

1. 第一个阶段，先训练一个dVAE把每张 256x256 的 RGB 图片压缩成 32x32 的图片token，每个位置有 8192 种可能的取值(也就是说dVAE的encoder输出是维度为32x32x8192的logits，然后通过logits索引codebook的特征进行组合，codebook的embedding是可学习的)
2. 第二阶段，用BPE Encoder对文本进行编码，得到最多 256 个文本token，token 数不满256的话 padding 到256，然后将256个文本token与1024个图像token进行拼接，得到长度为1280的数据，最后将拼接的数据输入 Transformer 中进行自回归训练，典型的 teacher forcing 的方式，滑窗式样生成
3. 训练阶段，先训练dVAE模型，然后固定dVAE模型再来训练自回归的 Transformer
4. 推理阶段(图)，DALL·E 的第一个版本是 GPT-3 风格的 transformer 解码器，它可以根据文本输入生成很多图像code串，然后使用 dVAE 的decoder 可以生成很多可选的 256×256 大小的图像。
5. rerank 阶段(重排阶段)，通过输入不同的首个图像的 token 可生成很多各种类型的图片（设置max=512），需要根据 CLIP 来对得到的图文对进行重排

> dVAE、Transformer和CLIP三个模型都是不同阶段独立训练的

参考: https://zhuanlan.zhihu.com/p/604902250