@echo off
echo ========================================
echo    荔链直达 - 区块链溯源系统启动脚本
echo ========================================

echo 正在检查Node.js...
node --version >nul 2>&1
if errorlevel 1 (
    echo 错误: 未检测到Node.js，请先安装Node.js 16+
    echo 下载地址: https://nodejs.org/
    pause
    exit /b 1
)

echo 正在检查MongoDB...
mongod --version >nul 2>&1
if errorlevel 1 (
    echo 警告: 未检测到MongoDB，请确保MongoDB服务正在运行
    echo 如未安装，请访问: https://www.mongodb.com/
    echo.
)

echo 正在安装后端依赖...
cd backend
if not exist node_modules (
    npm install
    if errorlevel 1 (
        echo 错误: 后端依赖安装失败
        pause
        exit /b 1
    )
)

echo 正在安装前端依赖...
cd ../frontend
if not exist node_modules (
    npm install
    if errorlevel 1 (
        echo 错误: 前端依赖安装失败
        pause
        exit /b 1
    )
)

echo 正在初始化演示数据...
cd ../backend
node initDemoData.js
if errorlevel 1 (
    echo 警告: 演示数据初始化失败，但系统仍可运行
)

echo.
echo ========================================
echo          系统启动中...
echo ========================================
echo.
echo 后端服务将在 http://localhost:3001 启动
echo 前端服务将在 http://localhost:3000 启动
echo.
echo 按任意键启动服务...
pause >nul

start "荔链直达-后端" cmd /k "cd backend && npm run dev"
timeout /t 3 /nobreak >nul
start "荔链直达-前端" cmd /k "cd frontend && npm start"

echo.
echo 系统启动完成！
echo 请在浏览器中访问: http://localhost:3000
echo.
echo 演示产品ID: LC20240117001, LC20240117002
echo.
pause
