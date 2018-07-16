var q = async.queue(function(file, callback) {
    fs.readFile(file, 'utf-8', callback);
}, 2);
q.drain = function() {
    //完成队列中的所有任务
};
fs.readdirSync('.').forEach(function(file) {
    q.push(file, function(err, data) {
        // TODO 
    });
})