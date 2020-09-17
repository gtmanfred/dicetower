var path = require('path');

module.exports = {
  publicPath: process.env.NODE_ENV === 'production' ? '/ui/' : '/',
  outputDir: path.resolve(__dirname, 'dicetower/static'),
  devServer: {
    proxy: {
      '^/(api|openapi.json)': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      },
    },
  },
};
