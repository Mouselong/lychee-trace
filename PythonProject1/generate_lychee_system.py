import http.server
import socketserver
import webbrowser
import threading
import time


def start_local_server(html_file_path, port=8000):
    """启动本地HTTP服务器"""

    # 切换到HTML文件所在目录
    os.chdir(os.path.dirname(html_file_path))
    html_filename = os.path.basename(html_file_path)

    # 自定义请求处理程序
    class CustomHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            # 默认重定向到我们的HTML文件
            if self.path == '/':
                self.path = f'/{html_filename}'
            return http.server.SimpleHTTPRequestHandler.do_GET(self)

    handler = CustomHandler

    # 启动服务器
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"🌐 本地服务器启动: http://localhost:{port}")
        print(f"📄 访问网页: http://localhost:{port}/{html_filename}")
        print("🛑 按 Ctrl+C 停止服务器")

        # 在浏览器中打开
        webbrowser.open(f"http://localhost:{port}")

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 服务器已停止")


def create_integrated_solution():
    """创建完整的溯源解决方案"""

    # 产品ID
    product_id = "LZ20240615001"

    print("=" * 60)
    print("         荔枝产品溯源系统生成器")
    print("=" * 60)

    # 1. 创建溯源网页
    print("\n📝 步骤1: 创建溯源网页...")
    html_path, file_url = create_traceability_html(product_id, "lychee_traceability.html")

    # 2. 生成二维码
    print("\n📱 步骤2: 生成二维码...")

    # 使用本地服务器URL作为二维码内容
    local_url = f"http://localhost:8000/lychee_traceability.html"
    qr_path = generate_qrcode_for_webpage(local_url, product_id, "lychee_qrcode.png")

    # 3. 生成一个包含二维码的HTML预览页面
    print("\n🎨 步骤3: 创建预览页面...")
    create_preview_page(product_id, html_path, qr_path)

    print("\n" + "=" * 60)
    print("🎉 生成完成!")
    print("=" * 60)
    print(f"\n📁 生成的文件:")
    print(f"  1. 溯源网页: {html_path}")
    print(f"  2. 二维码图片: {qr_path}")
    print(f"  3. 预览页面: lychee_preview.html")

    print("\n📋 下一步操作:")
    print("  1. 打开 'lychee_preview.html' 查看完整效果")
    print("  2. 扫描二维码或在浏览器中打开溯源网页")
    print("  3. 如需在线访问，请将文件上传到Web服务器")

    # 询问是否启动本地服务器
    response = input("\n🚀 是否启动本地服务器测试? (y/n): ")
    if response.lower() == 'y':
        print("\n正在启动本地服务器...")
        start_local_server(html_path)


