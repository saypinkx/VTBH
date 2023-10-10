module.exports = {
  mode: 'production',
  entry: ['./src/index.tsx'],
  module: {
    rules: require('./webpack.rules'),
  },
  output: {
    filename: '[name].[chunkhash].js',
    chunkFilename: '[name].[chunkhash].chunk.js',
    clean: true,
  },
  plugins: [...require('./webpack.plugins')],
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
      `promise new Promise((resolve) => {
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
  devServer: {
    historyApiFallback: true,
    host: '0.0.0.0',
    port: 8180,
  },
  optimization: {
    minimize: true,
    sideEffects: true,
    concatenateModules: true,
    runtimeChunk: 'single',
    splitChunks: {
      chunks: 'all',
      maxInitialRequests: 10,
      minSize: 0,
      cacheGroups: {
        vendor: {
          name: 'vendors',
          test: /[\\/]node_modules[\\/]/,
          chunks: 'all',
        },
      },
    },
  },
};
