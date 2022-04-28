# 目标生成1010
import torch
import torch.nn as nn


def gan():
 # todo 1. 验证网络verify
 def verify():
  vn=nn.Module()
  vn.model=nn.Sequential(
   nn.Linear(4,200),
   nn.LeakyReLU(0.02),
   nn.LayerNorm(200),
   nn.Linear(200,2),
   nn.Sigmoid(),
  )
  vn.loss_function=nn.BCELoss()
  vn.optimiser=torch.optim.Adam(vn.parameters())

  def forward(inputs):
   return vn.model(inputs)
  verify.forward=forward

  def train(inp,tar):
   outp=forward(inp)
   loss=vn.loss_function(outp,tar)
   vn.optimiser.zero_grad()
   loss.backward()
   vn.optimiser.step()
  verify.train=train



 # todo 2. 生成网络 adver
 def adver():
  an=nn.Module()
  an.model=nn.Sequential(
   nn.Linear(4,200),
   nn.LeakyReLU(0.02),
   nn.LayerNorm(200),
   nn.Linear(200,2),
   nn.Sigmoid(),
  )
  an.loss_function=nn.BCELoss()
  an.optimiser=torch.optim.Adam(an.parameters())

  def forward(inputs):
   return an.model(inputs)
  adver.forward=forward

  def train(inp,tar):
   outp=forward(inp)
   loss=an.loss_function(outp,tar)
   an.optimiser.zero_grad()
   loss.backward()
   an.optimiser.step()
  adver.train=train

 # todo 3. 验证生成网络
 def forward(inputs):
  return adver.forward(inputs)

 # todo 4. 训练生成网络
 def train(inputs):
  # todo 1. 训练verify
  # todo 2. adver生成
  # todo 3. adver生成去到verify, verify给反馈
  # todo 4. 根据verify反馈训练adver
