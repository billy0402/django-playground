const path = require('path');

const TsconfigPathsPlugin = require('tsconfig-paths-webpack-plugin');
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  webpack: function (config, env) {
    config.output = {
      path: path.resolve('./build/webpack_bundles/'),
      filename: 'static/js/[name].[hash].js',
      chunkFilename: 'static/js/[name].[hash].chunk.js',
    };
    config.resolve.plugins.push(new TsconfigPathsPlugin({}));
    config.plugins.push(
      new BundleTracker({ filename: `./webpack-stats-${env}.json` }),
    );
    return config;
  },
};
