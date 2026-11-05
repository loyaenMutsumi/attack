[README.md](https://github.com/user-attachments/files/34407337/README.md)
# QQ 邮箱每日早安邮件机器人

利用 GitHub Actions 每天**北京时间早上 8:00** 自动给朋友发送 QQ 邮件。

## 文件说明

- `.github/workflows/send-mail.yml` — GitHub Actions 定时任务配置
- `send_mail.py` — 发邮件的 Python 脚本

## 部署步骤

### 第 1 步：获取 QQ 邮箱 SMTP 授权码

1. 登录 [mail.qq.com](https://mail.qq.com) → **设置** → **账号**（或"账户"）
2. 找到 **POP3/IMAP/SMTP 服务**，开启 **IMAP/SMTP 服务**（需短信验证）
3. 开启后会生成一个 **16 位授权码**（形如 `abcdwxyzabcdwxyz`），保存好——注意这不是 QQ 密码！

### 第 2 步：创建 GitHub 私有仓库

1. 登录 GitHub，点右上角 **+** → **New repository**
2. 仓库名随意（如 `daily-mail`），勾选 **Private**（保护隐私）
3. 创建后，把本项目 `qq-mail-bot` 文件夹里的内容全部上传到仓库根目录（保持 `.github/workflows/send-mail.yml` 的目录结构）

上传方式（本地有 git 时）：

```bash
cd qq-mail-bot
git init
git add .
git commit -m "init daily mail bot"
git branch -M main
git remote add origin https://github.com/你的用户名/daily-mail.git
git push -u origin main
```

### 第 3 步：配置 Secrets 和 Variables

进入仓库页面 → **Settings** → **Secrets and variables** → **Actions**：

**Secrets（点 New repository secret，共 3 个）：**

| Name | 值 |
|---|---|
| `QQ_EMAIL` | 你的QQ邮箱，如 `123456789@qq.com` |
| `QQ_AUTH_CODE` | 第 1 步获取的 16 位授权码 |
| `TO_EMAIL` | 朋友的邮箱地址 |

**Variables（点 Variables 标签页 → New repository variable，共 2 个）：**

| Name | 值（示例） |
|---|---|
| `MAIL_SUBJECT` | `早安 ☀` |
| `MAIL_CONTENT` | `早上好！新的一天也要元气满满哦！` |

> 固定文字就写在这里，随时可以改，不用动代码。

### 第 4 步：测试

仓库页面 → **Actions** → 选 **Send QQ Mail Every Morning** → **Run workflow** → 点击运行。

成功的话朋友马上会收到一封邮件。

## 定时说明

- 工作流里 `cron: '0 0 * * *'` 是 UTC 时间 0:00 = **北京时间早上 8:00**
- GitHub Actions 定时任务**可能延迟几分钟到十几分钟**，属于正常现象
- 免费公共仓库的 Actions 每月 2000 分钟额度，每天跑一次完全够用
- ⚠️ 仓库连续 60 天无活动会被 GitHub 自动暂停定时任务，偶尔 push 一次或手动 Run 一下即可续期
