import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import './TracePage.css';

function TracePage() {
  const { productId } = useParams();
  const [product, setProduct] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchProductData();
  }, [productId]);

  const fetchProductData = async () => {
    try {
      setLoading(true);
      const response = await axios.get(`http://localhost:3001/api/trace/${productId}`);
      setProduct(response.data);
      setError(null);
    } catch (err) {
      setError('未找到该产品信息，请检查产品ID是否正确');
      console.error('获取产品信息失败:', err);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="trace-container">
        <div className="loading">
          <div>正在加载产品溯源信息...</div>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="trace-container">
        <div className="error">{error}</div>
        <div className="demo-data">
          <h3>演示数据</h3>
          <p>为了展示效果，以下是示例产品数据：</p>
          <div className="demo-product">
            <h4>荔枝产品ID: LC20240117001</h4>
            <p>品种: 妃子笑</p>
            <p>产地: 广东省茂名市</p>
            <p>农户: 李师傅</p>
            <p>种植日期: 2024-01-01</p>
            <p>采摘日期: 2024-06-15</p>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="trace-container">
      <div className="trace-card">
        <h1 className="trace-title">🌰 荔枝溯源信息</h1>

        <div className="trace-info">
          <div className="info-item">
            <h4>📋 基本信息</h4>
            <p><strong>产品ID:</strong> {product.productId}</p>
            <p><strong>产品名称:</strong> {product.name}</p>
            <p><strong>品种:</strong> {product.variety}</p>
            <p><strong>产地:</strong> {product.origin}</p>
          </div>

          <div className="info-item">
            <h4>👨‍🌾 农户信息</h4>
            <p><strong>农户姓名:</strong> {product.farmer?.name}</p>
            <p><strong>种植地点:</strong> {product.farmer?.location}</p>
            <p><strong>联系方式:</strong> {product.farmer?.contact}</p>
          </div>

          <div className="info-item">
            <h4>📅 时间信息</h4>
            <p><strong>种植日期:</strong> {product.plantingDate ? new Date(product.plantingDate).toLocaleDateString('zh-CN') : '暂无'}</p>
            <p><strong>采摘日期:</strong> {product.harvestDate ? new Date(product.harvestDate).toLocaleDateString('zh-CN') : '暂无'}</p>
          </div>
        </div>

        <div className="trace-section">
          <h3>🌱 种植过程</h3>
          <div className="trace-info">
            <div className="info-item">
              <h4>土壤环境</h4>
              <p>{product.traceabilityData?.planting?.soil || '有机土壤，PH值适中'}</p>
            </div>
            <div className="info-item">
              <h4>生长条件</h4>
              <p><strong>温度:</strong> {product.traceabilityData?.planting?.temperature || '25-30°C'}</p>
              <p><strong>湿度:</strong> {product.traceabilityData?.planting?.humidity || '60-80%'}</p>
            </div>
            <div className="info-item">
              <h4>施肥记录</h4>
              <ul>
                {(product.traceabilityData?.planting?.fertilizers || ['有机肥', '复合肥']).map((fert, index) => (
                  <li key={index}>{fert}</li>
                ))}
              </ul>
            </div>
            <div className="info-item">
              <h4>农药使用</h4>
              <ul>
                {(product.traceabilityData?.planting?.pesticides || ['无农药', '绿色防控']).map((pest, index) => (
                  <li key={index}>{pest}</li>
                ))}
              </ul>
            </div>
          </div>
        </div>

        <div className="trace-section">
          <h3>🚜 生长监控</h3>
          <div className="trace-info">
            <div className="info-item">
              <h4>灌溉方式</h4>
              <p>{product.traceabilityData?.growth?.irrigation || '滴灌系统，定时定量'}</p>
            </div>
            <div className="info-item">
              <h4>监控记录</h4>
              <ul>
                {(product.traceabilityData?.growth?.monitoring || ['每日人工巡检', '物联网传感器监控']).map((monitor, index) => (
                  <li key={index}>{monitor}</li>
                ))}
              </ul>
            </div>
          </div>
        </div>

        <div className="trace-section">
          <h3>✂️ 采摘加工</h3>
          <div className="trace-info">
            <div className="info-item">
              <h4>采摘方式</h4>
              <p>{product.traceabilityData?.harvest?.method || '手工采摘'}</p>
            </div>
            <div className="info-item">
              <h4>采摘日期</h4>
              <p>{product.traceabilityData?.harvest?.date ? new Date(product.traceabilityData.harvest.date).toLocaleDateString('zh-CN') : '2024-06-15'}</p>
            </div>
            <div className="info-item">
              <h4>品质等级</h4>
              <p>{product.traceabilityData?.harvest?.quality || '一级品'}</p>
            </div>
            <div className="info-item">
              <h4>加工流程</h4>
              <p><strong>清洗:</strong> {product.traceabilityData?.processing?.cleaning || '清水清洗'}</p>
              <p><strong>包装:</strong> {product.traceabilityData?.processing?.packaging || '真空包装'}</p>
              <p><strong>存储:</strong> {product.traceabilityData?.processing?.storage || '冷藏存储'}</p>
            </div>
          </div>
        </div>

        <div className="trace-section">
          <h3>🚚 物流运输</h3>
          <div className="trace-info">
            <div className="info-item">
              <h4>运输方式</h4>
              <p>{product.traceabilityData?.logistics?.transport || '冷链运输'}</p>
            </div>
            <div className="info-item">
              <h4>运输温度</h4>
              <p>{product.traceabilityData?.logistics?.temperature || '5-8°C'}</p>
            </div>
            <div className="info-item">
              <h4>目的地</h4>
              <p>{product.traceabilityData?.logistics?.destination || '全国各大城市'}</p>
            </div>
          </div>
        </div>

        {product.blockchainHash && (
          <div className="trace-section">
            <h3>🔒 区块链验证</h3>
            <div className="info-item">
              <h4>区块链哈希</h4>
              <p style={{ fontFamily: 'monospace', fontSize: '14px' }}>{product.blockchainHash}</p>
              <p>✅ 数据已上链，不可篡改</p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default TracePage;
