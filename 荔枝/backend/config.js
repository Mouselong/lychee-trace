// 配置文件
module.exports = {
  PORT: process.env.PORT || 3001,
  MONGODB_URI: process.env.MONGODB_URI || 'mongodb://localhost:27017/lichi-trace',
  FRONTEND_URL: process.env.FRONTEND_URL || 'http://localhost:3000',
  BLOCKCHAIN_RPC_URL: process.env.BLOCKCHAIN_RPC_URL || '',
  BLOCKCHAIN_PRIVATE_KEY: process.env.BLOCKCHAIN_PRIVATE_KEY || ''
};
