import qrcode
from PIL import Image, ImageDraw, ImageFont
import os


def generate_qrcode_for_webpage(webpage_url, product_id, output_path="lychee_qrcode.png"):
    """生成链接到网页的二维码"""

    # 创建二维码
    qr = qrcode.QRCode(
        version=7,  # 适当版本
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # 高容错率
        box_size=12,
        border=2,
    )

    # 使用网页URL作为二维码内容
    qr.add_data(webpage_url)
    qr.make(fit=True)

    # 生成二维码图片
    img = qr.make_image(fill_color="#C40C0C", back_color="#FFF9E6")  # 荔枝主题色

    # 添加logo（可选）
    try:
        # 如果有logo文件，可以添加
        logo_size = 60
        logo = Image.new('RGBA', (logo_size, logo_size), (255, 255, 255, 0))
        draw_logo = ImageDraw.Draw(logo)

        # 绘制简单的荔枝logo
        draw_logo.ellipse([10, 10, logo_size - 10, logo_size - 10],
                          fill="#C40C0C", outline="#8B0000", width=3)
        draw_logo.ellipse([18, 18, 22, 22], fill="#FFCC00")  # 中心点
        draw_logo.ellipse([30, 15, 35, 20], fill="#228B22")  # 叶子

        # 计算logo位置（居中）
        img_width, img_height = img.size
        logo_position = ((img_width - logo_size) // 2, (img_height - logo_size) // 2)

        # 创建白色背景
        logo_bg = Image.new('RGBA', (logo_size + 8, logo_size + 8), (255, 255, 255, 255))
        logo_bg.paste(logo, (4, 4), logo)

        # 粘贴logo到二维码中心
        img.paste(logo_bg, logo_position)
    except Exception as e:
        print(f"⚠️ Logo添加失败: {e}")

    # 添加边框和文字
    draw = ImageDraw.Draw(img)

    # 添加产品ID文字
    try:
        font = ImageFont.truetype("arial.ttf", 18)
    except:
        font = ImageFont.load_default()

    # 在底部添加文字
    text = f"荔枝溯源 ID: {product_id}"
    text_width = draw.textlength(text, font=font)
    text_position = ((img_width - text_width) // 2, img_height - 30)

    # 添加文字背景
    draw.rectangle(
        [text_position[0] - 10, text_position[1] - 5,
         text_position[0] + text_width + 10, text_position[1] + 25],
        fill="#FFF9E6"
    )

    draw.text(text_position, text, fill="#C40C0C", font=font)

    # 保存二维码
    img.save(output_path)
    print(f"✅ 二维码已生成: {output_path}")
    print(f"🔗 二维码链接到: {webpage_url}")

    return output_path