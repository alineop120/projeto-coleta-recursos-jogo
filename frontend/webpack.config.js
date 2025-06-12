const path = require('path');

module.exports = {
    entry: './src/index.js', // Ajuste se o caminho for diferente
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'bundle.js',
    },
    mode: 'development', // Isso evita warnings
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,         // Aplica para .js e .jsx
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',    // Fundamental para interpretar JSX
                },
            },
            {
                test: /\.css$/,              // Para interpretar arquivos CSS
                use: ['style-loader', 'css-loader'],
            },
        ],
    },
    resolve: {
        extensions: ['.js', '.jsx'],     // Permite importar arquivos sem extensão
    },
    devServer: {
        static: path.resolve(__dirname, 'public'),
        port: 8080,
        open: true,
    },
};
