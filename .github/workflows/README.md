# GitHub Actions 配置说明

## 设置 CDS API 密钥

要使用此工作流，你需要在 GitHub 仓库中配置 CDS (Climate Data Store) API 密钥：

### 1. 获取 CDS API 密钥

1. 访问 [CDS 官网](https://cds.climate.copernicus.eu/)
2. 注册并登录账户
3. 进入你的个人资料页面
4. 复制你的 API Key（格式为：`UID:API_KEY`）

### 2. 在 GitHub 仓库中添加 Secret

1. 进入你的 GitHub 仓库
2. 点击 `Settings` (设置)
3. 在左侧菜单中选择 `Secrets and variables` > `Actions`
4. 点击 `New repository secret`
5. 名称填写：`CDS_API_KEY`
6. 值填写：你从 CDS 网站获取的完整 API Key（格式：`UID:YOUR_API_KEY`）
7. 点击 `Add secret`

## 工作流触发方式

此工作流支持以下三种触发方式：

1. **手动触发**：在 GitHub 仓库的 Actions 标签页中手动运行
2. **定时触发**：每天 UTC 时间 0:00 自动运行（可根据需要修改）
3. **代码推送触发**：当 `main.py` 或 `requirements.txt` 发生变化时自动运行

## 工作流功能

- ✅ 自动安装 Python 和依赖包
- ✅ 配置 CDS API 认证
- ✅ 运行风场可视化脚本
- ✅ 上传生成的数据和图像为工件（保留 30 天）
- ✅ （可选）自动提交结果到仓库

## 注意事项

- 确保你的 CDS 账户已激活并接受了许可协议
- CDS API 有请求限制，请合理设置运行频率
- 生成的数据会作为 GitHub Actions 工件保存 30 天
- 如需长期保存数据，建议启用自动提交功能或使用其他存储方案
