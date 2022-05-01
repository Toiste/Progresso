exports.middlewareGlobal = (req, res ,next) => {
    console.log();
    next();
}

exports.outroMiddleware = (req,res,next) => {
    next();
};

exports.checkCsrfError = (err, req, res, next) => {
    if(err && 'EBADCSRFTOKEN' === err.code) {
        return res.send('404');
    }
};

exports.csrfMiddleware = (req, res ,next) => {
    res.locals.csrfToken = req.csrfToken();
    next();
}