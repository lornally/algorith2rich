## CLIP（Contrastive Language-Image Pre-Training）

这需要 AI 在海量「文本-图片」数据上学习图片和文本的匹配。图中绿色方块是「图片潜在空间」的 N 张图片，紫色方块是「文本潜在空间」的 N 句描述语。AI 会努力将对应的 I1 与 T1 （蓝色方块）匹配，而不是 I2 与 T3 （灰色方块）匹配。这个 AI 就是广泛被用在 AI 作画中的 **CLIP**（Contrastive Language-Image Pre-Training / 对比式语言-文字预训练）