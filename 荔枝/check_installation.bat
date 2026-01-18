@echo off
echo ========================================
echo    荔链直达 - 环境检查脚本
echo ========================================

echo 正在检查Node.js...
node --version >nul 2>&1
if errorlevel 1 (
    echo [X] Node.js未安装或不在PATH中
    echo.
    echo 请重新安装Node.js，并确保添加到系统PATH
    echo 下载地址: https://nodejs.org/dist/v18.18.2/node-v18.18.2-x64.msi
    pause
    exit /b 1
) else (
    echo [√] Node.js已安装
    node --version
)

echo.
echo 正在检查npm...
npm --version >nul 2>&1
if errorlevel 1 (
    echo [X] npm未安装
    pause
    exit /b 1
) else (
    echo [√] npm已安装
    npm --version
)

echo.
echo ========================================
echo        环境检查完成，开始安装依赖
echo ========================================

echo 正在安装后端依赖...
cd backend
if not exist node_modules (
    npm install
    if errorlevel 1 (
        echo [X] 后端依赖安装失败
        pause
        exit /b 1
    )
) else (
    echo [√] 后端依赖已存在
)

echo 正在安装前端依赖...
cd ../frontend
if not exist node_modules (
    npm install
    if errorlevel 1 (
        echo [X] 前端依赖安装失败
        pause
        exit /b 1
    )
) else (
    echo [√] 前端依赖已存在
)

echo.
echo ========================================
echo        初始化演示数据
echo ========================================

cd ../backend
echo 正在初始化演示数据...
node initDemoData.js
if errorlevel 1 (
    echo [X] 演示数据初始化失败
    echo 但系统仍可运行
) else (
    echo [√] 演示数据初始化成功
)

echo.
echo ========================================
echo         [√] 环境准备完成！
echo ========================================
echo.
echo 现在可以运行 run_system.bat 来启动系统
echo 或手动运行以下命令：
echo.
echo 启动后端: cd backend && npm run dev
echo 启动前端: cd frontend && npm start
echo.
pause
