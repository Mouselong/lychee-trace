import React from 'react';
import './Header.css';

function Header() {
  return (
    <header className="header">
      <div className="header-content">
        <div className="logo">
          <h1>荔链直达</h1>
          <p>区块链溯源，让每一颗荔枝都有身份证</p>
        </div>
        <nav className="nav">
          <a href="/">首页</a>
          <a href="#about">关于我们</a>
          <a href="#contact">联系我们</a>
        </nav>
      </div>
    </header>
  );
}

export default Header;
