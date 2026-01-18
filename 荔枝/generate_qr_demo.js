const QRCode = require('qrcode');
const fs = require('fs');
const path = require('path');

async function generateQRDemo() {
  const products = [
    {
      id: 'LC20240117001',
      name: '妃子笑荔枝',
      url: 'http://localhost:3000/trace/LC20240117001'
    },
    {
      id: 'LC20240117002',
      name: '桂味荔枝',
      url: 'http://localhost:3000/trace/LC20240117002'
    }
  ];

  console.log('========================================');
  console.log('荔链直达 - 二维码生成演示');
  console.log('========================================');
  console.log();

  // 创建二维码目录
  const qrDir = path.join(__dirname, 'qrcodes');
  if (!fs.existsSync(qrDir)) {
    fs.mkdirSync(qrDir);
  }

  for (const product of products) {
    try {
      // 生成二维码图片文件
      const filename = `qr_${product.id}.png`;
      const filepath = path.join(qrDir, filename);

      await QRCode.toFile(filepath, product.url, {
        width: 300,
        margin: 2,
        color: {
          dark: '#000000',
          light: '#FFFFFF'
        }
      });

      console.log(`✅ ${product.name} (${product.id})`);
      console.log(`   二维码文件: ${filename}`);
      console.log(`   访问链接: ${product.url}`);
      console.log(`   文件位置: ${filepath}`);
      console.log();

    } catch (error) {
      console.error(`❌ 生成 ${product.name} 二维码失败:`, error);
    }
  }

  console.log('========================================');
  console.log('二维码生成完成！');
  console.log('========================================');
  console.log();
  console.log('使用说明:');
  console.log('1. 启动系统后，用手机扫描这些二维码');
  console.log('2. 或者在浏览器中直接访问上面的链接');
  console.log('3. 二维码图片保存在 qrcodes/ 目录中');
  console.log();
  console.log('演示产品:');
  console.log('- LC20240117001: 妃子笑荔枝 (广东省茂名市电白区)');
  console.log('- LC20240117002: 桂味荔枝 (广东省湛江市徐闻县)');
}

// 直接运行生成
if (require.main === module) {
  generateQRDemo().catch(console.error);
}

module.exports = { generateQRDemo };
