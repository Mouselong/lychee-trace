# 保存为: generate_lychee_traceability.py
import os
import webbrowser
import qrcode
from PIL import Image, ImageDraw


def quick_generate():
    """一键生成荔枝溯源解决方案"""

    print("🚀 正在生成荔枝溯源解决方案...")

    # 创建简单的HTML页面
    html_content = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>荔枝产品溯源</title>
    <style>
        body { font-family: Arial; max-width: 800px; margin: auto; padding: 20px; }
        .header { background: #c40c0c; color: white; padding: 20px; text-align: center; }
        .info { background: #f9f9f9; padding: 20px; margin: 20px 0; border-radius: 10px; }
        .qrcode { text-align: center; margin: 30px 0; }
    </style>
</head>
<body>
    <div class="header">
        <h1>🍒 妃子笑荔枝产品溯源</h1>
        <p>产品编号: LZ20240615001</p>
    </div>

    <div class="info">
        <h2>产品信息</h2>
        <p><strong>产地:</strong> 广东茂名高州市</p>
        <p><strong>采摘日期:</strong> 2024年6月10日</p>
        <p><strong>等级:</strong> 特级果</p>
        <p><strong>保质期:</strong> 2024年6月20日</p>
    </div>

    <div class="info">
        <h2>溯源轨迹</h2>
        <p>✅ 2024-06-10 06:30 基地采摘</p>
        <p>✅ 2024-06-10 08:00 预冷处理</p>
        <p>✅ 2024-06-10 10:30 分选包装</p>
        <p>✅ 2024-06-11 14:00 冷链运输</p>
    </div>

    <div class="qrcode">
        <h3>扫描二维码验证产品</h3>
        <p><small>本页面为模拟溯源信息，仅供演示使用</small></p>
    </div>

    <div style="text-align: center; color: #666; margin-top: 40px;">
        <p>© 2024 荔枝溯源系统 | 客服: 400-123-4567</p>
    </div>
</body>
</html>
"""

    # 保存HTML文件
    with open("Upload website files/lychee_trace_simple.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    # 生成二维码
    qr = qrcode.QRCode(version=5, box_size=10, border=2)
    qr.add_data("http://localhost:8000/lychee_trace_simple.html")
    qr.make(fit=True)
    img = qr.make_image(fill_color="#c40c0c", back_color="white")

    # 添加文字
    draw = ImageDraw.Draw(img)
    draw.text((50, img.height - 30), "荔枝溯源", fill="#c40c0c")

    img.save("lychee_qrcode_simple.png")

    print("✅ 生成完成!")
    print("📁 生成的文件:")
    print("  1. lychee_trace_simple.html - 溯源网页")
    print("  2. lychee_qrcode_simple.png - 二维码")

    # 创建说明文件
    with open("README.txt", "w", encoding="utf-8") as f:
        f.write("荔枝溯源系统使用说明\n")
        f.write("=" * 30 + "\n")
        f.write("1. 将 lychee_trace_simple.html 上传到服务器\n")
        f.write("2. 更新二维码中的链接为实际服务器地址\n")
        f.write("3. 打印二维码到产品包装上\n")
        f.write("\n测试方法:\n")
        f.write("1. 在文件所在目录运行: python -m http.server 8000\n")
        f.write("2. 打开浏览器访问: http://localhost:8000/lychee_trace_simple.html\n")
        f.write("3. 扫描二维码测试\n")

    print("\n📋 详细说明请查看 README.txt")

    # 询问是否打开文件
    if input("\n打开HTML文件? (y/n): ").lower() == 'y':
        webbrowser.open("Upload website files/lychee_trace_simple.html")

    if input("打开二维码图片? (y/n): ").lower() == 'y':
        webbrowser.open("Upload website files/lychee_qrcode_simple.png")


if __name__ == "__main__":
    quick_generate()