function runTest() {
    assert(fs.statSync(filename).size === filesize);
    var rs = fs.createReadStream(filename, {
        highWaterMark: size,
        encoding: encoding
    });
    rs.on('open', function() {
        bench.start();
    });
    var bytes = 0;
    rs.on('data', function(chunk) {
        bytes += chunk.length;
    });
    rs.on('end', function() {
        try { fs.unlinkSync(filename); } catch (e) {} // MB/sec
        bench.end(bytes / (1024 * 1024));
    });
}