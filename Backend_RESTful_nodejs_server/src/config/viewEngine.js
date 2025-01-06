const path = require('path')
const express = require('express')

const config_viewEngine = (app) => {
    console.log(path.join('./src', 'views'))
    // Config template engine
    app.set('views', path.join('./src', 'views'))
    app.set('views engine', 'ejs')

    // Config static files
    app.use(express.static(path.join('./src', 'public')))
}

module.exports = config_viewEngine;