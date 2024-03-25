
---

# iOSRealRun-cli

## 背景
原 [iOSFakeRun](https://github.com/Mythologyli/iOSFakeRun) 只能在Windows上使用，每圈的路径是固定的。对于许多iOS/iPadOS 16及以上的设备，无法方便地打开开发者模式。因此，本项目应运而生。

## 功能
- **已实现**
  - [x] 方便打开开发者模式，无需第三方软件
  - [x] 使用与 [iOSFakeRun](https://github.com/Mythologyli/iOSFakeRun) 相同的路径格式（请只画一圈）
  - [x] 自定义配速
  - [x] 实现一种随机方式，使每一圈略有不同
  - [x] 支持Windows和MacOS
  - [x] 每次跑完路径后以随机速度再跑一次
- **暂未实现**
  - [ ] 另一种随机方式
- **无法实现**
  - [ ] 步数模拟

## 原理
不作解释，懂的人自然懂。

## 要求
- 操作系统为 `Windows` 或 `MacOS`
- Windows 需要安装 iTunes
- 已安装 `Python3` 和 `pip3`
- **重要提示**: 只能连接一台 iPhone 或 iPad 到电脑，否则可能出现问题

## 使用方法
1. 克隆本项目到本地并进入项目目录
2. 安装依赖（建议使用虚拟环境）  
    ```shell
    pip3 install -r requirements.txt
    ```
    如果 `pip3` 安装失败，请尝试使用 `pip`  
    如果遇到版本问题，请尝试更换软件源
3. 对于iOS 17以下的设备，需要挂载开发者镜像。
    - 打开 [DeveloperDiskImage](https://github.com/mspvirajpatel/Xcode_Developer_Disk_Images/releases) 仓库  
    - 下载对应自己的 iOS 版本的 `DeveloperDiskImage.dmg` 和 `DeveloperDiskImage.dmg.signature` 文件
    - 将文件放入相应的目录（如图所示）

    <img src="https://s2.loli.net/2024/03/25/uUgEaDdc7SA6h9J.png">  
4. 获取跑步路径，格式需与 [iOSFakeRun](https://github.com/Mythologyli/iOSFakeRun) 相同，项目预置了紫金港操场和海宁操场路径（在 `config.yaml` 中修改），建议自行绘制路径
5. 打开 `route.txt` 文件，粘贴路径坐标，保存
6. 在 `config.yaml` 中设置速度参数 `v`，例如，3.3对应大约5-5.5分钟每公里的配速
7. 连接设备到电脑，解锁并信任
8. Windows **以管理员身份** 运行终端（cmd 或 PowerShell），在项目目录执行以下命令  
    ```shell
    python main.py
    ```
    MacOS 使用终端，在项目目录执行以下命令  
    ```shell
    sudo python3 main.py
    ```
9. 按照提示操作，若提示未连接设备，请确保iTunes已安装并重新运行程序，确保设备连接并信任
10. 结束时务必使用 `Ctrl + C` 终止程序，否则定位信息可能无法恢复
11. 若定位未能恢复，重启手机即可解决

## 免责声明
本项目仅供Python和C学习交流使用，对软件用途不做任何说明或暗示。使用本软件造成的后果作者概不负责。

## 致谢
- [iOSFakeRun](https://github.com/Mythologyli/iOSFakeRun)

## 许可证
- 提交 [4d932f](https://github.com/iOSRealRun/iOSRealRun-cli/commit/4d932f7b1a8b83a5b3baca8a19d45f8949fd1fe2) 将许可证由 MIT 改为 [MPL-2.0](https://github.com/iOSRealRun/iOSRealRun-cli/blob/main/LICENSE)，之后采用 [MPL-2.0](https://github.com/iOSRealRun/iOSRealRun-cli/blob/main/LICENSE) 分发（除libimobiledevice文件夹外的部分）

--- 