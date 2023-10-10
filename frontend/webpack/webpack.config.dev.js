module.exports = {
  mode: 'development',
  entry: ['./src/index.tsx'],
  module: {
    rules: require('./webpack.rules'),
  },
  output: {
    filename: '[name].js',
    chunkFilename: '[name].chunk.js',
  },
  plugins: require('./webpack.plugins'),
  resolve: {
    extensions: ['.js', '.ts', '.jsx', '.tsx', '.css'],
    alias: {
      // custom aliases
      ...require('./webpack.aliases'),
    },
  },
  externalsType: 'script',
  externals: {
    '@yandex/ymaps3-types': [
      `new Promise((resolve) => {
          if (typeof ymaps3 !== 'undefined') {
            return ymaps3.ready.then(() => resolve(ymaps3));
          }
          const script = document.createElement('script');
          script.src = "https://api-maps.yandex.ru/v3/?apikey=3e1b5b71-7984-40b2-b1be-bbcf1825d105&lang=ru_RU";
          script.onload = () => {
            ymaps3.ready.then(() => resolve(ymaps3));
          };
          document.body.appendChild(script);
        })`
    ]
  },
  stats: 'errors-warnings',
  devtool: 'cheap-module-source-map',
  devServer: {
    historyApiFallback: true,
    hot: true,
    open: true,
    port: 8180,
  },
  optimization: {
    splitChunks: {
      chunks: 'all',
    },
  },
  performance: {
    hints: false,
  },
};
