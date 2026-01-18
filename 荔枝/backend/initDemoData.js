const mongoose = require('mongoose');
const config = require('./config');

// 产品模型
const ProductSchema = new mongoose.Schema({
  productId: { type: String, required: true, unique: true },
  name: { type: String, required: true },
  variety: String,
  origin: String,
  farmer: {
    name: String,
    location: String,
    contact: String
  },
  plantingDate: Date,
  harvestDate: Date,
  traceabilityData: {
    planting: {
      soil: String,
      temperature: String,
      humidity: String,
      fertilizers: [String],
      pesticides: [String]
    },
    growth: {
      irrigation: String,
      monitoring: [String]
    },
    harvest: {
      method: String,
      date: Date,
      quality: String
    },
    processing: {
      cleaning: String,
      packaging: String,
      storage: String
    },
    logistics: {
      transport: String,
      temperature: String,
      destination: String
    }
  },
  qrCode: String,
  blockchainHash: String,
  createdAt: { type: Date, default: Date.now }
});

const Product = mongoose.model('Product', ProductSchema);

// 演示数据
const demoProducts = [
  {
    productId: 'LC20240117001',
    name: '妃子笑荔枝',
    variety: '妃子笑',
    origin: '广东省茂名市电白区',
    farmer: {
      name: '李师傅',
      location: '广东省茂名市电白区林头镇',
      contact: '13812345678'
    },
    plantingDate: new Date('2024-01-01'),
    harvestDate: new Date('2024-06-15'),
    traceabilityData: {
      planting: {
        soil: '有机土壤，PH值6.5-7.0',
        temperature: '25-30°C',
        humidity: '60-80%',
        fertilizers: ['有机肥', '磷酸二氢钾', '钙镁磷肥'],
        pesticides: ['无农药', '采用物理防治和生物防治']
      },
      growth: {
        irrigation: '滴灌系统，定时定量供水',
        monitoring: ['每日人工巡检', '物联网传感器实时监测', '定期土壤检测']
      },
      harvest: {
        method: '手工采摘，成熟度80%以上',
        date: new Date('2024-06-15'),
        quality: '一级品'
      },
      processing: {
        cleaning: '清水清洗，去除杂质',
        packaging: '真空包装，保鲜处理',
        storage: '冷藏存储，温度控制在5°C'
      },
      logistics: {
        transport: '冷链运输车',
        temperature: '5-8°C',
        destination: '全国各大城市'
      }
    },
    blockchainHash: '0x8f7e2a9b3c5d1e4f6a8b2c9d3e5f7a1b4c6d8e9f2a3b5c7d9e1f3a5b7c9d1e3f5a'
  },
  {
    productId: 'LC20240117002',
    name: '桂味荔枝',
    variety: '桂味',
    origin: '广东省湛江市',
    farmer: {
      name: '王阿姨',
      location: '广东省湛江市徐闻县',
      contact: '13987654321'
    },
    plantingDate: new Date('2024-01-05'),
    harvestDate: new Date('2024-06-20'),
    traceabilityData: {
      planting: {
        soil: '沙质土壤，排水良好',
        temperature: '24-28°C',
        humidity: '65-75%',
        fertilizers: ['复合肥', '有机肥料', '微量元素肥'],
        pesticides: ['绿色防控', '物理防治']
      },
      growth: {
        irrigation: '喷灌系统，适时适量',
        monitoring: ['智能传感器监测', '专家定期指导', '生长日志记录']
      },
      harvest: {
        method: '分批采摘，保证新鲜度',
        date: new Date('2024-06-20'),
        quality: '特级品'
      },
      processing: {
        cleaning: '纯净水清洗',
        packaging: '气调包装',
        storage: '恒温冷库'
      },
      logistics: {
        transport: '专业冷链物流',
        temperature: '4-6°C',
        destination: '华南地区各大超市'
      }
    },
    blockchainHash: '0x1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3'
  }
];

// 初始化演示数据
async function initDemoData() {
  try {
    await mongoose.connect(config.MONGODB_URI, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });

    console.log('连接数据库成功');

    // 清空现有数据
    await Product.deleteMany({});
    console.log('清空现有数据');

    // 插入演示数据
    await Product.insertMany(demoProducts);
    console.log('演示数据插入成功');

    console.log('演示数据初始化完成！');
    console.log('可用产品ID：');
    demoProducts.forEach(product => {
      console.log(`- ${product.productId}: ${product.name}`);
    });

  } catch (error) {
    console.error('初始化演示数据失败:', error);
  } finally {
    await mongoose.connection.close();
    console.log('数据库连接已关闭');
  }
}

// 运行初始化
if (require.main === module) {
  initDemoData();
}

module.exports = { initDemoData };
