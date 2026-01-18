@echo off
echo ========================================
echo    荔链直达 - 完整安装指南
echo ========================================

echo.
echo 本系统需要安装以下软件：
echo.
echo 1. Node.js (JavaScript运行环境)
echo 2. MongoDB (数据库)
echo 3. 项目依赖包
echo.
echo ========================================
echo.

:check_nodejs
echo 正在检查Node.js...
node --version >nul 2>&1
if errorlevel 1 (
    echo [X] Node.js未安装
    echo.
    echo 请按以下步骤安装Node.js：
    echo 1. 下载安装程序: https://nodejs.org/dist/v18.18.2/node-v18.18.2-x64.msi
    echo 2. 双击运行安装程序
    echo 3. 安装过程中务必勾选 "Add to PATH" 选项
    echo 4. 安装完成后，重启命令提示符
    echo.
    echo 按任意键打开下载页面...
    pause >nul
    start https://nodejs.org/dist/v18.18.2/node-v18.18.2-x64.msi
    echo.
    echo 下载完成后，请重新运行此脚本
    pause
    exit /b 1
) else (
    echo [] Node.js已安装
    node --version
    echo.
)

:check_mongodb
echo 正在检查MongoDB...
mongod --version >nul 2>&1
if errorlevel 1 (
    echo [X] MongoDB未安装
    echo.
    echo 请按以下步骤安装MongoDB：
    echo 1. 下载安装程序: https://www.mongodb.com/try/download/community
    echo 2. 选择 "Windows" -> "x64" -> "msi"
    echo 3. 双击运行安装程序
    echo 4. 选择 "Complete" 安装类型
    echo 5. 安装时勾选 "Install MongoDB as a Service"
    echo 6. 选择 "Run service as Network Service user"
    echo.
    echo 按任意键打开下载页面...
    pause >nul
    start https://www.mongodb.com/try/download/community
    echo.
    echo 安装完成后，请重新运行此脚本
    pause
    exit /b 1
) else (
    echo [] MongoDB已安装
    mongod --version
    echo.
)

echo ========================================
echo      环境检查通过，开始项目配置
echo ========================================

echo 正在安装后端依赖...
cd backend
if not exist node_modules (
    echo 安装中，请稍候...
    npm install
    if errorlevel 1 (
        echo [X] 后端依赖安装失败
        echo 请检查网络连接后重试
        pause
        exit /b 1
    )
) else (
    echo [] 后端依赖已存在
)

echo.
echo 正在安装前端依赖...
cd ../frontend
if not exist node_modules (
    echo 安装中，请稍候...
    npm install
    if errorlevel 1 (
        echo [X] 前端依赖安装失败
        echo 请检查网络连接后重试
        pause
        exit /b 1
    )
) else (
    echo [] 前端依赖已存在
)

echo.
echo 正在初始化演示数据...
cd ../backend
node initDemoData.js
if errorlevel 1 (
    echo [X] 演示数据初始化失败
    echo 但系统仍可运行
) else (
    echo [] 演示数据初始化成功
)

echo.
echo ========================================
echo         [] 安装完成！
echo ========================================
echo.
echo 现在可以运行以下脚本启动系统：
echo.
echo 1. 双击 run_system.bat 启动服务
echo 2. 或手动运行:
echo    - 后端: cd backend ^&^& npm run dev
echo    - 前端: cd frontend ^&^& npm start
echo.
echo 系统启动后访问: http://localhost:3000
echo 演示产品ID: LC20240117001, LC20240117002
echo.
echo 感谢使用荔链直达系统！
echo.
pause
