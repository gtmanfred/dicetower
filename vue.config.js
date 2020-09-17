var path = require('path')

module.exports = {
  configureWebpack: {
    devtool: 'source-map'
  },
  publicPath: process.env.NODE_ENV === 'production' ? '/ui/' : '/',
  outputDir: path.resolve(__dirname, 'dicetower/static')
}
