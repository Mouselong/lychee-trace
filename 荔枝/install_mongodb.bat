@echo off
echo ========================================
echo    MongoDB 安装指南
echo ========================================

echo MongoDB是本系统的数据库组件
echo.
echo 安装步骤：
echo 1. 下载MongoDB Community Server
echo    下载地址: https://www.mongodb.com/try/download/community
echo    选择: Windows x64 MSI
echo.
echo 2. 运行安装程序
echo    - 选择 "Complete" 安装类型
echo    - 安装到默认路径
echo    - 勾选 "Install MongoDB as a Service"
echo    - 选择 "Run service as Network Service user"
echo.
echo 3. 验证安装
echo    运行: mongod --version
echo.
echo 4. 启动MongoDB服务
echo    - 服务名称: MongoDB
echo    - 或在命令行运行: net start MongoDB
echo.
echo 按任意键打开下载页面...
pause >nul

start https://www.mongodb.com/try/download/community

echo.
echo 下载完成后，请按照上述步骤安装MongoDB
echo 安装完成后，运行 check_installation.bat 检查环境
echo.
pause
