@echo off
echo ========================================
echo    荔链直达 - 启动服务
echo ========================================

echo 正在检查Node.js...
node --version >nul 2>&1
if errorlevel 1 (
    echo [X] Node.js未安装或不在PATH中
    echo 请先运行 check_installation.bat 来检查环境
    pause
    exit /b 1
)

echo 正在检查npm...
npm --version >nul 2>&1
if errorlevel 1 (
    echo [X] npm未安装
    echo 请先运行 check_installation.bat 来检查环境
    pause
    exit /b 1
)

echo.
echo ========================================
echo          系统启动中...
echo ========================================
echo.
echo 后端服务将在 http://localhost:3001 启动
echo 前端服务将在 http://localhost:3000 启动
echo.
echo 按任意键开始启动...
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
