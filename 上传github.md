# 项目上传到GitHub详细步骤

为了将中医咨询健康网站项目上传到GitHub，需要先安装git并完成相关配置。以下是详细步骤：

## 1. 安装Git
1. 访问 [Git官网](https://git-scm.com/downloads) 下载适合您操作系统的Git安装包
2. 按照安装向导完成Git安装
3. 安装完成后，打开命令提示符或终端，运行 `git --version` 验证安装成功

## 2. 配置Git
1. 设置用户名：`git config --global user.name "您的GitHub用户名"`
2. 设置邮箱：`git config --global user.email "您的GitHub邮箱"`

## 3. 在GitHub上创建仓库
1. 登录GitHub账户
2. 点击右上角的"+"按钮，选择"New repository"
3. 仓库名称填写为"bapsweb"
4. 选择公开(Public)仓库
5. 点击"Create repository"按钮

## 4. 初始化本地仓库并上传代码
1. 在项目目录中打开命令提示符或终端
2. 初始化git仓库：`git init`
3. 添加所有文件：`git add .`
4. 提交初始 commit：`git commit -m "Initial commit"`
5. 关联远程仓库：`git remote add origin https://github.com/您的GitHub用户名/bapsweb.git`
6. 推送到GitHub：`git push -u origin master`

## 5. 验证上传结果
1. 打开浏览器，访问 `https://github.com/您的GitHub用户名/bapsweb`
2. 确认项目文件已成功上传

## 6. 部署到GitHub Pages（可选）
如果您希望通过GitHub Pages使网站可访问：
1. 在GitHub仓库页面，点击"Settings"
2. 选择"Pages"
3. 在"Source"选项中，选择分支（通常为main或master）
4. 点击"Save"
5. 等待几分钟后，网站将可通过 `https://您的GitHub用户名.github.io/bapsweb` 访问

## 注意事项
- GitHub Pages仅支持静态网站，而我们的项目是基于Flask的动态网站。要完全运行此项目，用户需要在本地或其他服务器上安装Flask环境并运行应用。
- 如果在执行过程中遇到任何问题，请检查网络连接和Git配置是否正确。
