# ! 1. 主函数
import torch
import torch.nn as nn
if 'fnn' in dir():
  del fnn
def fnn():
  # 生成一个module, 它是torch的基础神经网络对象
  mnn=nn.Module()
  # 定义基础参数
  mnn.model=nn.Sequential(
      nn.Linear(784,200), # 线性全连接从输入到中间 ax+b, 这里a和b都是学习会调整的参数, 此处已经比我们numpy的实现强大了一丢丢

      nn.LeakyReLU(0.02),   # ! 隐藏层使用了relu
      nn.LayerNorm(200), # ! 这里标准化了数据
      nn.Linear(200,10), # 线性全连接从中间到输出
      nn.Sigmoid(), # fixme 因为BCE只能0-1, relu输出不止, 所以最终输出层不能用relu

      # nn.LeakyReLU(0.02), # fixme BCEloss不能配合leakyrelu
  )

  # fixme BCEloss不能配合leakyrelu
  mnn.loss_function=nn.BCELoss()


  # ! 注意参数数量变了, 他的学习率都不同, 所以不需要设置
  mnn.optimiser=torch.optim.Adam(mnn.parameters())


  # 这里是验证函数
  def forward(inputs):
    # 非常简便, 直接调用官方提供的model函数就能实现验证功能
    return mnn.model(inputs)
  fnn.forward=forward

  # 定义train之前, 需要定义几个属性
  counter=0 # 可视化训练需要的计数器
  progress=[] # 可视化训练需要的过程中的参数, 存储参数来自于下面定义的损失函数

  # 训练函数
  def train(inp,targ):
    # 第一步, 训练拿到模型结果
    outp=forward(inp)
    # 计算损失值, 定义loss, 这里使用了之前定义的loss_function
    loss=mnn.loss_function(outp, targ)
    # ! 这三行是精华
    mnn.optimiser.zero_grad() # 将计算图中的梯度归零, 避免每次计算叠加效果, 换句话说, 很多机器学习算法会需要叠加每一轮的梯度
    loss.backward() # loss计算了梯度
    mnn.optimiser.step() # 更新网络的可学习参数
    # 此时代码已经完成了我们在numpy方式中做的所有功能
    # 下面的内容是为了可视化训练, 在训练中, 我们能够监控训练情况
    counter +=1
    if(counter%10==0):
      # 这一行item()函数是为了取值方便, progress是之前定义的数组
      progress.append(loss.item())
      if(counter%10000==0):
        print('counter', counter)
      pass
  fnn.train=train
  # 绘图函数, 图示训练过程
  def plot_progress():
    # 这里用了pandas, 定义了数据来源, 以及列的表头使用哪一行
    df=pandas.DataFrame(rogress, columns=['lose'])
    # 这里调整视图的各种格式风格参数, 大伙先用吧, 如果想要了解pandas, 这个本身也需要一次分享, 在此之前, 只要知道pandas是干翻了R的库, 就可以了
    df.plot(ylim=(0,1.0), figsize=(16,8), alpha=0.1, marker='.',grid=True, yticks=(0,0.25,0.5))
  fnn.plot_progress=plot_progress


# ! 2. 引入drive
from google.colab import drive
drive.mount('./mount')

# ! 3. 定义加载数据的方法
import pandas
from torch.utils.data import Dataset
import matplotlib.pyplot as plt
if 'mdata' in dir()::
  del mdata
def mdata(csv_file):
  df=pandas.read_csv(csv_file, header=None)

  def ploti(index):
    arr=df.iloc[index, 1:].values.reshape(28,28)
    plt.title('label ='+str(df.iloc[index,0]))
    plt.imshow(arr, cmap='Greens',interpolation='hamming')
  mdata.ploti=ploti
  #mdata的长度
  mdata.len=len(df)

  # 定义一个得到某个元素的方法,
  def item(i):
      label=df.iloc[i, 0]
      target=torch.zeros((10))
      target[label]=1.0
      img=torch.FloatTensor(df.iloc[i, 1:].values)/255.0
      return label, img, target
  mdata.item=item

# ! 4. 载入训练数据
mdata('mount/My Drive/Colab Notebooks/mnist_train.csv')

# ! 5. 训练模型
%%time
fnn()
round=3
for i in range(round):
  print ('训练轮次:', i+1, '/总轮次',round)
  for i in range(mdata.len):
    (label, image_data_tensor, target_tensor)=mdata.item(i)
    fnn.train(image_data_tensor, target_tensor)

# ! 6. 加载测试数据
mdata('mount/My Drive/Colab Notebooks/mnist_test.csv')

# ! 7. 测试模型
count=0.0
for (label, image, target) in mdata.ite:
  output=fnn.forward(image).detach().numpy()
  if label==output.argmax() :
    count+=1
print(count, mdata.len, count/mdata.len)