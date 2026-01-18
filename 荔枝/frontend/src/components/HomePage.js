import React, { useState } from 'react';
import QRCode from 'qrcode.react';
import './HomePage.css';

function HomePage() {
  const [productId, setProductId] = useState('');
  const [showQR, setShowQR] = useState(false);

  const handleGenerateQR = () => {
    if (productId.trim()) {
      setShowQR(true);
    }
  };

  const qrUrl = productId ? `http://localhost:3000/trace/${productId}` : '';

  return (
    <div className="home-page">
      <div className="hero-section">
        <h1>区块链溯源系统</h1>
        <p>扫描二维码，查看荔枝从枝头到舌尖的全程信息</p>

        <div className="demo-section">
          <h2>演示功能</h2>
          <div className="input-group">
            <input
              type="text"
              placeholder="输入产品ID（如：LC20240117001）"
              value={productId}
              onChange={(e) => setProductId(e.target.value)}
            />
            <button onClick={handleGenerateQR}>生成二维码</button>
          </div>

          {showQR && (
            <div className="qr-display">
              <h3>产品二维码</h3>
              <QRCode value={qrUrl} size={200} />
              <p>扫描二维码查看溯源信息</p>
              <div className="demo-links">
                <a href={`/trace/${productId}`} target="_blank" rel="noopener noreferrer">
                  直接查看溯源页面
                </a>
              </div>
            </div>
          )}
        </div>

        <div className="features">
          <div className="feature-card">
            <h3>🌱 种植溯源</h3>
            <p>实时监测土壤、温度、湿度等种植环境数据</p>
          </div>
          <div className="feature-card">
            <h3>🚛 物流追踪</h3>
            <p>全程监控运输过程中的温度、湿度等关键指标</p>
          </div>
          <div className="feature-card">
            <h3>🔒 区块链验证</h3>
            <p>数据上链不可篡改，确保信息真实可靠</p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default HomePage;
