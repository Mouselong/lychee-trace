const express = require('express');
const path = require('path');
const app = express();
const PORT = 3000;

// 提供静态文件服务
app.use(express.static(path.join(__dirname)));

// 根路径重定向到演示页面
app.get('/', (req, res) => {
    res.redirect('/专业溯源演示.html');
});

// 溯源查询路由
app.get('/trace/:id', (req, res) => {
    const productId = req.params.id;
    // 重定向到本地HTML页面，带参数
    res.redirect(`/webTrace/trace.html?id=${encodeURIComponent(productId)}`);
});

// 兼容旧的URL格式
app.get('/webTrace/trace', (req, res) => {
    const id = req.query.id;
    if (id) {
        res.redirect(`/webTrace/trace.html?id=${encodeURIComponent(id)}`);
    } else {
        res.redirect('/webTrace/trace.html');
    }
});

app.listen(PORT, () => {
    console.log(`🌐 荔链直达服务器已启动！`);
    console.log(`📱 访问地址: http://localhost:${PORT}`);
    console.log(`📋 演示页面: http://localhost:${PORT}/专业溯源演示.html`);
    console.log(`🔍 溯源查询: http://localhost:${PORT}/webTrace/trace.html`);
    console.log(`❌ 按 Ctrl+C 停止服务器`);
});
