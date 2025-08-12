# git 学习

## git 的安装和简单的配置

### 安装 Git

#### Windows 系统

在 Windows 系统上安装 Git 有两种方法：

1. 在 [Git 官网](https://git-scm.com/) 上直接下载 [Git 安装包](https://git-scm.com/downloads/win) 之后按照安装向导进行安装；

2. 使用包管理器，

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
   coop install git
   ```

安装完成后可以在终端中输入以下指令查看 Git 版本：

```powershell
git -v
```

#### 在 macOS 上安装 Git

在 macOS 上安装 Git 有两种方法：

1. 使用 [Homebrew](https://brew.sh/) 包管理器，打开终端，输入以下命令：

   ```bash
   brew install git
   ```

2. 使用 XCode， 内置 了 Git 工具
   运行 XCode，选择菜单 "Xcode" -> "Preferences" -> "Downloads"，然后选择一个 Command Line Tools 版本，系统会提示你安装命令行工具，点击 "Instal" 安装即可.

---

使用包管理器安装 Git 是最简单的方式，推荐使用这种方式.

同时使用包管理器更新 Git 也非常方便.

- `scoop update git` (Windows)
- `brew upgrade git` (macOS)

### 配置 Git

安装完成之后对 Git 进行一些基本的配置

在命令行中输入

```powershell
git config --global user.name "Your Name"
git config --global user.email "email@example.com"
```

其中 `Your Name` 替换为你的名字，`email@example.com` 替换为你的邮箱地址.

`--global` 参数表明这台机器上的所有仓库都会使用这个配置，如果你想为某个特定的仓库设置不同的名字和邮箱，可以进入该仓库目录，去掉 `--global` 参数，重新执行上述命令即可.

配置完之后可以使用以下命令查看配置信息：

```bash
git config -l
```

## 创建版本库

版本库也叫做仓库(repository)，是用于存储文件的地方，里面每个文件的变动 Git 都能记录.

`cd` 到你**需要创建版本库的目录下**，输入以下命令：

```bash
git init
```

这会在当前目录下创建一个名为 `.git` 的隐藏目录，里面存储了 Git 需要的所有信息.

若此时使用 `ls` 命令查看当前的目录,看不到任何新建的文件夹，因为 `.git` 是一个隐藏目录.

### 向版本库中添加文件

首先创建一个 `Readme.md` 文件,内容为

```markdown
# Git 学习

Git is a version control system.

Git is free software.
```

这个文件一定要在刚才创建的版本库的目录或子目录下

1. 在终端输入

   ```bash
   git add Readme.md
   ```

   这里输入的是路径而不是文件名，可以选择相对路径或者绝对路径.`git add` 命令会指示这些文件是需要装车的货物.

   如果没有输出任何内容，说明添加成功了.

2. 提交这些文件到版本库中，输入以下命令：

   ```bash
   git commit -m "Add Readme.md"
   ```

   `-m` 参数后面跟的是提交信息，描述了这次提交的内容,有助于其他人或者未来的自己理解这次提交的目的.

   一些工具可以使用 ai 生成提交信息,如 Github Desktop,这个也是十分好用的 Git 的图形化客户端.
