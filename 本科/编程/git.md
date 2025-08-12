# git 学习

## 安装git

### Windows 系统

在 Windows 系统上安装 Git 有两种方法：

第一种是在 [Git 官网](https://git-scm.com/) 上直接下载 [Git 安装包](https://git-scm.com/downloads/win) 之后按照安装向导进行安装；

第二种方法是使用包管理器，

先下载一个包管理器，这里使用 [scoop](https://scoop.sh/) 作为示例，这里参考了 [CS 自学指南](https://csdiy.wiki/%E5%BF%85%E5%AD%A6%E5%B7%A5%E5%85%B7/Scoop/#scoop_1).

打开 power shell，执行以下命令：

```powershell
# 设置 PowerShell 执行策略
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# 下载安装脚本
irm get.scoop.sh -outfile 'install.ps1'
# 执行安装, --ScoopDir 参数指定 Scoop 安装路径
.\install.ps1 -ScoopDir 'C:\Scoop'
```

然后继续输入以下指令安装 Git：

```powershell
scoop install git
```

安装完成后可以在终端中输入以下指令查看 Git 版本：

```powershell
git -v
```
