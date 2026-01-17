import os
import json
from datetime import datetime


def create_traceability_html(product_id, save_path="lychee_traceability.html"):
    """创建荔枝溯源网页"""

    # 模拟溯源数据
    trace_data = {
        "product_id": product_id,
        "product_name": "妃子笑荔枝",
        "brand": "岭南佳品",
        "origin": {
            "region": "广东省茂名市高州市",
            "farm": "高州荔枝示范基地",
            "coordinates": "21.9167° N, 110.8500° E"
        },
        "dates": {
            "bloom": "2024-03-15",
            "harvest": "2024-06-10",
            "packaging": "2024-06-11",
            "expiry": "2024-06-20"
        },
        "quality": {
            "grade": "特级",
            "sugar_content": "18.5°Bx",
            "size": "28-30g/颗",
            "freshness": "98%"
        },
        "certifications": [
            "绿色食品认证",
            "无公害农产品认证",
            "地理标志保护产品"
        ],
        "supply_chain": [
            {"step": "采摘", "date": "2024-06-10 06:30", "location": "高州基地A区", "operator": "张三"},
            {"step": "预冷", "date": "2024-06-10 08:00", "location": "基地冷库", "temperature": "1°C"},
            {"step": "分选", "date": "2024-06-10 10:30", "location": "加工中心", "grade": "特级果"},
            {"step": "包装", "date": "2024-06-11 09:00", "location": "包装车间", "package": "500g精品礼盒"},
            {"step": "质检", "date": "2024-06-11 11:00", "location": "质检中心", "result": "合格"},
            {"step": "运输", "date": "2024-06-11 14:00", "location": "冷链运输", "vehicle": "粤A·LC1234"}
        ],
        "farmer_info": {
            "name": "李大山",
            "experience": "20年荔枝种植经验",
            "phone": "138****5678",
            "certificate": "高级农艺师"
        },
        "testing": {
            "pesticide": "未检出",
            "heavy_metal": "符合国家标准",
            "report_no": "TS20240611001"
        }
    }

    # 生成HTML内容
    html_content = f'''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>荔枝产品溯源 - {trace_data['product_name']}</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Segoe UI', 'Microsoft YaHei', sans-serif;
            background: linear-gradient(135deg, #f9f3e9 0%, #fff5e6 100%);
            color: #333;
            line-height: 1.6;
            min-height: 100vh;
        }}

        .container {{
            max-width: 1000px;
            margin: 0 auto;
            padding: 20px;
        }}

        header {{
            background: linear-gradient(to right, #c40c0c, #e63946);
            color: white;
            padding: 30px 20px;
            border-radius: 15px 15px 0 0;
            text-align: center;
            box-shadow: 0 4px 12px rgba(196, 12, 12, 0.2);
        }}

        .logo {{
            font-size: 2.5rem;
            margin-bottom: 10px;
        }}

        h1 {{
            font-size: 2.2rem;
            margin-bottom: 10px;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.3);
        }}

        .product-id {{
            background: rgba(255,255,255,0.2);
            padding: 8px 15px;
            border-radius: 20px;
            display: inline-block;
            font-family: monospace;
            font-size: 1.1rem;
        }}

        .main-content {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 25px;
            margin-top: 25px;
        }}

        @media (max-width: 768px) {{
            .main-content {{
                grid-template-columns: 1fr;
            }}
        }}

        .card {{
            background: white;
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.08);
            transition: transform 0.3s ease;
        }}

        .card:hover {{
            transform: translateY(-5px);
        }}

        .card h2 {{
            color: #c40c0c;
            border-bottom: 2px solid #ffcc00;
            padding-bottom: 10px;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .card h2 i {{
            color: #ff9900;
        }}

        .info-item {{
            margin-bottom: 15px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 0;
            border-bottom: 1px dashed #eee;
        }}

        .info-label {{
            font-weight: 600;
            color: #666;
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .info-value {{
            font-weight: 500;
            color: #222;
            text-align: right;
        }}

        .timeline {{
            position: relative;
            padding-left: 30px;
        }}

        .timeline::before {{
            content: '';
            position: absolute;
            left: 15px;
            top: 0;
            bottom: 0;
            width: 2px;
            background: linear-gradient(to bottom, #c40c0c, #ff9900);
        }}

        .timeline-item {{
            position: relative;
            margin-bottom: 25px;
            padding-bottom: 15px;
            border-bottom: 1px solid #f0f0f0;
        }}

        .timeline-item:last-child {{
            border-bottom: none;
        }}

        .timeline-item::before {{
            content: '';
            position: absolute;
            left: -23px;
            top: 5px;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: #c40c0c;
            border: 3px solid white;
            box-shadow: 0 0 0 2px #c40c0c;
        }}

        .timeline-date {{
            color: #c40c0c;
            font-weight: 600;
            margin-bottom: 5px;
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .timeline-step {{
            font-weight: 600;
            margin-bottom: 5px;
            color: #333;
        }}

        .timeline-details {{
            color: #666;
            font-size: 0.9rem;
        }}

        .cert-badge {{
            display: inline-block;
            background: linear-gradient(to right, #4CAF50, #45a049);
            color: white;
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 0.85rem;
            margin: 5px;
            box-shadow: 0 2px 5px rgba(76, 175, 80, 0.3);
        }}

        .quality-badge {{
            background: linear-gradient(to right, #FF9800, #FF5722);
            color: white;
            padding: 8px 15px;
            border-radius: 10px;
            font-weight: bold;
            text-align: center;
            margin: 10px 0;
        }}

        .farmer-card {{
            background: linear-gradient(135deg, #e8f5e9, #c8e6c9);
            border-left: 5px solid #4CAF50;
            padding: 20px;
            border-radius: 10px;
            margin-top: 15px;
        }}

        .qrcode-section {{
            text-align: center;
            margin-top: 30px;
            padding: 20px;
            background: white;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        }}

        .qrcode-section h3 {{
            color: #c40c0c;
            margin-bottom: 15px;
        }}

        footer {{
            text-align: center;
            margin-top: 40px;
            padding: 20px;
            color: #666;
            font-size: 0.9rem;
            border-top: 1px solid #eee;
        }}

        .verification {{
            background: #f8f9fa;
            padding: 10px;
            border-radius: 8px;
            margin: 15px 0;
            text-align: center;
            border: 1px dashed #ccc;
        }}

        .stamp {{
            color: #c40c0c;
            font-weight: bold;
            font-size: 1.2rem;
            margin: 10px 0;
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <div class="logo">
                <i class="fas fa-seedling"></i>
            </div>
            <h1>荔枝产品溯源信息</h1>
            <p>每一颗荔枝，都有它的故事</p>
            <div class="product-id">
                <i class="fas fa-barcode"></i> 产品编号: {trace_data['product_id']}
            </div>
        </header>

        <div class="verification">
            <i class="fas fa-shield-check" style="color: #4CAF50; font-size: 1.5rem;"></i>
            <div class="stamp">✓ 正品验证通过</div>
            <p>本产品已通过区块链技术溯源验证，信息不可篡改</p>
            <p>验证时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        </div>

        <div class="main-content">
            <div class="card">
                <h2><i class="fas fa-info-circle"></i> 产品基本信息</h2>
                <div class="info-item">
                    <div class="info-label"><i class="fas fa-apple-alt"></i> 产品名称</div>
                    <div class="info-value">{trace_data['product_name']}</div>
                </div>
                <div class="info-item">
                    <div class="info-label"><i class="fas fa-tag"></i> 品牌</div>
                    <div class="info-value">{trace_data['brand']}</div>
                </div>
                <div class="info-item">
                    <div class="info-label"><i class="fas fa-map-marker-alt"></i> 原产地</div>
                    <div class="info-value">{trace_data['origin']['region']}</div>
                </div>
                <div class="info-item">
                    <div class="info-label"><i class="fas fa-tractor"></i> 种植基地</div>
                    <div class="info-value">{trace_data['origin']['farm']}</div>
                </div>

                <h2 style="margin-top: 30px;"><i class="fas fa-certificate"></i> 产品认证</h2>
                <div>
                    {''.join([f'<span class="cert-badge">{cert}</span>' for cert in trace_data['certifications']])}
                </div>
            </div>

            <div class="card">
                <h2><i class="fas fa-star"></i> 质量信息</h2>
                <div class="quality-badge">
                    品质等级: {trace_data['quality']['grade']}
                </div>
                <div class="info-item">
                    <div class="info-label"><i class="fas fa-wine-bottle"></i> 糖度</div>
                    <div class="info-value">{trace_data['quality']['sugar_content']}</div>
                </div>
                <div class="info-item">
                    <div class="info-label"><i class="fas fa-weight"></i> 单果重量</div>
                    <div class="info-value">{trace_data['quality']['size']}</div>
                </div>
                <div class="info-item">
                    <div class="info-label"><i class="fas fa-leaf"></i> 新鲜度</div>
                    <div class="info-value">{trace_data['quality']['freshness']}</div>
                </div>

                <h2 style="margin-top: 30px;"><i class="fas fa-calendar-alt"></i> 关键日期</h2>
                <div class="info-item">
                    <div class="info-label"><i class="fas fa-seedling"></i> 开花期</div>
                    <div class="info-value">{trace_data['dates']['bloom']}</div>
                </div>
                <div class="info-item">
                    <div class="info-label"><i class="fas fa-harvest"></i> 采摘日期</div>
                    <div class="info-value">{trace_data['dates']['harvest']}</div>
                </div>
                <div class="info-item">
                    <div class="info-label"><i class="fas fa-box"></i> 包装日期</div>
                    <div class="info-value">{trace_data['dates']['packaging']}</div>
                </div>
                <div class="info-item">
                    <div class="info-label"><i class="fas fa-clock"></i> 保质期至</div>
                    <div class="info-value">{trace_data['dates']['expiry']}</div>
                </div>
            </div>

            <div class="card" style="grid-column: 1 / -1;">
                <h2><i class="fas fa-road"></i> 供应链轨迹</h2>
                <div class="timeline">
                    {''.join([f'''
                    <div class="timeline-item">
                        <div class="timeline-date">
                            <i class="far fa-calendar"></i> {item['date']}
                        </div>
                        <div class="timeline-step">
                            <i class="fas fa-chevron-circle-right"></i> {item['step']}
                        </div>
                        <div class="timeline-details">
                            地点: {item['location']}
                            {f" • 操作员: {item['operator']}" if 'operator' in item else ''}
                            {f" • 温度: {item['temperature']}" if 'temperature' in item else ''}
                            {f" • 等级: {item['grade']}" if 'grade' in item else ''}
                            {f" • 包装: {item['package']}" if 'package' in item else ''}
                            {f" • 结果: {item['result']}" if 'result' in item else ''}
                            {f" • 车辆: {item['vehicle']}" if 'vehicle' in item else ''}
                        </div>
                    </div>
                    ''' for item in trace_data['supply_chain']])}
                </div>
            </div>

            <div class="card">
                <h2><i class="fas fa-user-tie"></i> 果农信息</h2>
                <div class="farmer-card">
                    <div class="info-item">
                        <div class="info-label"><i class="fas fa-user"></i> 姓名</div>
                        <div class="info-value">{trace_data['farmer_info']['name']}</div>
                    </div>
                    <div class="info-item">
                        <div class="info-label"><i class="fas fa-award"></i> 经验</div>
                        <div class="info-value">{trace_data['farmer_info']['experience']}</div>
                    </div>
                    <div class="info-item">
                        <div class="info-label"><i class="fas fa-certificate"></i> 资质</div>
                        <div class="info-value">{trace_data['farmer_info']['certificate']}</div>
                    </div>
                    <p style="margin-top: 15px; font-style: italic; color: #555;">
                        <i class="fas fa-quote-left"></i> 
                        我们用心种植每一颗荔枝，从开花到结果，坚持自然成熟，不使用催熟剂。
                        <i class="fas fa-quote-right"></i>
                    </p>
                </div>
            </div>

            <div class="card">
                <h2><i class="fas fa-flask"></i> 质量检测</h2>
                <div class="info-item">
                    <div class="info-label"><i class="fas fa-spray-can"></i> 农残检测</div>
                    <div class="info-value" style="color: #4CAF50;">
                        <i class="fas fa-check-circle"></i> {trace_data['testing']['pesticide']}
                    </div>
                </div>
                <div class="info-item">
                    <div class="info-label"><i class="fas fa-radiation"></i> 重金属检测</div>
                    <div class="info-value" style="color: #4CAF50;">
                        <i class="fas fa-check-circle"></i> {trace_data['testing']['heavy_metal']}
                    </div>
                </div>
                <div class="info-item">
                    <div class="info-label"><i class="fas fa-file-alt"></i> 检测报告编号</div>
                    <div class="info-value">{trace_data['testing']['report_no']}</div>
                </div>
                <div style="margin-top: 20px; padding: 15px; background: #f0f7ff; border-radius: 8px;">
                    <i class="fas fa-info-circle" style="color: #2196F3;"></i>
                    <strong>检测说明：</strong> 本批次荔枝经第三方检测机构检测，所有指标均符合国家食品安全标准。
                </div>
            </div>
        </div>

        <div class="qrcode-section">
            <h3><i class="fas fa-qrcode"></i> 分享本溯源信息</h3>
            <p>扫描二维码查看本产品溯源信息</p>
            <div id="qrcode-container">
                <!-- 二维码将在这里显示 -->
                <div style="padding: 20px; background: #f5f5f5; border-radius: 10px; display: inline-block; margin: 15px;">
                    <div style="text-align: center; color: #888; margin-bottom: 10px;">
                        <i class="fas fa-qrcode fa-3x"></i>
                        <p style="margin-top: 10px;">二维码位置</p>
                        <p><small>(将在下一步生成)</small></p>
                    </div>
                </div>
            </div>
            <p style="margin-top: 15px; color: #666;">
                <i class="fas fa-mobile-alt"></i> 使用手机扫描二维码，随时查看溯源信息
            </p>
        </div>

        <footer>
            <p>© 2024 岭南佳品荔枝溯源系统 | 每一份安心，源自透明</p>
            <p>客服热线: 400-123-4567 | 官方网站: www.lingnan-lychee.com</p>
            <p style="font-size: 0.8rem; margin-top: 10px; color: #999;">
                本溯源信息基于区块链技术，确保数据真实不可篡改。
                <br>最后更新: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            </p>
        </footer>
    </div>

    <script>
        // 简单的页面交互
        document.addEventListener('DOMContentLoaded', function() {{
            // 添加卡片点击效果
            const cards = document.querySelectorAll('.card');
            cards.forEach(card => {{
                card.addEventListener('click', function() {{
                    this.style.boxShadow = '0 10px 25px rgba(0,0,0,0.15)';
                    setTimeout(() => {{
                        this.style.boxShadow = '0 5px 15px rgba(0,0,0,0.08)';
                    }}, 300);
                }});
            }});

            // 显示当前时间
            function updateTime() {{
                const now = new Date();
                const timeStr = now.toLocaleString('zh-CN');
                const timeElement = document.getElementById('current-time');
                if (timeElement) {{
                    timeElement.textContent = timeStr;
                }}
            }}

            updateTime();
            setInterval(updateTime, 1000);
        }});
    </script>
</body>
</html>
'''

    # 保存HTML文件
    with open(save_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"✅ 溯源网页已创建: {save_path}")

    # 获取文件的绝对路径
    abs_path = os.path.abspath(save_path)
    file_url = f"file:///{abs_path.replace(os.sep, '/')}"

    return abs_path, file_url