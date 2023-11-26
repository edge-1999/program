// 引入Express模块
const express = require('express');

// 创建Express应用
const app = express();

// 定义一个简单的路由：当访问根URL时，返回"Hello World!"
app.get('/', (req, res) => {
    res.send('Hello World!');
});

// 设置应用监听3000端口
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});