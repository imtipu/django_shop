const mix = require('laravel-mix');

mix.sass('resources/scss/dashboard/dashboard.scss', 'static/dashboard/css/')
    .sass('resources/scss/frontend/styles.scss', 'static/shop/css/')
    .options({
        hmrOptions: {
            host: '127.0.0.1',
            port: 8000
        }
    })
    .setPublicPath('static');
