# 荔链直达 - 区块链溯源系统

基于区块链和物联网技术的荔枝全链路溯源平台，让每一颗荔枝都有"数字身份证"。

## 项目特色

- 🌱 **种植溯源**: 实时监测土壤、温度、湿度等种植环境
- 🚛 **物流追踪**: 全程监控运输过程中的关键指标
- 🔒 **区块链验证**: 数据上链不可篡改，确保信息真实可靠
- 📱 **移动端友好**: 支持二维码扫描查看溯源信息

## 技术架构

- **前端**: React + React Router
- **后端**: Node.js + Express
- **数据库**: MongoDB
- **二维码**: QRCode.js

## 快速开始

### 环境要求

- Node.js 16+ (推荐 18.x)
- MongoDB 4.4+ (数据库)
- Windows 7+ / macOS / Linux

### 环境安装

#### 1. 安装Node.js

**Windows用户:**
- 下载: https://nodejs.org/dist/v18.18.2/node-v18.18.2-x64.msi
- 双击安装，**务必勾选 "Add to PATH"**
- 验证: `node --version`

**macOS用户:**
```bash
brew install node
```

**Linux用户:**
```bash
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs
```

#### 2. 安装MongoDB

**Windows用户:**
- 下载: https://www.mongodb.com/try/download/community
- 选择 Windows x64 MSI
- 安装时选择 "Install MongoDB as a Service"
- 验证: `mongod --version`

**macOS用户:**
```bash
brew install mongodb/brew/mongodb-community
brew services start mongodb/brew/mongodb-community
```

**Linux用户:**
```bash
sudo apt-get install mongodb
sudo systemctl start mongodb
```

### 安装步骤

#### 方法一：一键安装和启动 (推荐)

1. **安装Node.js**
   - 下载安装程序: https://nodejs.org/dist/v18.18.2/node-v18.18.2-x64.msi
   - 双击运行安装程序，**务必勾选 "Add to PATH" 选项**
   - 重启命令提示符后验证: `node --version`

2. **运行环境检查脚本**
   ```bash
   # 双击运行 check_installation.bat
   # 脚本会自动安装所有依赖并初始化数据
   ```

3. **启动系统**
   ```bash
   # 双击运行 run_system.bat
   # 系统会自动打开浏览器访问页面
   ```

#### 方法二：手动安装

1. **安装Node.js**
   ```bash
   # 下载并安装Node.js 18.x
   # 确保npm也一同安装
   ```

2. **安装后端依赖**
   ```bash
   cd backend
   npm install
   ```

3. **安装前端依赖**
   ```bash
   cd ../frontend
   npm install
   ```

4. **启动MongoDB**
   ```bash
   # 确保MongoDB服务正在运行
   mongod
   ```

5. **初始化演示数据**
   ```bash
   cd backend
   node initDemoData.js
   ```

6. **启动服务**
   ```bash
   # 终端1 - 启动后端
   cd backend
   npm run dev

   # 终端2 - 启动前端
   cd frontend
   npm start
   ```

## 使用说明

### 演示功能

1. 打开浏览器访问 `http://localhost:3000`
2. 在"演示功能"部分输入产品ID，如：`LC20240117001`
3. 点击"生成二维码"查看二维码
4. 扫描二维码或点击"直接查看溯源页面"查看产品溯源信息

### 可用演示数据

- **LC20240117001**: 妃子笑荔枝 - 广东省茂名市电白区
- **LC20240117002**: 桂味荔枝 - 广东省湛江市徐闻县

## API 接口

### 获取产品溯源信息
```
GET /api/trace/:productId
```

### 生成二维码
```
GET /api/qrcode/:productId
```

### 创建新产品
```
POST /api/products
```

### 更新产品信息
```
PUT /api/products/:productId
```

## 溯源信息包含内容

- 📋 基本信息（产品ID、名称、品种、产地）
- 👨‍🌾 农户信息（姓名、种植地点、联系方式）
- 📅 时间信息（种植日期、采摘日期）
- 🌱 种植过程（土壤环境、生长条件、施肥农药记录）
- 🚜 生长监控（灌溉方式、监控记录）
- ✂️ 采摘加工（采摘方式、品质等级、加工流程）
- 🚚 物流运输（运输方式、温度控制、目的地）
- 🔒 区块链验证（哈希值验证）

## 项目结构

```
lichi-trace/
├── backend/                 # 后端服务
│   ├── server.js           # 主服务器文件
│   ├── initDemoData.js     # 演示数据初始化
│   ├── package.json        # 后端依赖
│   └── .env.example        # 环境配置示例
├── frontend/               # 前端应用
│   ├── src/
│   │   ├── components/     # React组件
│   │   │   ├── Header.js
│   │   │   ├── HomePage.js
│   │   │   ├── TracePage.js
│   │   │   └── ...
│   │   ├── App.js
│   │   └── index.js
│   └── package.json        # 前端依赖
└── README.md              # 项目说明
```

## 未来扩展计划

- [ ] 集成真实区块链网络
- [ ] 添加物联网传感器数据接入
- [ ] 实现移动端App
- [ ] 添加用户管理系统
- [ ] 实现果树认养功能
- [ ] 添加定制礼盒系统

## 许可证

MIT License

## 联系我们

如有问题或建议，请联系开发团队。
