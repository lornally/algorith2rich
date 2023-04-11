# 方案一, AUTOMATIC1111 stable-diffusion-webui
> 参考: https://www.bilibili.com/video/BV1Pb411X79e/?spm_id_from=333.880.my_history.page.click&vd_source=ffeb47064b4ccc7342945681d65bf7ba

```sh
brew install cmake protobuf  wget

# 其他都不行, 3.8, 3.9, 3.11都不可以, 因为pytorch依赖这个版本
brew install python@3.10

git clone git@github.com:AUTOMATIC1111/stable-diffusion-webui.git

./webui.sh
```