def create_preview_page(product_id, html_path, qr_path):
    """创建包含二维码的预览页面"""

    preview_html = f'''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>荔枝溯源预览</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 1000px;
            margin: 0 auto;
            padding: 20px;
            background: #f9f3e9;
        }}
        .header {{
            text-align: center;
            background: linear-gradient(to right, #c40c0c, #e63946);
            color: white;
            padding: 25px;
            border-radius: 15px;
            margin-bottom: 30px;
        }}
        .container {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
        }}
        @media (max-width: 768px) {{
            .container {{ grid-template-columns: 1fr; }}
        }}
        .card {{
            background: white;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }}
        .qrcode-card {{
            text-align: center;
        }}
        .qrcode-img {{
            max-width: 100%;
            border: 1px solid #ddd;
            border-radius: 10px;
            margin: 15px 0;
        }}
        .btn {{
            display: inline-block;
            background: #c40c0c;
            color: white;
            padding: 12px 25px;
            border-radius: 8px;
            text-decoration: none;
            margin: 10px;
            font-weight: bold;
            transition: all 0.3s;
        }}
        .btn:hover {{
            background: #a00a0a;
            transform: translateY(-2px);
        }}
        .instructions {{
            background: #e8f5e9;
            padding: 20px;
            border-radius: 10px;
            margin-top: 30px;
        }}
        .step {{
            display: flex;
            align-items: center;
            margin: 15px 0;
        }}
        .step-num {{
            background: #c40c0c;
            color: white;
            width: 30px;
            height: 30px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-right: 15px;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🍒 荔枝产品溯源系统预览</h1>
        <p>产品ID: {product_id} | 生成时间: {time.strftime("%Y-%m-%d %H:%M:%S")}</p>
    </div>

    <div class="container">
        <div class="card">
            <h2>📱 产品二维码</h2>
            <p>使用手机扫描此二维码查看产品溯源信息</p>

            <img src="{qr_path}" alt="荔枝溯源二维码" class="qrcode-img">

            <p>
                <a href="{html_path}" class="btn" target="_blank">
                    <i class="fas fa-external-link-alt"></i> 直接打开网页
                </a>
                <a href="{qr_path}" class="btn" download>
                    <i class="fas fa-download"></i> 下载二维码
                </a>
            </p>

            <h3>测试二维码扫描:</h3>
            <ol>
                <li>使用手机摄像头或微信"扫一扫"</li>
                <li>扫描上方的二维码</li>
                <li>将跳转到产品溯源页面</li>
            </ol>
        </div>

        <div class="card">
            <h2>🌐 溯源网页预览</h2>
            <p>完整的荔枝产品溯源信息页面</p>

            <div style="border: 2px dashed #ccc; padding: 15px; border-radius: 10px; margin: 20px 0;">
                <h3>网页包含内容:</h3>
                <ul>
                    <li>✔️ 产品基本信息</li>
                    <li>✔️ 原产地信息</li>
                    <li>✔️ 供应链轨迹</li>
                    <li>✔️ 质量检测报告</li>
                    <li>✔️ 果农信息</li>
                    <li>✔️ 产品认证信息</li>
                </ul>
            </div>

            <iframe src="{html_path}" 
                    style="width: 100%; height: 300px; border: 1px solid #ddd; border-radius: 8px;">
            </iframe>

            <p style="text-align: center; margin-top: 15px;">
                <a href="{html_path}" class="btn" target="_blank">
                    <i class="fas fa-external-link-alt"></i> 在新窗口打开完整网页
                </a>
            </p>
        </div>
    </div>

    <div class="instructions">
        <h2>📋 使用说明</h2>

        <div class="step">
            <div class="step-num">1</div>
            <div>
                <strong>测试二维码:</strong> 使用手机扫描左侧二维码，查看手机端显示效果
            </div>
        </div>

        <div class="step">
            <div class="step-num">2</div>
            <div>
                <strong>部署到服务器:</strong> 将 "lychee_traceability.html" 上传到您的Web服务器
            </div>
        </div>

        <div class="step">
            <div class="step-num">3</div>
            <div>
                <strong>更新二维码链接:</strong> 将二维码中的链接改为您的服务器URL
            </div>
        </div>

        <div class="step">
            <div class="step-num">4</div>
            <div>
                <strong>打印二维码:</strong> 将 "lychee_qrcode.png" 打印到产品包装上
            </div>
        </div>
    </div>

    <div style="text-align: center; margin-top: 30px; color: #666;">
        <p>© 2024 荔枝溯源系统 | 生成工具 v1.0</p>
    </div>

    <script>
        // 添加Font Awesome图标
        const faScript = document.createElement('script');
        faScript.src = 'https://kit.fontawesome.com/a076d05399.js';
        faScript.crossOrigin = 'anonymous';
        document.head.appendChild(faScript);
    </script>
</body>
</html>
'''

    with open("lychee_preview.html", "w", encoding="utf-8") as f:
        f.write(preview_html)

    print(f"✅ 预览页面已创建: lychee_preview.html")


# 主程序入口
if __name__ == "__main__":
    print("开始生成荔枝产品溯源系统...")
    create_integrated_solution()

    # 询问是否打开预览页面
    response = input("\n🖥️ 是否打开预览页面? (y/n): ")
    if response.lower() == 'y':
        webbrowser.open("lychee_preview.html")