@echo off
echo ========================================
echo    荔链直达 - 溯源服务器启动
echo ========================================
echo.

echo 正在检查Node.js...
node --version >nul 2>&1
if errorlevel 1 (
    echo [X] Node.js未安装或不在PATH中
    echo 请先安装Node.js: https://nodejs.org
    pause
    exit /b 1
)

echo 正在检查npm...
npm --version >nul 2>&1
if errorlevel 1 (
    echo [X] npm未安装
    pause
    exit /b 1
)

echo.
echo ========================================
echo        正在安装依赖...
echo ========================================
echo.

call npm install express

if errorlevel 1 (
    echo [X] 依赖安装失败
    pause
    exit /b 1
)

echo.
echo ========================================
echo        启动服务器...
echo ========================================
echo.

echo 服务器将在 http://localhost:3000 启动
echo 按任意键开始...
pause >nul

node start_server.js
